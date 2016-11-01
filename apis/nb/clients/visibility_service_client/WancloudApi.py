#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class WancloudApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getWanClouds(self, **kwargs):
        """API to get WAN clouds

        Args:
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: WanCloudListResult
        """

        allParams = ['scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getWanClouds" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/wan-cloud'
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
        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'WanCloudListResult')
        return responseObject
        
        
        
    
    def addWanCloud(self, **kwargs):
        """API to Provision WAN Cloud - API to save and apply the WAN Cloud configuration

        Args:
            
            wanClouds, list[WanCloudDTO]: wanClouds (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['wanClouds', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addWanCloud" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/wan-cloud'
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
        

        

        

        
        if ('wanClouds' in params):
            bodyParam = params['wanClouds']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getWanCloudByUuid(self, **kwargs):
        """API to get the WAN cloud based on WAN cloud ID

        Args:
            
            wanCloudId, str: wanCloudId (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: WanCloudResult
        """

        allParams = ['wanCloudId', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getWanCloudByUuid" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/wan-cloud/{wanCloudId}'
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
        

        
        if ('wanCloudId' in params):
            replacement = str(self.apiClient.toPathValue(params['wanCloudId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'wanCloudId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'WanCloudResult')
        return responseObject
        
        
        
    


