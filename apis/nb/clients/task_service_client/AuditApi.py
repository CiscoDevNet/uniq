#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class AuditApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getAuditWithFilter(self, **kwargs):
        """Retrieve Audit by flexible search

        Args:
            
            auditRequestor, str: This is the user who triggered the event (required)
            
            
            limit, str: This is the number of records fetched (required)
            
            
            offset, str: This is the offset used for pagination (required)
            
            
            auditRecordStartTime, str: This is the epoch start time from which audit records need to be fetched (required)
            
            
            auditRecordEndTime, str: This is the epoch end time upto which audit records need to be fetched (required)
            
            
            deviceIP, str: This is the device ip of the device (required)
            
            
            siteName, str: This is the site name associated to the audit record (required)
            
            
            deviceName, str: This is the device name assoicated to the audit (required)
            
            
            applicationName, str: This is the applicaiton name that generated the audit (required)
            
            
            tag, str: This is the tag defined for audit (required)
            
            
            severity, str: This is the severity of the audit record (required)
            
            
        
        Returns: ListAuditResourceDTOResponse
        """

        allParams = ['auditRequestor', 'limit', 'offset', 'auditRecordStartTime', 'auditRecordEndTime', 'deviceIP', 'siteName', 'deviceName', 'applicationName', 'tag', 'severity']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAuditWithFilter" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/audit'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('auditRequestor' in params):
            queryParams['auditRequestor'] = self.apiClient.toPathValue(params['auditRequestor'])
        
        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])
        
        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])
        
        if ('auditRecordStartTime' in params):
            queryParams['auditRecordStartTime'] = self.apiClient.toPathValue(params['auditRecordStartTime'])
        
        if ('auditRecordEndTime' in params):
            queryParams['auditRecordEndTime'] = self.apiClient.toPathValue(params['auditRecordEndTime'])
        
        if ('deviceIP' in params):
            queryParams['deviceIP'] = self.apiClient.toPathValue(params['deviceIP'])
        
        if ('siteName' in params):
            queryParams['siteName'] = self.apiClient.toPathValue(params['siteName'])
        
        if ('deviceName' in params):
            queryParams['deviceName'] = self.apiClient.toPathValue(params['deviceName'])
        
        if ('applicationName' in params):
            queryParams['applicationName'] = self.apiClient.toPathValue(params['applicationName'])
        
        if ('tag' in params):
            queryParams['tag'] = self.apiClient.toPathValue(params['tag'])
        
        if ('severity' in params):
            queryParams['severity'] = self.apiClient.toPathValue(params['severity'])
        

        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ListAuditResourceDTOResponse')
        return responseObject
        
        
        
    
    def getAuditCountWithFilter(self, **kwargs):
        """Retrieve Count of number of records to be fetched by flexible search

        Args:
            
            auditRequestor, str: This is the user who triggered the event (required)
            
            
            auditRecordStartTime, str: This is the epoch start time from which audit records need to be fetched (required)
            
            
            auditRecordEndTime, str: This is the epoch end time upto which audit records need to be fetched (required)
            
            
            deviceIP, str: This is the device ip of the device (required)
            
            
            siteName, str: This is the site name associated to the audit record (required)
            
            
            deviceName, str: This is the device name assoicated to the audit (required)
            
            
            applicationName, str: This is the applicaiton name that generated the audit (required)
            
            
            tag, str: This is the tag defined for audit (required)
            
            
            severity, str: This is the severity of the audit record (required)
            
            
        
        Returns: SuccessResult
        """

        allParams = ['auditRequestor', 'auditRecordStartTime', 'auditRecordEndTime', 'deviceIP', 'siteName', 'deviceName', 'applicationName', 'tag', 'severity']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAuditCountWithFilter" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/audit/count'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('auditRequestor' in params):
            queryParams['auditRequestor'] = self.apiClient.toPathValue(params['auditRequestor'])
        
        if ('auditRecordStartTime' in params):
            queryParams['auditRecordStartTime'] = self.apiClient.toPathValue(params['auditRecordStartTime'])
        
        if ('auditRecordEndTime' in params):
            queryParams['auditRecordEndTime'] = self.apiClient.toPathValue(params['auditRecordEndTime'])
        
        if ('deviceIP' in params):
            queryParams['deviceIP'] = self.apiClient.toPathValue(params['deviceIP'])
        
        if ('siteName' in params):
            queryParams['siteName'] = self.apiClient.toPathValue(params['siteName'])
        
        if ('deviceName' in params):
            queryParams['deviceName'] = self.apiClient.toPathValue(params['deviceName'])
        
        if ('applicationName' in params):
            queryParams['applicationName'] = self.apiClient.toPathValue(params['applicationName'])
        
        if ('tag' in params):
            queryParams['tag'] = self.apiClient.toPathValue(params['tag'])
        
        if ('severity' in params):
            queryParams['severity'] = self.apiClient.toPathValue(params['severity'])
        

        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SuccessResult')
        return responseObject
        
        
        
    
    def downloadAuditLogs(self, **kwargs):
        """Download Audit logs to a file. 

        Args:
            
            auditRequestor, str: This is the user who triggered the event (required)
            
            
            auditRecordStartTime, str: This is the epoch start time from which audit records need to be fetched (required)
            
            
            auditRecordEndTime, str: This is the epoch end time upto which audit records need to be fetched (required)
            
            
            deviceIP, str: This is the device ip of the device (required)
            
            
            siteName, str: This is the site name associated to the audit record (required)
            
            
            deviceName, str: This is the device name assoicated to the audit (required)
            
            
            applicationName, str: This is the applicaiton name that generated the audit (required)
            
            
            tag, str: This is the tag defined for audit (required)
            
            
            severity, str: This is the severity of the audit record (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['auditRequestor', 'auditRecordStartTime', 'auditRecordEndTime', 'deviceIP', 'siteName', 'deviceName', 'applicationName', 'tag', 'severity']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method downloadAuditLogs" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/audit/download'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('auditRequestor' in params):
            queryParams['auditRequestor'] = self.apiClient.toPathValue(params['auditRequestor'])
        
        if ('auditRecordStartTime' in params):
            queryParams['auditRecordStartTime'] = self.apiClient.toPathValue(params['auditRecordStartTime'])
        
        if ('auditRecordEndTime' in params):
            queryParams['auditRecordEndTime'] = self.apiClient.toPathValue(params['auditRecordEndTime'])
        
        if ('deviceIP' in params):
            queryParams['deviceIP'] = self.apiClient.toPathValue(params['deviceIP'])
        
        if ('siteName' in params):
            queryParams['siteName'] = self.apiClient.toPathValue(params['siteName'])
        
        if ('deviceName' in params):
            queryParams['deviceName'] = self.apiClient.toPathValue(params['deviceName'])
        
        if ('applicationName' in params):
            queryParams['applicationName'] = self.apiClient.toPathValue(params['applicationName'])
        
        if ('tag' in params):
            queryParams['tag'] = self.apiClient.toPathValue(params['tag'])
        
        if ('severity' in params):
            queryParams['severity'] = self.apiClient.toPathValue(params['severity'])
        

        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    


