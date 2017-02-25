#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class HostApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getHosts(self, **kwargs):
        """Retrieve hosts based on given filters

        Args:
            
            limit, str: limit (required)
            
            
            offset, str: offset (required)
            
            
            sortBy, str: sortBy (required)
            
            
            order, str: order (required)
            
            
            hostName, list[str]: hostName (required)
            
            
            hostMac, list[str]: hostMac (required)
            
            
            hostType, str: Host type : wired or wireless (required)
            
            
            connectedInterfaceName, list[str]: connectedInterfaceName (required)
            
            
            hostIp, list[str]: hostIp (required)
            
            
            connectedNetworkDeviceIpAddress, list[str]: connectedNetworkDeviceIpAddress (required)
            
            
            subType, str: Available values: &#39;UNKNOWN&#39; or &#39;IP_PHONE&#39; or &#39;TELEPRESENCE&#39; or &#39;VIDEO_SURVEILLANCE_IP_CAMERA&#39; or &#39;VIDEO_ENDPOINT&#39;. Only exact match filtering supported on this field (required)
            
            
            filterOperation, str: startswith/contains/endswith (required)
            
            
        
        Returns: HostListResult
        """

        allParams = ['limit', 'offset', 'sortBy', 'order', 'hostName', 'hostMac', 'hostType', 'connectedInterfaceName', 'hostIp', 'connectedNetworkDeviceIpAddress', 'subType', 'filterOperation']

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
        
        if ('connectedNetworkDeviceIpAddress' in params):
            queryParams['connectedNetworkDeviceIpAddress'] = self.apiClient.toPathValue(params['connectedNetworkDeviceIpAddress'])
        
        if ('subType' in params):
            queryParams['subType'] = self.apiClient.toPathValue(params['subType'])
        
        if ('filterOperation' in params):
            queryParams['filterOperation'] = self.apiClient.toPathValue(params['filterOperation'])
        

        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'HostListResult')
        return responseObject
        
        
        
    
    def getHostCount(self, **kwargs):
        """Retrieves the number of hosts

        Args:
            
            hostName, list[str]: hostName (required)
            
            
            hostMac, list[str]: hostMac (required)
            
            
            hostType, str: Host type : wired or wireless (required)
            
            
            connectedInterfaceName, list[str]: connectedInterfaceName (required)
            
            
            hostIp, list[str]: hostIp (required)
            
            
            connectedNetworkDeviceIpAddress, list[str]: connectedNetworkDeviceIpAddress (required)
            
            
            subType, str: Available values: &#39;UNKNOWN&#39; or &#39;IP_PHONE&#39; or &#39;TELEPRESENCE&#39; or &#39;VIDEO_SURVEILLANCE_IP_CAMERA&#39; or &#39;VIDEO_ENDPOINT&#39;. Only exact match filtering supported on this field (required)
            
            
            filterOperation, str: startswith/contains/endswith (required)
            
            
        
        Returns: CountResult
        """

        allParams = ['hostName', 'hostMac', 'hostType', 'connectedInterfaceName', 'hostIp', 'connectedNetworkDeviceIpAddress', 'subType', 'filterOperation']

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
        
        if ('connectedNetworkDeviceIpAddress' in params):
            queryParams['connectedNetworkDeviceIpAddress'] = self.apiClient.toPathValue(params['connectedNetworkDeviceIpAddress'])
        
        if ('subType' in params):
            queryParams['subType'] = self.apiClient.toPathValue(params['subType'])
        
        if ('filterOperation' in params):
            queryParams['filterOperation'] = self.apiClient.toPathValue(params['filterOperation'])
        

        

        

        

        

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
            
            
        
        Returns: HostResult
        """

        allParams = ['id']

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
        
        
        
    


