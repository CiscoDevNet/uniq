#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class TaskApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getTaskByOperationId(self, **kwargs):
        """getTaskByOperationId

        Args:
            
            operationId, str: operationId (required)
            
            
            offset, int: Index, minimum value is 0 (required)
            
            
            limit, int: The maximum value of {limit} supported is 500. &lt;br/&gt; Base 1 indexing for {limit}, minimum value is 1 (required)
            
            
        
        Returns: TaskDTOListResponse
        """

        allParams = ['operationId', 'offset', 'limit']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getTaskByOperationId" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/task/operation/{operationId}/{offset}/{limit}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        
        if ('operationId' in params):
            replacement = str(self.apiClient.toPathValue(params['operationId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'operationId' + '}',
                                                replacement)
        
        if ('offset' in params):
            replacement = str(self.apiClient.toPathValue(params['offset']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'offset' + '}',
                                                replacement)
        
        if ('limit' in params):
            replacement = str(self.apiClient.toPathValue(params['limit']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'limit' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskDTOListResponse')
        return responseObject
        
        
        
    
    def getTaskByRange(self, **kwargs):
        """getTaskByRange

        Args:
            
            offset, int: Index, minimum value is 0 (required)
            
            
            limit, int: The maximum value of {limit} supported is 500. &lt;br/&gt; Base 1 indexing for {limit}, minimum value is 1 (required)
            
            
        
        Returns: TaskDTOListResponse
        """

        allParams = ['offset', 'limit']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getTaskByRange" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/task/{offset}/{limit}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        
        if ('offset' in params):
            replacement = str(self.apiClient.toPathValue(params['offset']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'offset' + '}',
                                                replacement)
        
        if ('limit' in params):
            replacement = str(self.apiClient.toPathValue(params['limit']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'limit' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskDTOListResponse')
        return responseObject
        
        
        
    
    def getTask(self, **kwargs):
        """getTruststoreFileCount

        Args:
            
            taskId, str: UUID of the Task (required)
            
            
        
        Returns: TaskDTOResponse
        """

        allParams = ['taskId']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getTask" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/task/{taskId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        
        if ('taskId' in params):
            replacement = str(self.apiClient.toPathValue(params['taskId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'taskId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskDTOResponse')
        return responseObject
        
        
        
    
    def getTaskTree(self, **kwargs):
        """Get Task Tree

        Args:
            
            taskId, str: UUID of the Task (required)
            
            
        
        Returns: TaskDTOListResponse
        """

        allParams = ['taskId']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getTaskTree" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/task/{taskId}/tree'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        
        if ('taskId' in params):
            replacement = str(self.apiClient.toPathValue(params['taskId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'taskId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskDTOListResponse')
        return responseObject
        
        
        
    


