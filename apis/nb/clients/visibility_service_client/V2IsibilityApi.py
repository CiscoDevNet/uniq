#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class V2IsibilityApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getApplicationCommonlyUsedLevel(self, **kwargs):
        """getApplicationCommonlyUsedLevel

        Args:
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: IwanApplicationCommonlyUsedLevel
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getApplicationCommonlyUsedLevel" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/visibility/application/commonly-used-level'
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

        responseObject = self.apiClient.deserialize(response, 'IwanApplicationCommonlyUsedLevel')
        return responseObject
        
        
        
    
    def getPhysicalServiceProviderList(self, **kwargs):
        """getPhysicalServiceProviderList

        Args:
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: IwanPhysicalServiceProviderListResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPhysicalServiceProviderList" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/visibility/iwan-physical-service-provider'
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

        responseObject = self.apiClient.deserialize(response, 'IwanPhysicalServiceProviderListResult')
        return responseObject
        
        
        
    
    def createPhysicalServiceProvider(self, **kwargs):
        """createPhysicalServiceProvider

        Args:
            
            psp, IwanPhysicalServiceProviderDTO: psp (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['psp', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createPhysicalServiceProvider" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/visibility/iwan-physical-service-provider'
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
        

        

        

        
        if ('psp' in params):
            bodyParam = params['psp']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    


