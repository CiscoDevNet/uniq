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

import logging
logger = logging.getLogger("uniq")

class UniqException(Exception):
    """ Base exception class in uniq takes an error message to get initialized

    It makes a log entry of level exception using the error message used while calling
    UniqException. The log entry has a tag of [UniqException], for the purpose of
    easy filtering.

    UniqException can be directly raised as an exception as well.

    Usage:
        raise UniqException("error_message")
    """

    # Class variable to keep count of the number of times the UniqException is raised in
    # the life of a test case.
    __COUNTER = 0

    __EXTRA_ACTIONS = set()

    def __init__(self, error_message):
        """ Initializes the test exception instance. """

        super(UniqException, self).__init__()
        self.__class__.__COUNTER += 1
        logger.error("[{0}] {1}".format(self.__class__.__name__, error_message))
        self.error_message = error_message
        for action in self.__class__.__EXTRA_ACTIONS:
            action()

    def __str__(self):
        return self.error_message

class ApiClientException(UniqException):
    """ Exception class for API specific scenarios"""

    def __init__(self, message=None):
        super(ApiClientException, self).__init__(message)

    @staticmethod
    def raise_exception(message=None, code=None):
        """ Raises exception based on the error code

        Args:
            message(str): response
            code (int): status code of the response
        """

        if code == 400:
            #TODO (hikoppu): Add more expections if any, which raise 404
            raise InvalidContentException(message)
        elif code == 401:
            raise UnauthorizedException(message)
        elif code == 404:
            #TODO (hikoppu): Add more expections if any, which raise 404
            raise ApiNotFoundException(message)

class ConnectionException(ApiClientException):
    def __init__(self, message=None):
        super(ConnectionException, self).__init__(
            message if message else "Connection to the server failed.")

class InvalidContentException(ApiClientException):
    def __init__(self, message=None):
        super(InvalidContentException, self).__init__(
            message if message else "Invalid content in request. ")

class UnauthorizedException(ApiClientException):
    def __init__(self, message=None):
        super(UnauthorizedException, self).__init__(
            message if message else "Unable to autheticate.")

class ApiNotFoundException(ApiClientException):
    def __init__(self, message=None):
        super(ApiNotFoundException, self).__init__(
            message if message else "Connection to the server failed.")






