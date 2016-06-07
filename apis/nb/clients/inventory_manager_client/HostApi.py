#!/usr/bin/env python
#pylint: skip-file
"""
HostApi.py
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


class HostApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient



    def getHosts(self, **kwargs):
        """Retrieve hosts

        Args:

            limit, str: limit (required)


            offset, str: offset (required)


            sortBy, str: sortBy (required)


            order, str: order (required)


            hostName, list[str]: hostName (required)


            hostMac, list[str]: hostMac (required)


            hostType, list[str]: hostType (required)


            connectedInterfaceName, list[str]: connectedInterfaceName (required)


            hostIp, list[str]: hostIp (required)


            connectedDeviceIp, list[str]: connectedDeviceIp (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: HostListResult
        """

        allParams = ['limit', 'offset', 'sortBy', 'order', 'hostName', 'hostMac', 'hostType', 'connectedInterfaceName', 'hostIp', 'connectedDeviceIp', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getHosts" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/host'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])

        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])

        if ('sortBy' in params):
            queryParams['sortBy'] = self.apiClient.toPathValue(params['sortBy'])

        if ('order' in params):
            queryParams['order'] = self.apiClient.toPathValue(params['order'])

        if ('hostName' in params):
            queryParams['hostName'] = self.apiClient.toPathValue(params['hostName'])

        if ('hostMac' in params):
            queryParams['hostMac'] = self.apiClient.toPathValue(params['hostMac'])

        if ('hostType' in params):
            queryParams['hostType'] = self.apiClient.toPathValue(params['hostType'])

        if ('connectedInterfaceName' in params):
            queryParams['connectedInterfaceName'] = self.apiClient.toPathValue(params['connectedInterfaceName'])

        if ('hostIp' in params):
            queryParams['hostIp'] = self.apiClient.toPathValue(params['hostIp'])

        if ('connectedDeviceIp' in params):
            queryParams['connectedDeviceIp'] = self.apiClient.toPathValue(params['connectedDeviceIp'])



        if ('scope' in params):
            headerParams['scope'] = params['scope']








        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'HostListResult')
        return responseObject




    def getHostCount(self, **kwargs):
        """Gives total number of hosts

        Args:

            scope, str: Authorization Scope for RBAC (required)



        Returns: CountResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getHostCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/host/count'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']








        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'CountResult')
        return responseObject




    def getHostById(self, **kwargs):
        """Retrieves host based on id

        Args:

            id, str: Host Id (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: HostResult
        """

        allParams = ['id', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getHostById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/host/{id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']



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

        responseObject = self.apiClient.deserialize(response, 'HostResult')
        return responseObject






