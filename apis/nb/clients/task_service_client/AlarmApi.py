#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class AlarmApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getAlarmWithFilter(self, **kwargs):
        """Retrieve Alarms

        Args:
            
        
        Returns: ListAlarmDTOResponse
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAlarmWithFilter" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/alarm'
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

        responseObject = self.apiClient.deserialize(response, 'ListAlarmDTOResponse')
        return responseObject
        
        
        
    
    def getAlarmCountWithFilter(self, **kwargs):
        """Retrieve Count of number of alarms

        Args:
            
        
        Returns: int
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAlarmCountWithFilter" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/alarm/count'
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

        responseObject = self.apiClient.deserialize(response, 'int')
        return responseObject
        
        
        
    
    def acknowledgeAlarm(self, **kwargs):
        """Acknowledge an Alarm by UUID

        Args:
            
            alertUUID, str: alertUUID (required)
            
            
            alarmDTO, AlarmDTO: alarmDTO (required)
            
            
        
        Returns: SuccessResult
        """

        allParams = ['alertUUID', 'alarmDTO']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method acknowledgeAlarm" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/alarm/{alertUUID}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        
        if ('alertUUID' in params):
            replacement = str(self.apiClient.toPathValue(params['alertUUID']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'alertUUID' + '}',
                                                replacement)
        

        

        
        if ('alarmDTO' in params):
            bodyParam = params['alarmDTO']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SuccessResult')
        return responseObject
        
        
        
    


