#!/usr/bin/env python
#pylint: skip-file
"""
V2PolicyApi.py
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


class V2PolicyApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient



    def getPolicyByFilters(self, **kwargs):
        """Retrieves policies based on a given filter

        Args:

            name, str: Retrieve policies for a given name (required)


            contract+name, str: Retrieve policies for a given contract name (required)


            producer+scalableGroupName, str: Retrieve policies for a given producer scalable group name (required)


            consumer+scalableGroupName, str: Retrieve policies for a given consumer scalable group name (required)


            scalableGroupName, str: Retrieve policies for a given scalable group name (used within producer or consumer) (required)


            offset, str: Starting index of the resources (1 based) (required)


            limit, str: Number of resources to return (required)



        Returns: PolicyDTOListResult
        """

        allParams = ['name', 'contract+name', 'producer+scalableGroupName', 'consumer+scalableGroupName', 'scalableGroupName', 'offset', 'limit']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPolicyByFilters" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v2/policy'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('name' in params):
            queryParams['name'] = self.apiClient.toPathValue(params['name'])

        if ('contract+name' in params):
            queryParams['contract+name'] = self.apiClient.toPathValue(params['contract+name'])

        if ('producer+scalableGroupName' in params):
            queryParams['producer+scalableGroupName'] = self.apiClient.toPathValue(params['producer+scalableGroupName'])

        if ('consumer+scalableGroupName' in params):
            queryParams['consumer+scalableGroupName'] = self.apiClient.toPathValue(params['consumer+scalableGroupName'])

        if ('scalableGroupName' in params):
            queryParams['scalableGroupName'] = self.apiClient.toPathValue(params['scalableGroupName'])

        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])

        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])










        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'PolicyDTOListResult')
        return responseObject




    def update(self, **kwargs):
        """Create Policy(s)

        Args:

            policyDTOs, list[PolicyDTO]: Policy Object(s) (required)



        Returns: TaskIdResult
        """

        allParams = ['policyDTOs']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method update" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v2/policy'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'










        if ('policyDTOs' in params):
            bodyParam = params['policyDTOs']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def add(self, **kwargs):
        """Create Policy(s)

        Args:

            policyDTOs, list[PolicyDTO]: Policy Object(s) (required)



        Returns: TaskIdResult
        """

        allParams = ['policyDTOs']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method add" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v2/policy'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'










        if ('policyDTOs' in params):
            bodyParam = params['policyDTOs']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getCount(self, **kwargs):
        """Return total count of policies

        Args:


        Returns: CountResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v2/policy/count'
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

        responseObject = self.apiClient.deserialize(response, 'CountResult')
        return responseObject




    def getById(self, **kwargs):
        """Retrieves a policy based on its id

        Args:

            id, str: id (required)



        Returns: PolicyDTOResult
        """

        allParams = ['id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v2/policy/{id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('id' in params):
            replacement = str(self.apiClient.toPathValue(params['id']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'id' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'PolicyDTOResult')
        return responseObject




    def delete(self, **kwargs):
        """Deletes a policy by its id

        Args:

            id, str: id (required)



        Returns: TaskIdResult
        """

        allParams = ['id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method delete" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v2/policy/{id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('id' in params):
            replacement = str(self.apiClient.toPathValue(params['id']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'id' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject






