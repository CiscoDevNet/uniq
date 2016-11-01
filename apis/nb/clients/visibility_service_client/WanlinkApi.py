#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class WanlinkApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def create(self, **kwargs):
        """Create a link between a device and a cloud provider

        Args:
            
            wanLinkDTOs, list[WanLinkDTO]: wanLinkDTOs (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['wanLinkDTOs', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method create" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/wan-link'
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
        

        

        

        
        if ('wanLinkDTOs' in params):
            bodyParam = params['wanLinkDTOs']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def updateQosQueueBandwidth(self, **kwargs):
        """Update the queue bandwidth allocation of a wan interface

        Args:
            
            bandwidthInfo, IWanQosInterfaceBandwidthInfo: bandwidthInfo (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['bandwidthInfo', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateQosQueueBandwidth" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/wan-link/queue-bandwidth'
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
        
        if ('username' in params):
            headerParams['username'] = params['username']
        

        

        

        
        if ('bandwidthInfo' in params):
            bodyParam = params['bandwidthInfo']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def get(self, **kwargs):
        """Get a link between a device and a cloud provider

        Args:
            
            linkId, str: wanLinkUuid (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: WanLinkDTO
        """

        allParams = ['linkId', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/wan-link/{linkId}'
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
        

        
        if ('linkId' in params):
            replacement = str(self.apiClient.toPathValue(params['linkId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'linkId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'WanLinkDTO')
        return responseObject
        
        
        
    
    def delete(self, **kwargs):
        """API to delete a link between a device and a cloud provider

        Args:
            
            linkId, str: wanLinkUuid (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['linkId', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method delete" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/wan-link/{linkId}'
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
        

        
        if ('linkId' in params):
            replacement = str(self.apiClient.toPathValue(params['linkId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'linkId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getQueueBandwidth(self, **kwargs):
        """Get the queue bandwidth allocation of a wan interface

        Args:
            
            linkId, str: wanLinkUuid (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: StdResult«IWanQosInterfaceBandwidthInfo»
        """

        allParams = ['linkId', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getQueueBandwidth" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/wan-link/{linkId}/queue-bandwidth'
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
        

        
        if ('linkId' in params):
            replacement = str(self.apiClient.toPathValue(params['linkId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'linkId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'StdResult«IWanQosInterfaceBandwidthInfo»')
        return responseObject
        
        
        
    
    def scheduleCreate(self, **kwargs):
        """Schedule the creation of a link between a device and a cloud provider

        Args:
            
            wanLinkDTOs, list[WanLinkDTO]: wanLinkDTOs (required)
            
            
            scheduleTime, long: Schedule Time (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['wanLinkDTOs', 'scheduleTime', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method scheduleCreate" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/wan-link/{scheduleTime}'
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
        

        
        if ('scheduleTime' in params):
            replacement = str(self.apiClient.toPathValue(params['scheduleTime']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'scheduleTime' + '}',
                                                replacement)
        

        

        
        if ('wanLinkDTOs' in params):
            bodyParam = params['wanLinkDTOs']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    


