#!/usr/bin/env python
#pylint: skip-file
"""
FlowanalysisApi.py
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


class FlowanalysisApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient



    def getAllFlowAnalysis(self, **kwargs):
        """Retrieves a summary of all flow analyses stored

        Args:

            periodicRefresh, bool: Is analysis periodically refreshed? (required)


            sourceIP, str: Source IP address (required)


            destIP, str: Destination IP adress (required)


            sourcePort, str: Source port (required)


            destPort, str: Destination port (required)


            gtCreateTime, long: Analyses requested after this time (required)


            ltCreateTime, long: Analyses requested before this time (required)


            protocol, str: Protocol (required)


            status, str: Status (required)


            taskId, str: Task ID (required)


            lastUpdateTime, str: Last update time (required)


            limit, str: Number of resources returned (required)


            offset, str: Start index of resources returned (1-based) (required)


            order, str: Order by this field (required)


            sortBy, str: Sort by this field (required)



        Returns: FlowAnalysisListOutput
        """

        allParams = ['periodicRefresh', 'sourceIP', 'destIP', 'sourcePort', 'destPort', 'gtCreateTime', 'ltCreateTime', 'protocol', 'status', 'taskId', 'lastUpdateTime', 'limit', 'offset', 'order', 'sortBy']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAllFlowAnalysis" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/flow-analysis'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('periodicRefresh' in params):
            queryParams['periodicRefresh'] = self.apiClient.toPathValue(params['periodicRefresh'])

        if ('sourceIP' in params):
            queryParams['sourceIP'] = self.apiClient.toPathValue(params['sourceIP'])

        if ('destIP' in params):
            queryParams['destIP'] = self.apiClient.toPathValue(params['destIP'])

        if ('sourcePort' in params):
            queryParams['sourcePort'] = self.apiClient.toPathValue(params['sourcePort'])

        if ('destPort' in params):
            queryParams['destPort'] = self.apiClient.toPathValue(params['destPort'])

        if ('gtCreateTime' in params):
            queryParams['gtCreateTime'] = self.apiClient.toPathValue(params['gtCreateTime'])

        if ('ltCreateTime' in params):
            queryParams['ltCreateTime'] = self.apiClient.toPathValue(params['ltCreateTime'])

        if ('protocol' in params):
            queryParams['protocol'] = self.apiClient.toPathValue(params['protocol'])

        if ('status' in params):
            queryParams['status'] = self.apiClient.toPathValue(params['status'])

        if ('taskId' in params):
            queryParams['taskId'] = self.apiClient.toPathValue(params['taskId'])

        if ('lastUpdateTime' in params):
            queryParams['lastUpdateTime'] = self.apiClient.toPathValue(params['lastUpdateTime'])

        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])

        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])

        if ('order' in params):
            queryParams['order'] = self.apiClient.toPathValue(params['order'])

        if ('sortBy' in params):
            queryParams['sortBy'] = self.apiClient.toPathValue(params['sortBy'])










        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'FlowAnalysisListOutput')
        return responseObject




    def initiateFlowAnalysis(self, **kwargs):
        """Initiates a new flow analysis

        Args:

            flowAnalysisRequest, FlowAnalysisRequest: flowAnalysisRequest (required)



        Returns: FlowAnalysisRequestResultOutput
        """

        allParams = ['flowAnalysisRequest']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method initiateFlowAnalysis" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/flow-analysis'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'










        if ('flowAnalysisRequest' in params):
            bodyParam = params['flowAnalysisRequest']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'FlowAnalysisRequestResultOutput')
        return responseObject




    def getFullFlowAnalysisResult(self, **kwargs):
        """Retrieves result of a previously requested flow analysis

        Args:

            flowAnalysisId, str: Flow analysis request id (required)



        Returns: PathResponseResult
        """

        allParams = ['flowAnalysisId']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getFullFlowAnalysisResult" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/flow-analysis/{flowAnalysisId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('flowAnalysisId' in params):
            replacement = str(self.apiClient.toPathValue(params['flowAnalysisId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'flowAnalysisId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'PathResponseResult')
        return responseObject




    def deleteFlowAnalysis(self, **kwargs):
        """Deletes a flow analysis request

        Args:

            flowAnalysisId, str: Flow analysis request id (required)



        Returns: TaskIdResult
        """

        allParams = ['flowAnalysisId']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteFlowAnalysis" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/flow-analysis/{flowAnalysisId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('flowAnalysisId' in params):
            replacement = str(self.apiClient.toPathValue(params['flowAnalysisId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'flowAnalysisId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject






