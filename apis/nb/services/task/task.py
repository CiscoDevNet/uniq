"""
Copyright 2016 Cisco Systems

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import time
import json
from http.client import NOT_FOUND

from requests.exceptions import HTTPError

from uniq.apis.nb.services.services import Services
from uniq.apis.exceptions import ApiClientException

class Task(Services):
    """ Utility to use Task service. """

    POLL_FREQUENCY = 3  # seconds
    TASK_DEFAULT_TIMEOUT = 60  # seconds

    GET_TASK_MAX_RETRIES = 6
    EXPONENTIAL_BACKOFF_MULTIPLIER = 2

    def __wait_for_task_complete(self, task_id, timeout=TASK_DEFAULT_TIMEOUT,
                                 poll_frequency=POLL_FREQUENCY):
        """ Waits for task complete.

        Args:
            task_id (str): Id of the task.
            timeout (float): timeout in seconds.
            poll_frequency (float): poll frequency in seconds of getting task status

        Returns:
            the failure/success response of the task.
        """

        def get_task_status(task_id):
            """ Get task status.

            Args:
                task_id (str): id of task to check.

            Returns:
                task_response(AugmentedTaskDTO) if task is complete, else return False.
            """

            task_response = self.__get_task_response(task_id)
            if self.__is_task_success(task_response) or self.__is_task_failed(task_response):
                return task_response
            else:
                return False

        task_response = self.utils.wait.until(
            get_task_status, task_id=task_id, timeout=timeout, interval=poll_frequency,
            message="Task didn't finish in {} seconds.".format(timeout))
        return task_response

    def __wait_for_task_success(self, task_id=None, timeout=TASK_DEFAULT_TIMEOUT,
                                poll_frequency=POLL_FREQUENCY):
        """ Waits for task to be success for a given task_id.

        Args:
            task_id (str): Id of the task.
            timeout (float): timeout in seconds.
            poll_frequency (float): poll frequency in seconds of getting task status

        Returns:
            the failure/success response of the task.
        """

        task_response = self.__wait_for_task_complete(task_id, timeout, poll_frequency)

        if self.__is_task_success(task_response):
            return task_response
        elif self.__is_task_failed(task_response):
            raise ApiClientException(
                "Task Failed. errorCode: {}, failure reason: {}, progress: {}".format(
                    task_response.errorCode, task_response.failureReason, task_response.progress))

    def __wait_for_task_failure(self, task_id=None, timeout=TASK_DEFAULT_TIMEOUT,
                                poll_frequency=POLL_FREQUENCY):
        """ Waits for the task to be failure for a given task_id

        Args:
            task_id (str): task_id is waiting for the failure status.
            timeout (int): time_out value to wait for failure status of the task.
            poll_frequency (float): poll frequency in seconds of getting task status.

        Returns:
            the failure/success response of the task.
        """

        task_response = self.__wait_for_task_complete(task_id, timeout, poll_frequency)
        if self.__is_task_failed(task_response):
            return task_response
        elif self.__is_task_success(task_response):
            raise ApiClientException("Task expected to fail, but actually succeed.")

    def wait_for_task_success(self, task_id_result, timeout=TASK_DEFAULT_TIMEOUT,
                              poll_frequency=POLL_FREQUENCY):
        """ Waits for task to be success for a given task_id.

        Args:
            task_id_result (TaskIdResult): TaskIdResult object is waiting for the failure status.
            timeout (float): timeout (in seconds) value to wait for failure status of the task.
            poll_frequency (float): poll frequency in seconds of getting task status.

        Returns:
            the failure/success response of the task.
        """

        task_id = self.get_task_id_from_task_id_result(task_id_result)
        return self.__wait_for_task_success(task_id=task_id, timeout=timeout,
                                            poll_frequency=poll_frequency)

    def wait_for_task_failure(self, task_id_result, timeout=TASK_DEFAULT_TIMEOUT,
                              poll_frequency=POLL_FREQUENCY):
        """ Waits for the task to be failure for a given task_id

        Args:
            task_id_result (TaskIdResult): TaskIdResult object is waiting for the failure status.
            timeout (float): timeout (in seconds) value to wait for failure status of the task.
            poll_frequency (float): poll frequency in seconds of getting task status.

        Returns:
            the failure/success response of the task.
        """

        task_id = self.get_task_id_from_task_id_result(task_id_result)
        return self.__wait_for_task_failure(task_id=task_id, timeout=timeout,
                                            poll_frequency=poll_frequency)

    def wait_for_task_complete(self, task_id_result, timeout=TASK_DEFAULT_TIMEOUT,
                               poll_frequency=POLL_FREQUENCY):
        """ Waits for task complete.

        Args:
            task_id (str): Id of the task.
            timeout (float): timeout in seconds.
            poll_frequency (float): poll frequency in seconds of getting task status.

        Returns:
            the failure/success response of the task.
        """

        task_id = self.get_task_id_from_task_id_result(task_id_result)
        return self.__wait_for_task_complete(task_id=task_id, timeout=timeout,
                                             poll_frequency=poll_frequency)

    def __get_task_response(self, task_id):
        """ Get task response by task id.

        Args:
            task_id (str): id of the task.

        Returns:
            task_response (AugmentedTaskDTO) of the task.
        """

        retry_interval = 1
        retries = self.GET_TASK_MAX_RETRIES
        for retry in range(retries):
            try:
                task_result = self.nb_api.task.getTask(taskId=task_id)
                task_response = task_result.response
                return task_response
            except HTTPError as err:
                error_code = err.response.status_code
                error_result = err.response._content.decode()
                if error_code == NOT_FOUND:
                    if retry < retries - 1:
                        time.sleep(retry_interval)
                        retry_interval *= self.EXPONENTIAL_BACKOFF_MULTIPLIER
                    else:
                        raise ApiClientException(
                            "Max retries ({0}) exceeded\nHTTP error code: {1}\nerror result: {2}"
                            .format(retries, error_code, json.loads(error_result)))
                else:
                    raise ApiClientException("HTTP error code: {0}\nerror result: {1}"
                                             .format(error_code, json.loads(error_result)))
        raise ApiClientException("Didn't get any valid task response for '{}'".format(task_id))

    def __is_task_failed(self, task_response):
        """ Returns true if task failed.

        Args:
            task_response(AugmentedTaskDTO): object of task response.
        """

        return task_response.isError is True

    def __is_task_success(self, task_response, error_codes=None):
        """ Returns true if task succeed.

        Args:
            task_response(AugmentedTaskDTO): object of task response.
            error_codes (list[str]): error codes to treat as success.

        Returns:
            true if task succeed.
        """

        if error_codes and hasattr(task_response, 'errorCode'):
            return task_response.errorCode in error_codes

        return not (task_response.isError or task_response.endTime is None)

    def get_task_id_from_task_id_result(self, task_id_result):
        """ Gets task id from TaskIdResult object.

        Args:
            task_id_result (TaskIdResult): TaskIdResult object.

        Returns:
            task_id (str).
        """

        return task_id_result.response.taskId

    def get_task_progress(self, task_id_result):
        """ Gives the progress of the task from task response

        Args:
            task_id_result (TaskIdResult): TaskIdResult object

        Returns:
            progress (str): the progress (current state) of the task
        """

        task_id = self.get_task_id_from_task_id_result(task_id_result)
        task_dto_response = self.__get_task_response(task_id)
        return task_dto_response.progress

    def get_task_tree(self, task_id, timeout=TASK_DEFAULT_TIMEOUT, poll_frequency=POLL_FREQUENCY):
        """ Returns the task objects of the parent and child task

        Args:
            task_id (str): task id
            timeout (int) : default wait time

        Returns:
            task_list_response (TaskDTOListResponse object): list with parent and child task objects
        """

        def task_tree_results(task_id):
            """ Get task tree results.

            Args:
                task_id (str): task id.

            Returns:
                task_list_response (TaskDTOListResponse) if found 2 or more tasks, else return False
            """

            task_list_response = self.nb_api.task.getTaskTree(taskId=task_id).response
            if len(task_list_response) > 1:
                return task_list_response
            else:
                return False

        return self.utils.wait.until(
            task_tree_results,
            task_id=task_id,
            timeout=timeout,
            interval=poll_frequency)

    def is_task_tree_success(self, task_id_result):
        """ Returns true if all tasks in task tree are successful.

        Args:
            task_id_result (TaskIdResult): TaskIdResult object to check.

        Returns:
            True if all tasks in stask tree succeed, if any task failed, return False.
        """

        task_response = self.wait_for_task_complete(task_id_result=task_id_result)
        if self.__is_task_failed(task_response):
            return False
        task_id = self.get_task_id_from_task_id_result(task_id_result=task_id_result)
        task_list_response = self.nb_api.task.getTaskTree(taskId=task_id).response

        for task in task_list_response:
            if self.__is_task_failed(task):
                return False
        return True

    def is_task_success(self, task_id_result=None, error_codes=None):
        """ Returns true if task succeed.

        Args:
            task_id_result (TaskIdResult): TaskIdResult object to check.
            error_codes (list[str]): error_codes considered as success.

        Returns:
            True if task succeed.
        """

        task_response = self.wait_for_task_complete(task_id_result=task_id_result)
        return self.__is_task_success(task_response=task_response, error_codes=error_codes)

    def is_task_failure(self, task_id_result=None):
        """ Returns true if task failed.

        Args:
            task_id_result (TaskIdResult): TaskIdResult object to check.

        Returns:
            True if task failed.
        """

        task_response = self.wait_for_task_complete(task_id_result=task_id_result)
        return self.__is_task_failed(task_response=task_response)

    def get_task_failure_reasons(self, task_id_result):
        """ Retrieves the task failure reasons.

        Args:
            task_id_result (TaskIdResult): TaskIdResult object to check.

        Returns:
            string containing a list of task failure reasons
        """

        task_id = self.get_task_id_from_task_id_result(task_id_result)
        task_list_response = self.get_task_tree(task_id=task_id)
        failure_reasons = []
        for task in task_list_response:
            if task.failureReason is not None:
                failure_reasons.append(task.failureReason)

        return ", ".join(failure_reasons)

    def get_task_response(self, task_id_result):
        """ Get current task response.

        Args:
            task_id_result (TaskIdResult): TaskIdResult object to check.

        Returns:
            task_response (AugmentedTaskDTO) of the task.
        """

        task_id = self.get_task_id_from_task_id_result(task_id_result)
        return self.__get_task_response(task_id)
