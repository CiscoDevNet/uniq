#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class IwanuserinputApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getAllUserInputs(self, **kwargs):
        """getAllUserInputs

        Args:
            
            userId, str: User Id (required)
            
            
            inputIdPattern, str: Input Id Pattern (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: IwanUserInputDTOListResult
        """

        allParams = ['userId', 'inputIdPattern', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAllUserInputs" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/user-input'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('userId' in params):
            queryParams['userId'] = self.apiClient.toPathValue(params['userId'])
        
        if ('inputIdPattern' in params):
            queryParams['inputIdPattern'] = self.apiClient.toPathValue(params['inputIdPattern'])
        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'IwanUserInputDTOListResult')
        return responseObject
        
        
        
    
    def updateUserInput(self, **kwargs):
        """updateUserInput

        Args:
            
            userInputDTO, IwanUserInputDTO: userInputDTO (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['userInputDTO', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateUserInput" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/user-input'
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
        

        

        

        
        if ('userInputDTO' in params):
            bodyParam = params['userInputDTO']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def addUserInput(self, **kwargs):
        """addUserInput

        Args:
            
            userInputDTO, IwanUserInputDTO: userInputDTO (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['userInputDTO', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addUserInput" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/user-input'
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
        

        

        

        
        if ('userInputDTO' in params):
            bodyParam = params['userInputDTO']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def deleteAllUserInputs(self, **kwargs):
        """deleteAllUserInputs

        Args:
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteAllUserInputs" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/user-input'
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
        
        
        
    
    def getUserInputs(self, **kwargs):
        """getUserInputs

        Args:
            
            id, str: id (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: object
        """

        allParams = ['id', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getUserInputs" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/user-input/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'object')
        return responseObject
        
        
        
    
    def deleteUserInput(self, **kwargs):
        """deleteUserInput

        Args:
            
            id, str: id (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['id', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteUserInput" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/user-input/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    


