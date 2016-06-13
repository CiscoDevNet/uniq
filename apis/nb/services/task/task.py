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

from requests.exceptions import HTTPError
from http.client import NOT_FOUND

class Task(object):
    '''
    Utility to use Task service
    '''

    POLL_FREQUENCY = 3  # seconds
    TASK_DEFAULT_TIMEOUT = 60  # seconds

    SERVICE_TYPE = 'serviceType'
    PROGRESS = 'progress'

    GET_TASK_MAX_RETRIES = 6
    EXPONENTIAL_BACKOFF_MULTIPLIER = 2

    def __init__(self, task):
        """ Constructor of task service.

        Args:
            task (TaskApi): initalized TaskApi instance.
        """

        self.__task_api = task


    def __wait_for_task_complete(self, task_id=None, timeout=TASK_DEFAULT_TIMEOUT,
                                 poll_frequency=POLL_FREQUENCY):
        """ Waits for task complete.

        Args:
            task_id (str): Id of the task.
            timeout (float): timeout in seconds.
            poll_frequency (float): poll frequency in seconds of getting task status

        Returns:
            the failure/success response of the task.
        """

        assert task_id is not None
        task_completed = False

        start_time = time.time()
        while not task_completed:
            if (time.time() > (start_time + timeout)):
                assert False, ("Task {0} didn't complete within {1} seconds"
                               .format(task_response.__dict__, timeout))
            task_response = self.__get_task_response(task_id)
            if self.__is_task_success(task_response) or self.__is_task_failed(task_response):
                task_completed = True
                return task_response
            else:
                time.sleep(poll_frequency)
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
            assert False, ("Task failed, task response {0}".format(task_response.__dict__))

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
            assert False, ("Task successed, task response {0}".format(task_response.__dict__))

    def wait_for_task_success(self, task_id_result=None, timeout=TASK_DEFAULT_TIMEOUT,
                              poll_frequency=POLL_FREQUENCY):
        """ Waits for task to be success for a given task_id.

        Args:
            task_id_result (TaskIdResult): TaskIdResult object is waiting for the failure status.
            timeout (float): timeout in seconds.
            poll_frequency (float): poll frequency in seconds of getting task status.

        Returns:
            the failure/success response of the task.
        """

        assert task_id_result is not None
        task_id = self.get_task_id_from_task_id_result(task_id_result)
        return self.__wait_for_task_success(task_id=task_id, timeout=timeout,
                                            poll_frequency=poll_frequency)

    def wait_for_task_failure(self, task_id_result, timeout=TASK_DEFAULT_TIMEOUT,
                              poll_frequency=POLL_FREQUENCY):
        """ Waits for the task to be failure for a given task_id

        Args:
            task_id_result (TaskIdResult): TaskIdResult object is waiting for the failure status.
            timeout (int): time_out value to wait for failure status of the task.
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
                task_result = self.__task_api.getTask(taskId=task_id)
                assert task_result is not None

                task_response = task_result.response
                assert task_response is not None

                return task_response
            except HTTPError as err:
                error_code = err.response.status_code
                error_result = err.response._content.decode()
                if error_code == NOT_FOUND:
                    if retry < retries - 1:
                        time.sleep(retry_interval)
                        retry_interval *= self.EXPONENTIAL_BACKOFF_MULTIPLIER
                    else:
                        assert False, ("Max retries ({0}) exceeded\nHTTP error code: "
                                       "{1}\nerror result: {2}".format(retries,
                                                                       error_code,
                                                                       json.loads(error_result)))
                else:
                    assert False, ("HTTP error code: {0}\nerror result: {1}"
                                   .format(error_code, json.loads(error_result)))

    def __is_task_failed(self, task_response):
        assert task_response is not None
        return task_response.isError == True

    def __is_task_success(self, task_response, error_codes=[]):
        """
        :type error_codes: list
        """
        assert task_response is not None
        for error_code in error_codes:
            if (error_code is not None and hasattr(task_response, 'errorCode')
                and error_code == task_response.errorCode):
                return True
        is_not_error = task_response.isError is None or task_response.isError == False
        is_end_time_present = task_response.endTime is not None
        return (is_not_error and is_end_time_present)

    def get_task_id_from_task_id_result(self, task_id_result):
        assert task_id_result is not None
        task_id_response = task_id_result.response
        assert task_id_response is not None
        task_id = task_id_response.taskId
        assert task_id is not None
        return task_id

    def get_task_progress(self, task_id_result):
        """ Gives the progress of the task from task response

        Args:
            task_id_result (TaskIdResult object): TaskIdResult object

        Returns:
            progress (str): the progress (current state) of the task
        """

        task_id = task_id_result.response.taskId
        task_dto_response = self.__task_api.getTask(taskId=task_id).response
        return task_dto_response.progress

    def get_task_tree(self, task_id, timeout=None):
        """ Returns the task objects of the parent and child task

        Args:
            task_id (str): task id
            timeout (int) : default wait time

        Returns:
            task_list_response (TaskDTOListResponse object): list with parent and child task objects
        """

        if timeout is None:
            timeout = self.TASK_DEFAULT_TIMEOUT

        task_list_response = self.__task_api.getTaskTree(taskId=task_id).response

        start_time = time.time()
        while (len(task_list_response) == 1):
            if (time.time() > (start_time + timeout)):
                break
            time.sleep(1)
            task_list_response = self.__task_api.getTaskTree(taskId=task_id).response

        return task_list_response

    def is_task_tree_success(self, task_id_result=None):
        assert task_id_result is not None
        self.wait_for_task_success(task_id_result=task_id_result)
        task_id = self.get_task_id_from_task_id_result(task_id_result=task_id_result)
        task_list_result = self.__task_api.getTaskTree(taskId=task_id)
        assert task_list_result is not None

        task_list_response = task_list_result.response
        assert task_list_response is not None

        for task in task_list_response:
            assert self.__is_task_success(task_response=task), ("Task failed, task response {0}"
                                                                .format(task.__dict__))
        return True

    def is_task_success(self, task_id_result=None, error_codes=[]):
        """
        :type error_codes: list
        """
        assert task_id_result is not None
        task_response = self.wait_for_task_complete(task_id_result=task_id_result)
        assert task_response is not None , "Task is completed but response is None"
        return self.__is_task_success(task_response=task_response, error_codes=error_codes)

    def is_task_failure(self, task_id_result=None):
        assert task_id_result is not None
        task_response = self.wait_for_task_complete(task_id_result=task_id_result)
        assert task_response is not None , "Task is completed but response is None"
        return self.__is_task_failed(task_response=task_response)

    def get_task_failure_reasons(self, task_id):
        """ Retrieves the task failure reasons.

        Args:
            task_id (TaskIdResult object): TaskIdResult object

        Returns:
            string containing a list of task failure reasons
        """

        task_id = task_id.response.taskId
        task_list_response = self.get_task_tree(task_id=task_id)
        failure_reasons = []
        for task in task_list_response:
            if task.failureReason is not None:
                failure_reasons.append(task.failureReason)

        return ", ".join(failure_reasons)

    def get_task_response(self, task_id):
        return self.__get_task_response(task_id)
