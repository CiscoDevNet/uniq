#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class NetworkdevicepollercliApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getLegitCliKeywords(self, **kwargs):
        """Get all keywords of CLIs accepted by command runner

        Args:
            
        
        Returns: LegitCliKeyResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getLegitCliKeywords" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device-poller/cli/legit-reads'
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

        responseObject = self.apiClient.deserialize(response, 'LegitCliKeyResult')
        return responseObject
        
        
        
    
    def submitCommands(self, **kwargs):
        """Run read-only commands on devices to get their real-time configuration

        Args:
            
            commandRunnerDto, CommandRunnerDTO: commandRunnerDto (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['commandRunnerDto', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method submitCommands" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device-poller/cli/read-request'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        
        if ('username' in params):
            headerParams['username'] = params['username']
        

        

        

        
        if ('commandRunnerDto' in params):
            bodyParam = params['commandRunnerDto']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    


