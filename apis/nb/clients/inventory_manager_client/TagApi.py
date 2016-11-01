#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class TagApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getTags(self, **kwargs):
        """Get the tags by filters

        Args:
            
            resourceType, str: Type of resource (network-device) (required)
            
            
            resourceId, str: Resource ID (required)
            
            
        
        Returns: TagDtoListResult
        """

        allParams = ['resourceType', 'resourceId']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getTags" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/tag'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('resourceType' in params):
            queryParams['resourceType'] = self.apiClient.toPathValue(params['resourceType'])
        
        if ('resourceId' in params):
            queryParams['resourceId'] = self.apiClient.toPathValue(params['resourceId'])
        

        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TagDtoListResult')
        return responseObject
        
        
        
    
    def updateTag(self, **kwargs):
        """Update tag to a new value

        Args:
            
            tagDto, TagDto: TagDto with the new tag (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['tagDto']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateTag" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/tag'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('tagDto' in params):
            bodyParam = params['tagDto']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def addTag(self, **kwargs):
        """Add a new tag

        Args:
            
            tagDto, TagDto: TagDto with the tag (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['tagDto']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addTag" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/tag'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('tagDto' in params):
            bodyParam = params['tagDto']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def addTagToResource(self, **kwargs):
        """Associate a tag to a resource

        Args:
            
            tagDto, TagDto: TagDto with tag ID, resource ID and resource type (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['tagDto']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addTagToResource" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/tag/association'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('tagDto' in params):
            bodyParam = params['tagDto']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def deleteTagFromResource(self, **kwargs):
        """Delete association of tag from a resource

        Args:
            
            id, str: Tag ID (required)
            
            
            resourceType, str: Type of resource. Supported resourceTypes are network-device, interface. (required)
            
            
            resourceId, str: Resource ID (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['id', 'resourceType', 'resourceId']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteTagFromResource" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/tag/association/{id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('resourceType' in params):
            queryParams['resourceType'] = self.apiClient.toPathValue(params['resourceType'])
        
        if ('resourceId' in params):
            queryParams['resourceId'] = self.apiClient.toPathValue(params['resourceId'])
        

        

        
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
        
        
        
    
    def getTag(self, **kwargs):
        """Retrieves tag by its id

        Args:
            
            id, str: Tag ID (required)
            
            
        
        Returns: TagDtoResult
        """

        allParams = ['id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getTag" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/tag/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'TagDtoResult')
        return responseObject
        
        
        
    
    def deleteTag(self, **kwargs):
        """Delete tag by its id

        Args:
            
            id, str: Tag ID (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteTag" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/tag/{id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

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

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    


