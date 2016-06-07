#!/usr/bin/env python
#pylint: skip-file
"""
ReachabilityinfoApi.py
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


class ReachabilityinfoApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient



    def getAllNetworkDevicesReachabilityInfo(self, **kwargs):
        """getAllNetworkDevicesReachabilityInfo

        Args:

            scope, str: Authorization Scope for RBAC (required)



        Returns: NetworkDeviceReachabilityInfoNIOListResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAllNetworkDevicesReachabilityInfo" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/reachability-info'
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

        responseObject = self.apiClient.deserialize(response, 'NetworkDeviceReachabilityInfoNIOListResult')
        return responseObject




    def updateNetworkReachabilityInfoById(self, **kwargs):
        """updateNetworkReachabilityInfoById

        Args:

            networkDeviceReachabilityInfoNIO, NetworkDeviceReachabilityInfoNIO: networkDeviceReachabilityInfoNIO (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['networkDeviceReachabilityInfoNIO', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateNetworkReachabilityInfoById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/reachability-info'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']







        if ('networkDeviceReachabilityInfoNIO' in params):
            bodyParam = params['networkDeviceReachabilityInfoNIO']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def addNetworkDeviceReachabilityInfo(self, **kwargs):
        """addNetworkDeviceReachabilityInfo

        Args:

            networkDeviceReachabilityInfoNIO, NetworkDeviceReachabilityInfoNIO: networkDeviceReachabilityInfoNIO (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['networkDeviceReachabilityInfoNIO', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addNetworkDeviceReachabilityInfo" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/reachability-info'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = ''
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']







        if ('networkDeviceReachabilityInfoNIO' in params):
            bodyParam = params['networkDeviceReachabilityInfoNIO']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def deleteAllNetworkReachabilityInfo(self, **kwargs):
        """deleteAllNetworkReachabilityInfo

        Args:

            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteAllNetworkReachabilityInfo" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/reachability-info'
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








        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getNetworkDevicesReachabilityInfoCount(self, **kwargs):
        """getNetworkDevicesReachabilityInfoCount

        Args:

            scope, str: Authorization Scope for RBAC (required)



        Returns: CountResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getNetworkDevicesReachabilityInfoCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/reachability-info/count'
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




    def getNetworkReachabilityInfoByIpaddress(self, **kwargs):
        """getNetworkReachabilityInfoByIpaddress

        Args:

            ipAddress, str: ipAddress (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: NetworkDeviceReachabilityInfoNIOResult
        """

        allParams = ['ipAddress', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getNetworkReachabilityInfoByIpaddress" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/reachability-info/ip-address/{ipAddress}'
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

        responseObject = self.apiClient.deserialize(response, 'NetworkDeviceReachabilityInfoNIOResult')
        return responseObject




    def getNetworkReachabilityInfoById(self, **kwargs):
        """getNetworkReachabilityInfoById

        Args:

            networkDeviceId, str: networkDeviceId (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: NetworkDeviceReachabilityInfoNIOResult
        """

        allParams = ['networkDeviceId', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getNetworkReachabilityInfoById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/reachability-info/{networkDeviceId}'
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

        responseObject = self.apiClient.deserialize(response, 'NetworkDeviceReachabilityInfoNIOResult')
        return responseObject




    def deleteNetworkReachabilityInfoById(self, **kwargs):
        """deleteNetworkReachabilityInfoById

        Args:

            networkDeviceId, str: networkDeviceId (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['networkDeviceId', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteNetworkReachabilityInfoById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/reachability-info/{networkDeviceId}'
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

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getNetworkDeviceReachabilityInfoByRange(self, **kwargs):
        """getNetworkDeviceReachabilityInfoByRange

        Args:

            startIndex, int: startIndex (required)


            recordsToReturn, int: recordsToReturn (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: NetworkDeviceReachabilityInfoNIOListResult
        """

        allParams = ['startIndex', 'recordsToReturn', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getNetworkDeviceReachabilityInfoByRange" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/reachability-info/{startIndex}/{recordsToReturn}'
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

        responseObject = self.apiClient.deserialize(response, 'NetworkDeviceReachabilityInfoNIOListResult')
        return responseObject






