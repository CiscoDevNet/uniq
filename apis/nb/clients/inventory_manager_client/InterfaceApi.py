#!/usr/bin/env python
#pylint: skip-file
"""
InterfaceApi.py
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


class InterfaceApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient



    def getInterface(self, **kwargs):
        """Retrieves all interfaces

        Args:

            scope, str: Authorization Scope for RBAC (required)



        Returns: DeviceIfListResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getInterface" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/interface'
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

        responseObject = self.apiClient.deserialize(response, 'DeviceIfListResult')
        return responseObject




    def getInterfaceCount(self, **kwargs):
        """Retrieves interface count

        Args:

            scope, str: Authorization Scope for RBAC (required)



        Returns: CountResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getInterfaceCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/interface/count'
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




    def getInterfaceListByIp(self, **kwargs):
        """Retrieves interfaces by IP address

        Args:

            ipAddress, str: IP address of the interface (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: DeviceIfListResult
        """

        allParams = ['ipAddress', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getInterfaceListByIp" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/interface/ip-address/{ipAddress}'
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



        if ('ipAddress' in params):
            replacement = str(self.apiClient.toPathValue(params['ipAddress']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'ipAddress' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'DeviceIfListResult')
        return responseObject




    def getInterfaceByIsis(self, **kwargs):
        """Retrieves ISIS interfaces

        Args:

            scope, str: Authorization Scope for RBAC (required)



        Returns: DeviceIfListResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getInterfaceByIsis" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/interface/isis'
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

        responseObject = self.apiClient.deserialize(response, 'DeviceIfListResult')
        return responseObject




    def getInterfaceByDeviceId(self, **kwargs):
        """Retrieves device interfaces

        Args:

            deviceId, str: Device ID (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: DeviceIfListResult
        """

        allParams = ['deviceId', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getInterfaceByDeviceId" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/interface/network-device/{deviceId}'
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



        if ('deviceId' in params):
            replacement = str(self.apiClient.toPathValue(params['deviceId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'deviceId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'DeviceIfListResult')
        return responseObject




    def getInterfaceByDeviceIdAndName(self, **kwargs):
        """Retrieves interface for the given device and interface name

        Args:

            deviceId, str: Device ID (required)


            name, str: Interface name (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: DeviceIfResult
        """

        allParams = ['deviceId', 'name', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getInterfaceByDeviceIdAndName" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/interface/network-device/{deviceId}/interface-name'
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



        if ('scope' in params):
            headerParams['scope'] = params['scope']



        if ('deviceId' in params):
            replacement = str(self.apiClient.toPathValue(params['deviceId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'deviceId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'DeviceIfResult')
        return responseObject




    def getInterfaceRangeByDevice(self, **kwargs):
        """Retrieves interface range for the device

        Args:

            deviceId, str: Device ID (required)


            startIndex, int: Start index (required)


            recordsToReturn, int: Number of records to return (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: DeviceIfListResult
        """

        allParams = ['deviceId', 'startIndex', 'recordsToReturn', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getInterfaceRangeByDevice" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/interface/network-device/{deviceId}/{startIndex}/{recordsToReturn}'
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



        if ('deviceId' in params):
            replacement = str(self.apiClient.toPathValue(params['deviceId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'deviceId' + '}',
                                                replacement)

        if ('startIndex' in params):
            replacement = str(self.apiClient.toPathValue(params['startIndex']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'startIndex' + '}',
                                                replacement)

        if ('recordsToReturn' in params):
            replacement = str(self.apiClient.toPathValue(params['recordsToReturn']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'recordsToReturn' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'DeviceIfListResult')
        return responseObject




    def getInterfaceCountByDevice(self, **kwargs):
        """Retrieves device interface count

        Args:

            networkDeviceId, str: Device ID (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: CountResult
        """

        allParams = ['networkDeviceId', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getInterfaceCountByDevice" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/interface/network-device/{networkDeviceId}/count'
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



        if ('networkDeviceId' in params):
            replacement = str(self.apiClient.toPathValue(params['networkDeviceId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'networkDeviceId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'CountResult')
        return responseObject




    def getInterfaceByOspf(self, **kwargs):
        """Retrieves OSPF interfaces

        Args:

            scope, str: Authorization Scope for RBAC (required)



        Returns: DeviceIfListResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getInterfaceByOspf" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/interface/ospf'
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

        responseObject = self.apiClient.deserialize(response, 'DeviceIfListResult')
        return responseObject




    def getInterfaceById(self, **kwargs):
        """Retrieves interface by ID

        Args:

            id, str: Interface ID (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: DeviceIfResult
        """

        allParams = ['id', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getInterfaceById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/interface/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'DeviceIfResult')
        return responseObject




    def getInterfaceByTag(self, **kwargs):
        """Retrieves interfaces by tag

        Args:

            tagId, str: Tag ID (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: InterfaceNIOListResult
        """

        allParams = ['tagId', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getInterfaceByTag" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/tag/{tagId}/interface'
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



        if ('tagId' in params):
            replacement = str(self.apiClient.toPathValue(params['tagId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'tagId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'InterfaceNIOListResult')
        return responseObject




    def getInterfaceCountByTagId(self, **kwargs):
        """Retrieves interface count by tag

        Args:

            tagId, str: Tag ID (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: CountResult
        """

        allParams = ['tagId', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getInterfaceCountByTagId" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/tag/{tagId}/interface/count'
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



        if ('tagId' in params):
            replacement = str(self.apiClient.toPathValue(params['tagId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'tagId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'CountResult')
        return responseObject






