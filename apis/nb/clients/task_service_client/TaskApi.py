#!/usr/bin/env python
#pylint: skip-file
"""
TaskApi.py
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


class TaskApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient



    def getTaskByRange(self, **kwargs):
        """getTaskByRange

        Args:

            offset, int: Index (required)


            limit, int: The maximum value of {limit} supported is 500. &lt;br/&gt; Base 1 indexing for {limit}, minimum value is 1 (required)



        Returns: TaskDTOListResponse
        """

        allParams = ['offset', 'limit']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getTaskByRange" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/task/{offset}/{limit}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('offset' in params):
            replacement = str(self.apiClient.toPathValue(params['offset']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'offset' + '}',
                                                replacement)

        if ('limit' in params):
            replacement = str(self.apiClient.toPathValue(params['limit']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'limit' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskDTOListResponse')
        return responseObject




    def getTask(self, **kwargs):
        """getTruststoreFileCount

        Args:

            taskId, str: UUID of the Task (required)



        Returns: TaskDTOResponse
        """

        allParams = ['taskId']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getTask" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/task/{taskId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('taskId' in params):
            replacement = str(self.apiClient.toPathValue(params['taskId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'taskId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskDTOResponse')
        return responseObject




    def getTaskTree(self, **kwargs):
        """Get Task Tree

        Args:

            taskId, str: UUID of the Task (required)



        Returns: TaskDTOListResponse
        """

        allParams = ['taskId']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getTaskTree" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/task/{taskId}/tree'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('taskId' in params):
            replacement = str(self.apiClient.toPathValue(params['taskId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'taskId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskDTOListResponse')
        return responseObject






