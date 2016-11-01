#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class ServiceproviderprofileApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getServiceProviderProfilesByFilters(self, **kwargs):
        """Retrieves ServiceProviderProfiles based on a given filter

        Args:
            
            name, str: Retrieve ServiceProviderProfile for a given name (required)
            
            
            defaultModel, str: Retrieve Default(&#39;true&#39;) or Custom(&#39;false&#39;) ServiceProviderProfiles (required)
            
            
            interfaces.stale, str: Retrieve ServiceProviderProfiles which have stale interfaces - only valid value is &#39;true&#39; (required)
            
            
            interfaces.policyScope, str: Retrieve ServiceProviderProfiles which have stale interfaces within the policyScope (required)
            
            
            offset, str: Starting index of the resources (1 based) (required)
            
            
            limit, str: Number of resources to return (required)
            
            
        
        Returns: ServiceProviderProfileListResult
        """

        allParams = ['name', 'defaultModel', 'interfaces.stale', 'interfaces.policyScope', 'offset', 'limit']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getServiceProviderProfilesByFilters" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/service-provider-profile'
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
        
        if ('defaultModel' in params):
            queryParams['defaultModel'] = self.apiClient.toPathValue(params['defaultModel'])
        
        if ('interfaces.stale' in params):
            queryParams['interfaces.stale'] = self.apiClient.toPathValue(params['interfaces.stale'])
        
        if ('interfaces.policyScope' in params):
            queryParams['interfaces.policyScope'] = self.apiClient.toPathValue(params['interfaces.policyScope'])
        
        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])
        
        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])
        

        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ServiceProviderProfileListResult')
        return responseObject
        
        
        
    
    def update(self, **kwargs):
        """Update ServiceProviderProfiles(s)

        Args:
            
            serviceProviderProfileDTOs, list[ServiceProviderProfileDTO]: ServiceProviderProfile Object(s) (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['serviceProviderProfileDTOs']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method update" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/service-provider-profile'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('serviceProviderProfileDTOs' in params):
            bodyParam = params['serviceProviderProfileDTOs']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def add(self, **kwargs):
        """Create ServiceProviderProfiles(s)

        Args:
            
            serviceProviderProfileDTOs, list[ServiceProviderProfileDTO]: ServiceProviderProfile Object(s) (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['serviceProviderProfileDTOs']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method add" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/service-provider-profile'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('serviceProviderProfileDTOs' in params):
            bodyParam = params['serviceProviderProfileDTOs']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getCount(self, **kwargs):
        """Return total count of ServiceProviderProfile

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

        resourcePath = '/service-provider-profile/count'
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
        
        
        
    
    def getById(self, **kwargs):
        """Retrieves a ServiceProviderProfile based on its id

        Args:
            
            id, str: id (required)
            
            
        
        Returns: ServiceProviderProfileResult
        """

        allParams = ['id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/service-provider-profile/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'ServiceProviderProfileResult')
        return responseObject
        
        
        
    
    def delete(self, **kwargs):
        """Deletes a ServiceProviderProfile by its id

        Args:
            
            id, str: id (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method delete" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/service-provider-profile/{id}'
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
        
        
        
    


