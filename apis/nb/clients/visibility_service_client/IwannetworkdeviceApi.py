#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class IwannetworkdeviceApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def create(self, **kwargs):
        """API to create/associate device to the site 

        Args:
            
            deviceDto, list[SiteDeviceDTO]: deviceDto (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['deviceDto', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method create" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/network-device'
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
        
        if ('username' in params):
            headerParams['username'] = params['username']
        

        

        

        
        if ('deviceDto' in params):
            bodyParam = params['deviceDto']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getUnclaimedDevice(self, **kwargs):
        """API to get list of unclaimed IWAN Devices  

        Args:
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            state, str: State of device UNCLAIMED (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: SiteDeviceListResult
        """

        allParams = ['scope', 'state', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getUnclaimedDevice" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/network-device/'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('state' in params):
            queryParams['state'] = self.apiClient.toPathValue(params['state'])
        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        
        if ('username' in params):
            headerParams['username'] = params['username']
        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SiteDeviceListResult')
        return responseObject
        
        
        
    
    def validateDeviceForBrownfieldConfiguration(self, **kwargs):
        """Validate a device brownfield configuration

        Args:
            
            ipAddress, str: ipAddress (required)
            
            
            isExternalMasterController, str: isExternalMasterController (required)
            
            
            siteType, str: siteType (required)
            
            
            lanInterface, str: lanInterface (required)
            
            
            wanInterface, str: wanInterface (required)
            
            
            username, str: requestorUsername (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['ipAddress', 'isExternalMasterController', 'siteType', 'lanInterface', 'wanInterface', 'username', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method validateDeviceForBrownfieldConfiguration" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/network-device/validate/{ipAddress}/{isExternalMasterController}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('siteType' in params):
            queryParams['siteType'] = self.apiClient.toPathValue(params['siteType'])
        
        if ('lanInterface' in params):
            queryParams['lanInterface'] = self.apiClient.toPathValue(params['lanInterface'])
        
        if ('wanInterface' in params):
            queryParams['wanInterface'] = self.apiClient.toPathValue(params['wanInterface'])
        

        
        if ('username' in params):
            headerParams['username'] = params['username']
        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        
        if ('ipAddress' in params):
            replacement = str(self.apiClient.toPathValue(params['ipAddress']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'ipAddress' + '}',
                                                replacement)
        
        if ('isExternalMasterController' in params):
            replacement = str(self.apiClient.toPathValue(params['isExternalMasterController']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'isExternalMasterController' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getDeviceWanLinks(self, **kwargs):
        """Get the wan links connected to a specific device

        Args:
            
            deviceId, str: deviceUuid (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: WanLinkDTOListResult
        """

        allParams = ['deviceId', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getDeviceWanLinks" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/network-device/{deviceId}/wan-link'
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
        
        if ('username' in params):
            headerParams['username'] = params['username']
        

        
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

        responseObject = self.apiClient.deserialize(response, 'WanLinkDTOListResult')
        return responseObject
        
        
        
    
    def getDevice(self, **kwargs):
        """API to get the Device based on device instance UUID  

        Args:
            
            deviceInstanceUuid, str: deviceInstanceUuid (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: SiteDeviceResult
        """

        allParams = ['deviceInstanceUuid', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getDevice" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/network-device/{deviceInstanceUuid}'
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
        
        if ('username' in params):
            headerParams['username'] = params['username']
        

        
        if ('deviceInstanceUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['deviceInstanceUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'deviceInstanceUuid' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SiteDeviceResult')
        return responseObject
        
        
        
    
    def delete(self, **kwargs):
        """API to delete the device in the site 

        Args:
            
            deviceInstanceUuid, str: deviceInstanceUuid (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['deviceInstanceUuid', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method delete" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/network-device/{deviceInstanceUuid}'
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
        
        if ('username' in params):
            headerParams['username'] = params['username']
        

        
        if ('deviceInstanceUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['deviceInstanceUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'deviceInstanceUuid' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    


