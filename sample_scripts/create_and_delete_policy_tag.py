from uniq.apis.nb.services.services import Services
import login

class ExamplePolicyService(Services):
    """ Example Policy service class. """

    def add_policy_tag(self, tag_name):
        """ Add a new policy tag.

        Args:
            tag_name (str): name of tag.
        """

        print('Creating new policy tag "{}" using self-defined service.'.format(tag_name))
        task = self.nb_api.policy.addPolicyTag(policyTagDTO={'policyTag': tag_name})
        self.handle_task(task, 'Success')

    def delete_policy_tag(self, tag_name):
        """ Delete policy tag.

        Args:
            tag_name (str): name of tag.
        """

        print('Deleting policy tag "{}" using self-defined service.'.format(tag_name))
        task = self.nb_api.policy.deletePolicyTag(policyTag=tag_name)
        self.handle_task(task, 'Success')

client = login.login()

tag_name = 'example_tag'
print('Creating policy tag "{}".'.format(tag_name))
task_id_result = client.policy.addPolicyTag(policyTagDTO={'policyTag': tag_name})
print('Waiting for task complete successfully.')
client.task_util.wait_for_task_success(task_id_result, timeout=3, poll_frequency=0.5)

print('Trying to create duplicated policy tag "{}".'.format(tag_name))
task_id_result = client.policy.addPolicyTag(policyTagDTO={'policyTag': tag_name})
failed = client.task_util.is_task_failure(task_id_result)
if failed:
    print('The task failed.')
    failure_reason = client.task_util.get_task_failure_reasons(task_id_result)
    print('Failure reason: {}'.format(failure_reason))

print('Deleting policy tag "example_tag".')
task_id_result = client.policy.deletePolicyTag(policyTag='example_tag')
print('Waiting for task complete successfully.')
client.task_util.wait_for_task_success(task_id_result)
client.task_util.is_task_tree_success(task_id_result)

example_policy_service = ExamplePolicyService(client)
tag_name = 'new_tag'
example_policy_service.add_policy_tag(tag_name)
example_policy_service.delete_policy_tag(tag_name)
