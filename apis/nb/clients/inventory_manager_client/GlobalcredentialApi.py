#!/usr/bin/env python
#pylint: skip-file
"""
GlobalcredentialApi.py
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


class GlobalcredentialApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient



    def getGlobalCredential(self, **kwargs):
        """getGlobalCredential

        Args:

            credentialSubType, str: Credential type as CLI / SNMPV2_READ_COMMUNITY / SNMPV2_WRITE_COMMUNITY / SNMPV3 (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: GlobalCredentialListResult
        """

        allParams = ['credentialSubType', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getGlobalCredential" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/global-credential'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('credentialSubType' in params):
            queryParams['credentialSubType'] = self.apiClient.toPathValue(params['credentialSubType'])



        if ('scope' in params):
            headerParams['scope'] = params['scope']








        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GlobalCredentialListResult')
        return responseObject




    def addCliCredential(self, **kwargs):
        """addCliCredential

        Args:

            globalCredentialNioList, list[CLICredentialDTO]: globalCredentialNioList (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['globalCredentialNioList', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addCliCredential" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/global-credential/cli'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']







        if ('globalCredentialNioList' in params):
            bodyParam = params['globalCredentialNioList']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def addSnmpReadCommunity(self, **kwargs):
        """addSnmpReadCommunity

        Args:

            globalCredentialNioList, List[SNMPv2ReadCommunityDTO]: globalCredentialNioList (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['globalCredentialNioList', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addSnmpReadCommunity" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/global-credential/snmpv2-read-community'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']







        if ('globalCredentialNioList' in params):
            bodyParam = params['globalCredentialNioList']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def addSnmpWriteCommunity(self, **kwargs):
        """addSnmpWriteCommunity

        Args:

            globalCredentialNioList, List[SNMPv2WriteCommunityDTO]: globalCredentialNioList (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['globalCredentialNioList', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addSnmpWriteCommunity" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/global-credential/snmpv2-write-community'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']







        if ('globalCredentialNioList' in params):
            bodyParam = params['globalCredentialNioList']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def addSnmpv3Credential(self, **kwargs):
        """addSnmpv3Credential

        Args:

            globalCredentialNioList, List[SNMPv3CredentialDTO]: globalCredentialNioList (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['globalCredentialNioList', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addSnmpv3Credential" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/global-credential/snmpv3'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']







        if ('globalCredentialNioList' in params):
            bodyParam = params['globalCredentialNioList']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def deleteGlobalCredential(self, **kwargs):
        """deleteGlobalCredential

        Args:

            globalCredentialId, str: globalCredentialId (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['globalCredentialId', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteGlobalCredential" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/global-credential/{globalCredentialId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']



        if ('globalCredentialId' in params):
            replacement = str(self.apiClient.toPathValue(params['globalCredentialId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'globalCredentialId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject






