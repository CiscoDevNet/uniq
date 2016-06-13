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

print('Creating policy tag "example_tag".')
response = client.policy.addPolicyTag(policyTagDTO={'policyTag': 'example_tag'})
print('Waiting for task complete successfully.')
client.task_util.wait_for_task_success(response, timeout=3, poll_frequency=0.5)

print('Deleting policy tag "example_tag".')
response = client.policy.deletePolicyTag(policyTag='example_tag')
print('Waiting for task complete successfully.')
client.task_util.wait_for_task_success(response)

example_policy_service = ExamplePolicyService(client)
tag_name = 'new_tag'
example_policy_service.add_policy_tag(tag_name)
example_policy_service.delete_policy_tag(tag_name)
