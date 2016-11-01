#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class SharddcacheApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def clearShardOwnerships(self, **kwargs):
        """clearShardOwnerships

        Args:
            
        
        Returns: SuccessResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method clearShardOwnerships" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/shard/dcache/clear-shard-repository'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

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
        
        
        
    
    def getServiceInstances(self, **kwargs):
        """getServiceInstances

        Args:
            
        
        Returns: ServiceInstancesResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getServiceInstances" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/shard/dcache/service-instance'
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

        responseObject = self.apiClient.deserialize(response, 'ServiceInstancesResult')
        return responseObject
        
        
        
    
    def getShardCategoriesRegisteredForServiceInstance(self, **kwargs):
        """getShardCategoriesRegisteredForServiceInstance

        Args:
            
            serviceInstance, str: serviceInstance (required)
            
            
        
        Returns: ShardCategoriesForServiceInstanceResult
        """

        allParams = ['serviceInstance']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getShardCategoriesRegisteredForServiceInstance" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/shard/dcache/service-instance/{serviceInstance}/shard-category'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        
        if ('serviceInstance' in params):
            replacement = str(self.apiClient.toPathValue(params['serviceInstance']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'serviceInstance' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ShardCategoriesForServiceInstanceResult')
        return responseObject
        
        
        
    
    def getShardCategories(self, **kwargs):
        """getShardCategories

        Args:
            
        
        Returns: ShardCategoriesResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getShardCategories" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/shard/dcache/shard-category'
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

        responseObject = self.apiClient.deserialize(response, 'ShardCategoriesResult')
        return responseObject
        
        
        
    
    def getServiceInstancesRegisteredForShardCategory(self, **kwargs):
        """getServiceInstancesRegisteredForShardCategory

        Args:
            
            shardCategory, str: shardCategory (required)
            
            
        
        Returns: ServiceInstancesForShardCategoryResult
        """

        allParams = ['shardCategory']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getServiceInstancesRegisteredForShardCategory" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/shard/dcache/shard-category/{shardCategory}/service-instance'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        
        if ('shardCategory' in params):
            replacement = str(self.apiClient.toPathValue(params['shardCategory']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'shardCategory' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ServiceInstancesForShardCategoryResult')
        return responseObject
        
        
        
    
    def getServiceInstanceCountsRegisteredForShardCategory(self, **kwargs):
        """getServiceInstanceCountsRegisteredForShardCategory

        Args:
            
            shardCategory, str: shardCategory (required)
            
            
        
        Returns: ServiceInstanceOwnershipCountResult
        """

        allParams = ['shardCategory']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getServiceInstanceCountsRegisteredForShardCategory" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/shard/dcache/shard-category/{shardCategory}/service-instance/count'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        
        if ('shardCategory' in params):
            replacement = str(self.apiClient.toPathValue(params['shardCategory']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'shardCategory' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ServiceInstanceOwnershipCountResult')
        return responseObject
        
        
        
    
    def getKnownResourcesForShardCategoryOwnedByServiceInstance(self, **kwargs):
        """getKnownResourcesForShardCategoryOwnedByServiceInstance

        Args:
            
            shardCategory, str: shardCategory (required)
            
            
            serviceInstance, str: serviceInstance (required)
            
            
        
        Returns: KnownResourcesResult
        """

        allParams = ['shardCategory', 'serviceInstance']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getKnownResourcesForShardCategoryOwnedByServiceInstance" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/shard/dcache/shard-category/{shardCategory}/service-instance/{serviceInstance}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        
        if ('shardCategory' in params):
            replacement = str(self.apiClient.toPathValue(params['shardCategory']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'shardCategory' + '}',
                                                replacement)
        
        if ('serviceInstance' in params):
            replacement = str(self.apiClient.toPathValue(params['serviceInstance']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'serviceInstance' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'KnownResourcesResult')
        return responseObject
        
        
        
    


