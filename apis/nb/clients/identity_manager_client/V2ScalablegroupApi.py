#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class V2ScalablegroupApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getScalableGroupByFilters(self, **kwargs):
        """Retrieves scalable group based on a given filter

        Args:
            
            name, str: Retrieve policies for a given name (required)
            
            
            offset, str: Starting index of the resources (1 based) (required)
            
            
            limit, str: Number of resources to return (required)
            
            
        
        Returns: ScalableGroupListResult
        """

        allParams = ['name', 'offset', 'limit']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getScalableGroupByFilters" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v2/scalable-group'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('name' in params):
            queryParams['name'] = self.apiClient.toPathValue(params['name'])
        
        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])
        
        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])
        

        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ScalableGroupListResult')
        return responseObject
        
        
        
    
    def updateScalableGroups(self, **kwargs):
        """Updates existing scalable group.

        Args:
            
            scalableGroupDtos, list[ScalableGroupDTO]: scalableGroupDtos (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['scalableGroupDtos']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateScalableGroups" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v2/scalable-group'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('scalableGroupDtos' in params):
            bodyParam = params['scalableGroupDtos']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def addScalableGroups(self, **kwargs):
        """Creates scalable group inheriting properties from an existing scalable group.

        Args:
            
            scalableGroupDtos, list[ScalableGroupDTO]: scalableGroupDtos (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['scalableGroupDtos']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addScalableGroups" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v2/scalable-group'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('scalableGroupDtos' in params):
            bodyParam = params['scalableGroupDtos']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getCount(self, **kwargs):
        """getCount

        Args:
            
        
        Returns: CountResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v2/scalable-group/count'
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

        responseObject = self.apiClient.deserialize(response, 'CountResult')
        return responseObject
        
        
        
    
    def getEndPointGroupbyId(self, **kwargs):
        """List scalable group based on id

        Args:
            
            id, str: id (required)
            
            
        
        Returns: ScalableGroupResult
        """

        allParams = ['id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getEndPointGroupbyId" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v2/scalable-group/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'ScalableGroupResult')
        return responseObject
        
        
        
    
    def deleteScalableGroup(self, **kwargs):
        """Delete a scalable group by its id.

        Args:
            
            id, str: id (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteScalableGroup" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v2/scalable-group/{id}'
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
        
        
        
    
    def getUserByScalableGroupId(self, **kwargs):
        """List scalable group based on id

        Args:
            
            id, str: id (required)
            
            
        
        Returns: ApicEmUserListResult
        """

        allParams = ['id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getUserByScalableGroupId" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/v2/scalable-group/{id}/users'
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

        responseObject = self.apiClient.deserialize(response, 'ApicEmUserListResult')
        return responseObject
        
        
        
    


