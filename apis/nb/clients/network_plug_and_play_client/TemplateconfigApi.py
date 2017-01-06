#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class TemplateconfigApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getPnpTemplateConfig(self, **kwargs):
        """Retrieves a list of template configs

        Args:
            
            offset, int: Starting index of the response. Minimum value is 1 (required)
            
            
            limit, int: Limit the number of responses. Maximum value supported is 500. Minimum value is 1 (required)
            
            
            templateId, str: Id of template (required)
            
            
            configId, str: Id of configuration file (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: ZtdTemplateConfigListResult
        """

        allParams = ['offset', 'limit', 'templateId', 'configId', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPnpTemplateConfig" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/template-config'
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
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])
        
        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])
        
        if ('templateId' in params):
            queryParams['templateId'] = self.apiClient.toPathValue(params['templateId'])
        
        if ('configId' in params):
            queryParams['configId'] = self.apiClient.toPathValue(params['configId'])
        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ZtdTemplateConfigListResult')
        return responseObject
        
        
        
    
    def updatePnpTemplateConfig(self, **kwargs):
        """Updates existing template config

        Args:
            
            templateConfig, list[ZtdTemplateConfig]: PnP template. Template Config ID is mandatory (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['templateConfig', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updatePnpTemplateConfig" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/template-config'
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
        

        

        

        
        if ('templateConfig' in params):
            bodyParam = params['templateConfig']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def createPnpTemplateConfig(self, **kwargs):
        """Creates a new template config

        Args:
            
            templateConfig, list[ZtdTemplateConfig]: PnP template. Template name and template ID are mandatory (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['templateConfig', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createPnpTemplateConfig" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/template-config'
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
        

        

        

        
        if ('templateConfig' in params):
            bodyParam = params['templateConfig']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getPnpTemplateConfigById(self, **kwargs):
        """Retrieves a template config with its ID

        Args:
            
            templateConfigId, str: Template Config ID is mandatory (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: ZtdTemplateConfigResult
        """

        allParams = ['templateConfigId', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPnpTemplateConfigById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/template-config/{templateConfigId}'
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
        

        
        if ('templateConfigId' in params):
            replacement = str(self.apiClient.toPathValue(params['templateConfigId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'templateConfigId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ZtdTemplateConfigResult')
        return responseObject
        
        
        
    
    def deletePnpTemplateConfigId(self, **kwargs):
        """Deletes a template config with its ID

        Args:
            
            templateConfigId, str: Template Config ID is mandatory (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['templateConfigId', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deletePnpTemplateConfigId" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/template-config/{templateConfigId}'
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
        

        
        if ('templateConfigId' in params):
            replacement = str(self.apiClient.toPathValue(params['templateConfigId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'templateConfigId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    


