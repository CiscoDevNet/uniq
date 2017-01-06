#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class TemplaterendererApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getAllPnpTemplateRenderer(self, **kwargs):
        """Retrieves all the active rendered template in cache

        Args:
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: ZtdTemplateRendererResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAllPnpTemplateRenderer" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/template-renderer'
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

        responseObject = self.apiClient.deserialize(response, 'ZtdTemplateRendererResult')
        return responseObject
        
        
        
    
    def createPnpTemplateRenderer(self, **kwargs):
        """Renderer for pnp template

        Args:
            
            templaterenderer, list[ZtdTemplateRenderer]: fileId and configProperty is mandatory (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['templaterenderer', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createPnpTemplateRenderer" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/template-renderer'
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
        

        

        

        
        if ('templaterenderer' in params):
            bodyParam = params['templaterenderer']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getPnpTemplateRendererById(self, **kwargs):
        """Retrieves a rendered template

        Args:
            
            templateRendererId, str: Template Renderer ID is mandatory (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: ZtdTemplateRendererResult
        """

        allParams = ['templateRendererId', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPnpTemplateRendererById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/template-renderer/{templateRendererId}'
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
        

        
        if ('templateRendererId' in params):
            replacement = str(self.apiClient.toPathValue(params['templateRendererId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'templateRendererId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ZtdTemplateRendererResult')
        return responseObject
        
        
        
    


