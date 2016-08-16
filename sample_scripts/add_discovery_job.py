from uniq.apis.nb.client_manager import NbClientManager
from uniq.apis.nb.clients.inventory_manager_client.models.DiscoveryNIO import DiscoveryNIO
from uniq.utils.wait import Wait
from uniq.apis.exceptions import UniqException

def wait_for_discovery_complete(discovery_id):
    """ Waits for discovery to complete.

    Args:
        discovery_id (str): discovery id.
    """

    timeout = 60
    polling_interval = 2
    result = None

    def query_discovery_status():
        """ Get discovery condition """

        discovery_job = client.discovery.getDiscoveryById(id=discovery_id, scope="all").response

        if discovery_job.discoveryCondition == "Complete":
            devices_found = client.discovery.getNetworkDeviceCountByDiscoveryId(
                id=discovery_id,
                scope="all").response
            print("No. of devices found in discovery job: '{0}' are: {1}".format(discovery_id,
                                                                                 devices_found))
            return "Complete"
        elif discovery_job.discoveryCondition == "In Progress" or "Yet to Start":
            return False
        else:
            return "Failed"

    try:
        result = wait.until(query_discovery_status,
                            timeout=timeout,
                            interval=polling_interval,
                            message="Timeout while waiting discovery complete.")
    except UniqException:
        print("Discovery job did not Complete in {0} seconds.".format(timeout))

    if result == "Complete":
        print("Discovery job successfully completed.")
    elif result == "Failed":
        print("Discovery job failed to complete.")


client = NbClientManager(server="1.1.1.1",
                         username="username",
                         password="******",
                         connect=True)
wait = Wait()

request = {
  "name": "example_job",
  "discoveryType": "single",
  "protocolOrder": "ssh,telnet",
  "ipAddressList": "1.1.1.2",
  "retry": "3",
  "timeout": "60",
  "userNameList": ["******"],
  "passwordList": ["******"],
  "enablePasswordList": ["******"],
  "snmpROCommunity": "******",
  "snmpRWCommunity": "******",
}

print("Creating discovery job '{}'.".format(request["name"]))
task_id_result = client.discovery.insertDiscovery(request=request, scope="All")
task_id = task_id_result.response.taskId
print("Task ID - {}".format(task_id))

print("Waiting for task '{}' to complete successfully.".format(task_id))
client.task_util.wait_for_task_complete(task_id_result)

#get discovery id from task information
task_info = client.task.getTask(taskId=task_id)
discovery_id = task_info.response.progress
print("Discovery ID - {}".format(discovery_id))

#Introducing usage of services
print("Waiting for device scanning to complete.")
wait_for_discovery_complete(discovery_id)