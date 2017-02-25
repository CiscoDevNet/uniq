#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class NetworkdeviceidvlanApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getDeviceVLANData(self, **kwargs):
        """Retrieves list of VLAN data for a device

        Args:
            
            id, str: deviceUUID (required)
            
            
            interfaceType, str: Vlan assocaited with sub-interface (required)
            
            
        
        Returns: VlanListResult
        """

        allParams = ['id', 'interfaceType']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getDeviceVLANData" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device/{id}/vlan'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('interfaceType' in params):
            queryParams['interfaceType'] = self.apiClient.toPathValue(params['interfaceType'])
        

        

        
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

        responseObject = self.apiClient.deserialize(response, 'VlanListResult')
        return responseObject
        
        
        
    


