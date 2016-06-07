#!/usr/bin/env python
#pylint: skip-file
"""
UserApi.py
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
import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class UserApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient



    def getUsers(self, **kwargs):
        """getUsers

        Args:

            authSource, str: authSource (required)



        Returns: UserListResult
        """

        allParams = ['authSource']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getUsers" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/user'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('authSource' in params):
            queryParams['authSource'] = self.apiClient.toPathValue(params['authSource'])










        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'UserListResult')
        return responseObject




    def updateUser(self, **kwargs):
        """updateUser

        Args:

            user, UserReqRes: user (required)



        Returns: SuccessResult
        """

        allParams = ['user']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateUser" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/user'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'










        if ('user' in params):
            bodyParam = params['user']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SuccessResult')
        return responseObject




    def addUser(self, **kwargs):
        """addUser

        Args:

            user, UserReqRes: user (required)



        Returns: SuccessResult
        """

        allParams = ['user']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addUser" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/user'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'










        if ('user' in params):
            bodyParam = params['user']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SuccessResult')
        return responseObject




    def getUsersCache(self, **kwargs):
        """getUsersCache

        Args:


        Returns: UserListResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getUsersCache" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/user/cache'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'











        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'UserListResult')
        return responseObject




    def getAutoPassphrase(self, **kwargs):
        """getAutoPassphrase

        Args:


        Returns: AutoPassphraseResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAutoPassphrase" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/user/passphrase/auto'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'











        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'AutoPassphraseResult')
        return responseObject




    def getAutoPassphraseWithSeedPhrase(self, **kwargs):
        """getAutoPassphrase

        Args:

            seedPhrase, str: seedPhrase (required)



        Returns: AutoPassphraseResult
        """

        allParams = ['seedPhrase']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAutoPassphraseWithSeedPhrase" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/user/passphrase/auto/{seedPhrase}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('seedPhrase' in params):
            replacement = str(self.apiClient.toPathValue(params['seedPhrase']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'seedPhrase' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'AutoPassphraseResult')
        return responseObject




    def getAttemptCount(self, **kwargs):
        """getAttemptCount

        Args:


        Returns: UserLoginInvalidAttemptCountResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAttemptCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/user/password-policy/invalid-attempt-count'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'











        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'UserLoginInvalidAttemptCountResult')
        return responseObject




    def updateAttemptCount(self, **kwargs):
        """updateAttemptCount

        Args:

            attemptCount, UserLoginInvalidAttemptCount: attemptCount (required)



        Returns: SuccessResult
        """

        allParams = ['attemptCount']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateAttemptCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/user/password-policy/invalid-attempt-count'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'










        if ('attemptCount' in params):
            bodyParam = params['attemptCount']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SuccessResult')
        return responseObject




    def getLockExpiry(self, **kwargs):
        """getLockExpiry

        Args:


        Returns: UserLockExpiryTimeResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getLockExpiry" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/user/password-policy/lock-expiry-time'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'











        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'UserLockExpiryTimeResult')
        return responseObject




    def updateLockExpiryTimeout(self, **kwargs):
        """updateLockExpiryTimeout

        Args:

            expiryTime, UserLockExpiryTime: expiryTime (required)



        Returns: SuccessResult
        """

        allParams = ['expiryTime']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateLockExpiryTimeout" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/user/password-policy/lock-expiry-time'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'










        if ('expiryTime' in params):
            bodyParam = params['expiryTime']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SuccessResult')
        return responseObject




    def updateUserStatus(self, **kwargs):
        """updateUserStatus

        Args:

            userStatus, UserStatus: userStatus (required)



        Returns: SuccessResult
        """

        allParams = ['userStatus']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateUserStatus" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/user/status'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'










        if ('userStatus' in params):
            bodyParam = params['userStatus']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SuccessResult')
        return responseObject




    def getUserStatus(self, **kwargs):
        """getUserStatus

        Args:

            username, str: username (required)



        Returns: UserStatusResult
        """

        allParams = ['username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getUserStatus" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/user/status/{username}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('username' in params):
            replacement = str(self.apiClient.toPathValue(params['username']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'username' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'UserStatusResult')
        return responseObject




    def getUser(self, **kwargs):
        """getUser

        Args:

            username, str: username (required)



        Returns: UserResult
        """

        allParams = ['username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getUser" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/user/{username}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('username' in params):
            replacement = str(self.apiClient.toPathValue(params['username']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'username' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'UserResult')
        return responseObject




    def deleteUser(self, **kwargs):
        """deleteUser

        Args:

            username, str: username (required)



        Returns: SuccessResult
        """

        allParams = ['username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteUser" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/user/{username}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('username' in params):
            replacement = str(self.apiClient.toPathValue(params['username']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'username' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SuccessResult')
        return responseObject






