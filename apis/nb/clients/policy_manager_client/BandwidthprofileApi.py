#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class BandwidthprofileApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getAllBandwidthProfiles(self, **kwargs):
        """Retrieve all BandwidthProfiles

        Args:
            
        
        Returns: BandwidthProfileListResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAllBandwidthProfiles" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/bandwidth-profile'
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

        responseObject = self.apiClient.deserialize(response, 'BandwidthProfileListResult')
        return responseObject
        
        
        
    
    def update(self, **kwargs):
        """Update BandwidthProfile(s)

        Args:
            
            bandwidthProfileDTOs, list[BandwidthProfileDTO]: BandwidthProfile Object(s) (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['bandwidthProfileDTOs']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method update" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/bandwidth-profile'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('bandwidthProfileDTOs' in params):
            bodyParam = params['bandwidthProfileDTOs']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def add(self, **kwargs):
        """Create BandwidthProfile(s)

        Args:
            
            bandwidthProfileDTOs, list[BandwidthProfileDTO]: BandwidthProfile Object(s) (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['bandwidthProfileDTOs']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method add" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/bandwidth-profile'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('bandwidthProfileDTOs' in params):
            bodyParam = params['bandwidthProfileDTOs']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getBandwidthProfileById(self, **kwargs):
        """Retrieve a BandwidthProfile based on its id

        Args:
            
            id, str: id (required)
            
            
        
        Returns: BandwidthProfileResult
        """

        allParams = ['id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getBandwidthProfileById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/bandwidth-profile/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'BandwidthProfileResult')
        return responseObject
        
        
        
    
    def delete(self, **kwargs):
        """Delete a BandwidthProfile by its id

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

        resourcePath = '/bandwidth-profile/{id}'
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
        
        
        
    


