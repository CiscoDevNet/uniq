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


class Wait(object):
    """ Utility to wait. """

    TIMEOUT = 60
    INTERVAL = 1
    IGNORED_EXCEPTIONS = tuple()

    def __init__(self, timeout=TIMEOUT, interval=INTERVAL, ignored_exceptions=IGNORED_EXCEPTIONS):
        """ Initializer of Wait Util.

        Args:
            timeout (int): Number of seconds before timing out.
            interval (int): Sleep interval between calls.
            ignored_exceptions (list(Exception)): Exceptions to ignore.
        """

        self.log = logger
        self._timeout = timeout
        self._interval = interval
        if type(ignored_exceptions) is list:
            ignored_exceptions = tuple(ignored_exceptions)

        self._ignored_exceptions = ignored_exceptions

    def until(self, method, timeout=None, interval=None, ignored_exceptions=None, message='',
              *args, **kwargs):
        """ Calls the method provided until the return value is not False.

        Args:
            method (function): method to call for checking status.
            timeout (int): Number of seconds before timing out.
            interval (int): Sleep interval between calls.
            ignored_exceptions (list(Exception)): Exceptions to ignore.
            message (str): Message shows in TimeoutException.
            args (list): Arguments of method.
            kwargs (dict): Dictionary of arguments of method.

        Returns:
            Value of method if value is not False.

        Raises:
            TimeoutException if value of method is still False when time's up.
        """

        return self._until(method, False, timeout, interval, ignored_exceptions, message,
                           *args, **kwargs)

    def until_not(self, method, timeout=None, interval=None, ignored_exceptions=None, message='',
                  *args, **kwargs):
        """ Calls the method provided until the return value is False.

        Args:
            method (function): method to call for checking status.
            timeout (int): Number of seconds before timing out.
            interval (int): Sleep interval between calls.
            ignored_exceptions (list(Exception)): Exceptions to ignore.
            message (str): Message shows in TimeoutException.
            args (list): Arguments of method.
            kwargs (dict): Dictionary of arguments of method.

        Returns:
            False if value of method turns to False in time.

        Raises:
            TimeoutException if value of method is not False when time's up.
        """

        self._until(method, True, timeout, interval, ignored_exceptions, message,
                    *args, **kwargs)
        return False

    def _until(self, method, wait_false=False, timeout=None, interval=None, ignored_exceptions=None,
               message='', *args, **kwargs):
        """ Calls the method provided until the return value is not False.

        Args:
            method (function): method to call for checking status.
            wait_false (bool): true if wait method return value is not False, otherwise, wait return
                               value become False.
            timeout (int): Number of seconds before timing out.
            interval (int): Sleep interval between calls.
            ignored_exceptions (list(Exception)): Exceptions to ignore.
            message (str): Message shows in TimeoutException.
            args (list): Arguments of method.
            kwargs (dict): Dictionary of arguments of method.

        Returns:
            Value of method if value is not False. False if timeout.

        Raises:
            TimeoutException if value of method is still False when time's up.
        """

        if timeout is None:
            timeout = self._timeout
        if interval is None:
            interval = self._interval
        if ignored_exceptions is None:
            ignored_exceptions = self._ignored_exceptions
        else:
            ignored_exceptions = tuple(ignored_exceptions)

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
            time.sleep(interval)
            if time.time() > end_time:
                break
        raise TimeoutException(message)

class TimeoutException(Exception):
    pass


