#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class ReachabilityinfoApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getAllNetworkDevicesReachabilityInfo(self, **kwargs):
        """Retrieves all reachability-info

        Args:
            
        
        Returns: NetworkDeviceReachabilityInfoNIOListResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
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

        

        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'NetworkDeviceReachabilityInfoNIOListResult')
        return responseObject
        
        
        
    
    def getNetworkDevicesReachabilityInfoCount(self, **kwargs):
        """Retrieves reachability-info count

        Args:
            
        
        Returns: CountResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
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

        

        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'CountResult')
        return responseObject
        
        
        
    
    def getNetworkReachabilityInfoByIpaddress(self, **kwargs):
        """Retrieves reachability-info by IP address

        Args:
            
            ipAddress, str: IP address of device (required)
            
            
        
        Returns: NetworkDeviceReachabilityInfoNIOResult
        """

        allParams = ['ipAddress']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
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
        """Retrieves reachability-info by ID

        Args:
            
            networkDeviceId, str: ID of network-device (required)
            
            
        
        Returns: NetworkDeviceReachabilityInfoNIOResult
        """

        allParams = ['networkDeviceId']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
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
        
        
        
    
    def getNetworkDeviceReachabilityInfoByRange(self, **kwargs):
        """Retrieves range of reachability-info

        Args:
            
            startIndex, int: Start index (required)
            
            
            recordsToReturn, int: Number of records to return (required)
            
            
        
        Returns: NetworkDeviceReachabilityInfoNIOListResult
        """

        allParams = ['startIndex', 'recordsToReturn']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
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
        
        
        
    


