#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class PnpsearchApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getPnpAllSiteDevicesByRange(self, **kwargs):
        """This API is used to retrieve PnP resources based on search fields (Pagination)

        Args:
            
            hostName, str: Host name (required)
            
            
            productId, str: Product ID (required)
            
            
            serialNumber, str: Serial number (required)
            
            
            state, str: State of device. PENDING, PROVISIONED, IN_PROGRESS, ERROR. Accepts a list of states (required)
            
            
            deviceMatchesARule, bool: Should device match a rule (true) or not (false).  Current support true only. Set (true) to retrieve a list of devices under all project(s)  (required)
            
            
            offset, int: Starting index of the response. Minimum value is 1 (required)
            
            
            limit, int: Limit the number of responses. Maximum value supported is 500. Minimum value is 1 (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: ZtdSearchListResult
        """

        allParams = ['hostName', 'productId', 'serialNumber', 'state', 'deviceMatchesARule', 'offset', 'limit', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPnpAllSiteDevicesByRange" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-search'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('hostName' in params):
            queryParams['hostName'] = self.apiClient.toPathValue(params['hostName'])
        
        if ('productId' in params):
            queryParams['productId'] = self.apiClient.toPathValue(params['productId'])
        
        if ('serialNumber' in params):
            queryParams['serialNumber'] = self.apiClient.toPathValue(params['serialNumber'])
        
        if ('state' in params):
            queryParams['state'] = self.apiClient.toPathValue(params['state'])
        
        if ('deviceMatchesARule' in params):
            queryParams['deviceMatchesARule'] = self.apiClient.toPathValue(params['deviceMatchesARule'])
        
        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])
        
        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])
        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ZtdSearchListResult')
        return responseObject
        
        
        
    
    def getPnpAllSiteDeviceCount(self, **kwargs):
        """This API is used to retrieve a count of PnP resources based on search fields

        Args:
            
            hostName, str: Host name (required)
            
            
            productId, str: Product ID (required)
            
            
            serialNumber, str: Serial number (required)
            
            
            state, str: State of device. PENDING, PROVISIONED, IN_PROGRESS, ERROR. Accepts a list of states (required)
            
            
            deviceMatchesARule, bool: Should device match a rule (true) or not (false).  Current support true only. Set (true) to retrieve a count of devices under all project(s)  (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: str
        """

        allParams = ['hostName', 'productId', 'serialNumber', 'state', 'deviceMatchesARule', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPnpAllSiteDeviceCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-search/count'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('hostName' in params):
            queryParams['hostName'] = self.apiClient.toPathValue(params['hostName'])
        
        if ('productId' in params):
            queryParams['productId'] = self.apiClient.toPathValue(params['productId'])
        
        if ('serialNumber' in params):
            queryParams['serialNumber'] = self.apiClient.toPathValue(params['serialNumber'])
        
        if ('state' in params):
            queryParams['state'] = self.apiClient.toPathValue(params['state'])
        
        if ('deviceMatchesARule' in params):
            queryParams['deviceMatchesARule'] = self.apiClient.toPathValue(params['deviceMatchesARule'])
        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    


