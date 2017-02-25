#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class SegmentApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getSegmentInfo(self, **kwargs):
        """Retrieves list of segment info based on the policy tag

        Args:
            
            type, str: Type of segment (required)
            
            
            policyTag, str: Policy tag (required)
            
            
        
        Returns: SegmentResult
        """

        allParams = ['type', 'policyTag']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getSegmentInfo" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/segment'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('type' in params):
            queryParams['type'] = self.apiClient.toPathValue(params['type'])
        
        if ('policyTag' in params):
            queryParams['policyTag'] = self.apiClient.toPathValue(params['policyTag'])
        

        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SegmentResult')
        return responseObject
        
        
        
    


