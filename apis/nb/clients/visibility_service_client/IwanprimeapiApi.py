#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class IwanprimeapiApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def primeGet(self, **kwargs):
        """Pass through API to Prime - GET

        Args:
            
            primeUrl, str: primeUrl (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: str
        """

        allParams = ['primeUrl', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method primeGet" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/prime-api'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('primeUrl' in params):
            queryParams['primeUrl'] = self.apiClient.toPathValue(params['primeUrl'])
        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        
        if ('username' in params):
            headerParams['username'] = params['username']
        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    
    def primePut(self, **kwargs):
        """Pass through API to Prime - PUT

        Args:
            
            primeUrl, str: primeUrl (required)
            
            
            jsonStr, : jsonStr (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['primeUrl', 'jsonStr', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method primePut" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/prime-api'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('primeUrl' in params):
            queryParams['primeUrl'] = self.apiClient.toPathValue(params['primeUrl'])
        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        
        if ('username' in params):
            headerParams['username'] = params['username']
        

        

        

        
        if ('jsonStr' in params):
            bodyParam = params['jsonStr']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def primePost(self, **kwargs):
        """Pass through API to Prime - POST

        Args:
            
            primeUrl, str: primeUrl (required)
            
            
            jsonStr, : jsonStr (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: str
        """

        allParams = ['primeUrl', 'jsonStr', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method primePost" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/prime-api'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('primeUrl' in params):
            queryParams['primeUrl'] = self.apiClient.toPathValue(params['primeUrl'])
        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        
        if ('username' in params):
            headerParams['username'] = params['username']
        

        

        

        
        if ('jsonStr' in params):
            bodyParam = params['jsonStr']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    
    def primeDelete(self, **kwargs):
        """Pass through API to Prime - DELETE

        Args:
            
            primeUrl, str: primeUrl (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['primeUrl', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method primeDelete" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/prime-api'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('primeUrl' in params):
            queryParams['primeUrl'] = self.apiClient.toPathValue(params['primeUrl'])
        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        
        if ('username' in params):
            headerParams['username'] = params['username']
        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    


