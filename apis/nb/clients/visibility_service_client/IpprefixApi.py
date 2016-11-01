#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class IpprefixApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getAllPrefixes(self, **kwargs):
        """Get list of ip-prefixes (Pagination)

        Args:
            
            limit, str: limit (required)
            
            
            offset, str: offset (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: DCPrefixDTOListResult
        """

        allParams = ['limit', 'offset', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAllPrefixes" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ip-prefix'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])
        
        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])
        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        
        if ('username' in params):
            headerParams['username'] = params['username']
        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'DCPrefixDTOListResult')
        return responseObject
        
        
        
    
    def update(self, **kwargs):
        """Updates prefix(s) in site

        Args:
            
            dcPrefixDtos, list[DCPrefixDTO]: Prefix Object (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['dcPrefixDtos', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method update" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ip-prefix'
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
        

        

        

        
        if ('dcPrefixDtos' in params):
            bodyParam = params['dcPrefixDtos']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def create(self, **kwargs):
        """Creates ip-prefix(s) in site

        Args:
            
            dcPrefixDtos, list[DCPrefixDTO]: Prefix Object (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['dcPrefixDtos', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method create" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ip-prefix'
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
        

        

        

        
        if ('dcPrefixDtos' in params):
            bodyParam = params['dcPrefixDtos']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def delete(self, **kwargs):
        """Deletes ip-prefix(s) by id

        Args:
            
            ids, List: Prefix Object (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['ids', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method delete" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ip-prefix'
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
        

        

        

        
        if ('ids' in params):
            bodyParam = params['ids']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getPrefixById(self, **kwargs):
        """Get an ip-prefix by id

        Args:
            
            prefixId, str: prefixUuid (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: DCPrefixDTOResult
        """

        allParams = ['prefixId', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPrefixById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ip-prefix/{prefixId}'
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
        

        
        if ('prefixId' in params):
            replacement = str(self.apiClient.toPathValue(params['prefixId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'prefixId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'DCPrefixDTOResult')
        return responseObject
        
        
        
    
    def scheduleUpdate(self, **kwargs):
        """Schedule update of list of prefix(s) in site

        Args:
            
            dcPrefixDtos, list[DCPrefixDTO]: Prefix Object (required)
            
            
            scheduleTime, long: Schedule Time (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['dcPrefixDtos', 'scheduleTime', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method scheduleUpdate" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ip-prefix/{scheduleTime}'
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
        

        
        if ('scheduleTime' in params):
            replacement = str(self.apiClient.toPathValue(params['scheduleTime']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'scheduleTime' + '}',
                                                replacement)
        

        

        
        if ('dcPrefixDtos' in params):
            bodyParam = params['dcPrefixDtos']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def scheduleCreate(self, **kwargs):
        """Schedule Creation of ip-prefix(s) in site

        Args:
            
            dcPrefixDtos, list[DCPrefixDTO]: Prefix Object (required)
            
            
            scheduleTime, long: Schedule Time (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['dcPrefixDtos', 'scheduleTime', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method scheduleCreate" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ip-prefix/{scheduleTime}'
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
        

        

        
        if ('dcPrefixDtos' in params):
            bodyParam = params['dcPrefixDtos']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def scheduleDelete(self, **kwargs):
        """Schedule deletion of ip-prefix(s) by id

        Args:
            
            ids, List: Prefix Object (required)
            
            
            scheduleTime, long: Schedule Time (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['ids', 'scheduleTime', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method scheduleDelete" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ip-prefix/{scheduleTime}'
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
        

        
        if ('scheduleTime' in params):
            replacement = str(self.apiClient.toPathValue(params['scheduleTime']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'scheduleTime' + '}',
                                                replacement)
        

        

        
        if ('ids' in params):
            bodyParam = params['ids']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    


