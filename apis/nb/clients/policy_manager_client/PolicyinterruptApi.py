#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class PolicyinterruptApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getPolicyInterruptByScope(self, **kwargs):
        """Retrieves the latest interrupt on a policy scope

        Args:
            
            policyScope, str: policyScope (required)
            
            
            scopeWirelessSegment, str: scopeWirelessSegment (required)
            
            
        
        Returns: PolicyInterruptDTOResult
        """

        allParams = ['policyScope', 'scopeWirelessSegment']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPolicyInterruptByScope" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy/interrupt/'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('policyScope' in params):
            queryParams['policyScope'] = self.apiClient.toPathValue(params['policyScope'])
        
        if ('scopeWirelessSegment' in params):
            queryParams['scopeWirelessSegment'] = self.apiClient.toPathValue(params['scopeWirelessSegment'])
        

        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'PolicyInterruptDTOResult')
        return responseObject
        
        
        
    
    def updatePolicyInterrupt(self, **kwargs):
        """Update policy interrupt on a scope. Triggers &#39;abort&#39; and &#39;abort, restore to original&#39; actions

        Args:
            
            policyInterruptInput, PolicyInterruptInput: policyInterruptInput (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['policyInterruptInput']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updatePolicyInterrupt" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy/interrupt/'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('policyInterruptInput' in params):
            bodyParam = params['policyInterruptInput']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    


