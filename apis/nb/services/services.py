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
try:
    from uniq.common import logger
    logger = logger.log
except:
    import logging
    logger = logging.getLogger("uniq")
from uniq.utils import utils


class Services(object):
    """ Services base class"""

    DEFAULT_TIMEOUT = 60  # seconds
    DEFAULT_POLL_FREQUENCY = 1 # seconds

    def __init__(self, nb_api, *args, **kwargs):
        """ Initializer makes available the nb_api client and logger to objects of this class.

        Args:
            nb_api (NbClientManager): instance of NbClientManager
        """

        super().__init__(*args, **kwargs)

        self.nb_api = nb_api
        self.log = logger
        self.utils = utils

    def serialize(self, model):
        """ Serializes any service's model object into dictionary.

        Args:
            model (swagger model object): object of swagger model class

        Returns:
            a serialized dict of the swagger model object
        """

        self.log.info("Serializing swagger model object: {0}".format(model.__class__.__name__))
        return self.nb_api.serialize(model)

    def handle_task(self, task, task_status=None, timeout=DEFAULT_TIMEOUT,
                    poll_frequency=DEFAULT_POLL_FREQUENCY):
        """ Returns the task response for a task on completion

        By default it will only wait for the task to complete, it can be made to wait for a
        particular state (Success/Failure), depending on the argument value of task_status.

        Args:
            task (TaskIdResult): an object of the task response
            task_status (str): task status to wait for (Success/Failure). Default is None
            timeout (float): Number of seconds before timing out.
            poll_frequency (float): Sleep interval between calls.
        """

        if task_status:
            if task_status.lower() == "success":
                return self.nb_api.task_util.wait_for_task_success(task, timeout, poll_frequency)
            elif task_status.lower() == "failure":
                return self.nb_api.task_util.wait_for_task_failure(task, timeout, poll_frequency)
            else:
                raise Exception('Unrecognized task status "{}".'.format(task_status))
        return self.nb_api.task_util.wait_for_task_complete(task, timeout, poll_frequency)

    def waits_until(self, method, timeout=DEFAULT_TIMEOUT, poll_frequency=DEFAULT_POLL_FREQUENCY,
                    ignored_exceptions=None, message='', *args, **kwargs):
        """ Calls the method provided until the return value is not False.

        Args:
            method (function): method to call for checking status.
            timeout (float): Number of seconds before timing out.
            poll_frequency (float): Sleep interval between calls.
            ignored_exceptions (list(Exception)): Exceptions to ignore.
            message (str): Message shows in TimeoutException.
            args (list): Arguments of method.
            kwargs (dict): Dictionary of arguments of method.

        Returns:
            Value of method if value is not False.

        Raises:
            TimeoutException if value of method is still False when time's up.
        """

        return self._waits_until(method, False, timeout, poll_frequency, ignored_exceptions, message,
                                 *args, **kwargs)

    def waits_until_not(self, method, timeout=DEFAULT_TIMEOUT,
                        poll_frequency=DEFAULT_POLL_FREQUENCY, ignored_exceptions=None,
                        message='', *args, **kwargs):
        """ Calls the method provided until the return value is False.

        Args:
            method (function): method to call for checking status.
            timeout (float): Number of seconds before timing out.
            poll_frequency (float): Sleep interval between calls.
            ignored_exceptions (list(Exception)): Exceptions to ignore.
            message (str): Message shows in TimeoutException.
            args (list): Arguments of method.
            kwargs (dict): Dictionary of arguments of method.

        Returns:
            False if value of method turns to False in time.

        Raises:
            TimeoutException if value of method is not False when time's up.
        """

        self._waits_until(method, True, timeout, poll_frequency, ignored_exceptions, message,
                          *args, **kwargs)
        return False

    def _waits_until(self, method, wait_false=False, timeout=DEFAULT_TIMEOUT,
                     poll_frequency=DEFAULT_POLL_FREQUENCY,
                     ignored_exceptions=None, message='', *args, **kwargs):
        """ Calls the method provided until the return value is not False.

        Args:
            method (function): method to call for checking status.
            wait_false (bool): true if wait method return value is not False, otherwise, wait return
                               value become False.
            timeout (float): Number of seconds before timing out.
            poll_frequency (float): Sleep interval between calls.
            ignored_exceptions (list(Exception)): Exceptions to ignore.
            message (str): Message shows in TimeoutException.
            args (list): Arguments of method.
            kwargs (dict): Dictionary of arguments of method.

        Returns:
            Value of method if value is not False. False if timeout.

        Raises:
            TimeoutException if value of method is still False when time's up.
        """

        if ignored_exceptions:
            ignored_exceptions = tuple(ignored_exceptions)
        else:
            ignored_exceptions = tuple()

        if not message:
            message = ("Timeout, didn't get any non-False value from method {} in {} seconds."
                       .format(method, timeout))

        start_time = time.time()
        self.log.debug("Begins at {0}".format(start_time))

        end_time = start_time + timeout
        while True:
            try:
                value = method(*args, **kwargs)
                if wait_false:
                    value = not value
                if value is not False:
                    self.log.debug("Waited for {0} seconds.".format(time.time() - start_time))
                    return value
            except ignored_exceptions as exc:
                self.log.debug("Ignore exception: {0}:{1}".format(type(exc), exc))
            except:
                raise
            time.sleep(poll_frequency)
            if time.time() > end_time:
                break
        raise TimeoutException(message)


