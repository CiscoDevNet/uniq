#!/usr/bin/env python
#pylint: skip-file
"""
AuditApi.py
    Copyright 2016 Cisco Systems

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

"""
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


        Returns: ListAuditResourceDTOResponse
        """

        allParams = ['auditParentId', 'auditParameters', 'auditId', 'deviceIP', 'instanceUuid', 'createdDateTime', 'auditDescription', 'hasChildren', 'tag','derivedParentId','state','persistDateTime','siteName','auditRequestor','hasParent','deviceName']

        params = locals()
        for (key, val) in params['kwargs'].items():
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

        if ('auditParentId' in params):
            queryParams['auditParentId'] = self.apiClient.toPathValue(params['auditParentId'])


        if ('auditParameters' in params):
            queryParams['auditParameters'] = self.apiClient.toPathValue(params['auditParameters'])

        if ('auditId' in params):
            queryParams['auditId'] = self.apiClient.toPathValue(params['auditId'])

        if ('deviceIP' in params):
            queryParams['deviceIP'] = self.apiClient.toPathValue(params['deviceIP'])

        if ('instanceUuid' in params):
            queryParams['instanceUuid'] = self.apiClient.toPathValue(params['instanceUuid'])

        if ('createdDateTime' in params):
            queryParams['createdDateTime'] = self.apiClient.toPathValue(params['createdDateTime'])

        if ('auditDescription' in params):
            queryParams['auditDescription'] = self.apiClient.toPathValue(params['auditDescription'])

        if ('hasChildren' in params):
            queryParams['hasChildren'] = self.apiClient.toPathValue(params['hasChildren'])

        if ('auditDescription' in params):
            queryParams['auditDescription'] = self.apiClient.toPathValue(params['auditDescription'])

        if ('tag' in params):
            queryParams['tag'] = self.apiClient.toPathValue(params['tag'])

        if ('derivedParentId' in params):
            queryParams['derivedParentId'] = self.apiClient.toPathValue(params['derivedParentId'])

        if ('state' in params):
            queryParams['state'] = self.apiClient.toPathValue(params['state'])

        if ('persistDateTime' in params):
            queryParams['persistDateTime'] = self.apiClient.toPathValue(params['persistDateTime'])

        if ('siteName' in params):
            queryParams['siteName'] = self.apiClient.toPathValue(params['siteName'])

        if ('auditRequestor' in params):
            queryParams['auditRequestor'] = self.apiClient.toPathValue(params['auditRequestor'])

        if ('hasParent' in params):
            queryParams['hasParent'] = self.apiClient.toPathValue(params['hasParent'])

        if ('deviceName' in params):
            queryParams['deviceName'] = self.apiClient.toPathValue(params['deviceName'])

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ListAuditResourceDTOResponse')
        return responseObject
        #return response


    def downloadAuditLogs(self, **kwargs):
        """Download Audit logs to a file.

        Args:


        Returns: TaskIdResult
        """

        allParams = []

        params = locals()
        for (key, val) in params['kwargs'].items():
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
        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject


















