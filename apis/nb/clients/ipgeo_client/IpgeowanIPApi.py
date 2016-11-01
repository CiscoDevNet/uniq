#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class IpgeowanIPApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getCityInfo(self, **kwargs):
        """Get city details for a WAN IP address

        Args:
            
            wanIP, str: space-separated WAN IP addresses (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: IPGeoModelResult
        """

        allParams = ['wanIP', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getCityInfo" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ipgeo/{wanIP}'
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
        

        
        if ('wanIP' in params):
            replacement = str(self.apiClient.toPathValue(params['wanIP']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'wanIP' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'IPGeoModelResult')
        return responseObject
        
        
        
    


