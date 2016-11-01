#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class AaaserverApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getServers(self, **kwargs):
        """getAAAServers

        Args:
            
        
        Returns: AAAServerListResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getServers" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/aaa-server'
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

        responseObject = self.apiClient.deserialize(response, 'AAAServerListResult')
        return responseObject
        
        
        
    
    def updateServers(self, **kwargs):
        """updateAAAServers

        Args:
            
            aaaServerList, list[AAAServer]: aaaServerList (required)
            
            
        
        Returns: SuccessResult
        """

        allParams = ['aaaServerList']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateServers" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/aaa-server'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('aaaServerList' in params):
            bodyParam = params['aaaServerList']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SuccessResult')
        return responseObject
        
        
        
    
    def addAAAServer(self, **kwargs):
        """addAAAServer

        Args:
            
            aaaServerList, list[AAAServer]: aaaServerList (required)
            
            
        
        Returns: ServerIdListResult
        """

        allParams = ['aaaServerList']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addAAAServer" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/aaa-server'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('aaaServerList' in params):
            bodyParam = params['aaaServerList']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ServerIdListResult')
        return responseObject
        
        
        
    
    def getAAAAttribute(self, **kwargs):
        """getAAAAttribute

        Args:
            
        
        Returns: AAAAttributeResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAAAAttribute" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/aaa-server/authorization-attribute'
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

        responseObject = self.apiClient.deserialize(response, 'AAAAttributeResult')
        return responseObject
        
        
        
    
    def addAAAAttribute(self, **kwargs):
        """addAAAAttribute

        Args:
            
            aaaAttribute, AAAAttribute: aaaAttribute (required)
            
            
        
        Returns: SuccessResult
        """

        allParams = ['aaaAttribute']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addAAAAttribute" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/aaa-server/authorization-attribute'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('aaaAttribute' in params):
            bodyParam = params['aaaAttribute']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SuccessResult')
        return responseObject
        
        
        
    
    def deleteAAAAttribute(self, **kwargs):
        """deleteAAAAttribute

        Args:
            
        
        Returns: SuccessResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteAAAAttribute" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/aaa-server/authorization-attribute'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

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

        responseObject = self.apiClient.deserialize(response, 'SuccessResult')
        return responseObject
        
        
        
    
    def getServer(self, **kwargs):
        """getAAAServer

        Args:
            
            serverId, str: serverId (required)
            
            
        
        Returns: AAAServerResult
        """

        allParams = ['serverId']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getServer" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/aaa-server/{serverId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        
        if ('serverId' in params):
            replacement = str(self.apiClient.toPathValue(params['serverId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'serverId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'AAAServerResult')
        return responseObject
        
        
        
    
    def deleteServer(self, **kwargs):
        """deleteAAAServer

        Args:
            
            serverId, str: serverId (required)
            
            
        
        Returns: SuccessResult
        """

        allParams = ['serverId']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteServer" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/aaa-server/{serverId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        
        if ('serverId' in params):
            replacement = str(self.apiClient.toPathValue(params['serverId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'serverId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SuccessResult')
        return responseObject
        
        
        
    


