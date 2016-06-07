#!/usr/bin/env python
#pylint: skip-file
"""
ApplicationApi.py
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


class ApplicationApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient



    def getFilterApplication(self, **kwargs):
        """Retrieves applications based on a given filter, filters should be applied one at a time, except for the limit/index pagination filters.

        Args:

            isCustom, str: Retrieve custom applications (required)


            isRepresentative, str: Retrieve representative applications (required)


            categoryId, str: Retrieve applications by categoryId (required)


            name, str: name (required)


            offset, str: Starting index of the resources (1 based), This should be only used in conjuction with the limit param. (required)


            limit, str: Number of resources to return, WARNING: results may take an unexpectely long time with more than 50 results requested. (required)



        Returns: ApplicationListResult
        """

        allParams = ['isCustom', 'isRepresentative', 'categoryId', 'name', 'offset', 'limit']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getFilterApplication" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/application'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('isCustom' in params):
            queryParams['isCustom'] = self.apiClient.toPathValue(params['isCustom'])

        if ('isRepresentative' in params):
            queryParams['isRepresentative'] = self.apiClient.toPathValue(params['isRepresentative'])

        if ('categoryId' in params):
            queryParams['categoryId'] = self.apiClient.toPathValue(params['categoryId'])

        if ('name' in params):
            queryParams['name'] = self.apiClient.toPathValue(params['name'])

        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])

        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])










        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ApplicationListResult')
        return responseObject




    def updateApplication(self, **kwargs):
        """Updates application(s)

        Args:

            scheduleAt, str: scheduleAt (required)


            scheduleDesc, str: scheduleDesc (required)


            scheduleOrigin, str: scheduleOrigin (required)


            applicationDTOList, list[ApplicationDTO]: applicationDTOList (required)



        Returns: TaskIdResult
        """

        allParams = ['scheduleAt', 'scheduleDesc', 'scheduleOrigin', 'applicationDTOList']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateApplication" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/application'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('scheduleAt' in params):
            queryParams['scheduleAt'] = self.apiClient.toPathValue(params['scheduleAt'])

        if ('scheduleDesc' in params):
            queryParams['scheduleDesc'] = self.apiClient.toPathValue(params['scheduleDesc'])

        if ('scheduleOrigin' in params):
            queryParams['scheduleOrigin'] = self.apiClient.toPathValue(params['scheduleOrigin'])









        if ('applicationDTOList' in params):
            bodyParam = params['applicationDTOList']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def addApplication(self, **kwargs):
        """Creates custom application(s)

        Args:

            scheduleAt, str: scheduleAt (required)


            scheduleDesc, str: scheduleDesc (required)


            scheduleOrigin, str: scheduleOrigin (required)


            applicationDTOList, list[ApplicationDTO]: applicationDTOList (required)



        Returns: TaskIdResult
        """

        allParams = ['scheduleAt', 'scheduleDesc', 'scheduleOrigin', 'applicationDTOList']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addApplication" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/application'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('scheduleAt' in params):
            queryParams['scheduleAt'] = self.apiClient.toPathValue(params['scheduleAt'])

        if ('scheduleDesc' in params):
            queryParams['scheduleDesc'] = self.apiClient.toPathValue(params['scheduleDesc'])

        if ('scheduleOrigin' in params):
            queryParams['scheduleOrigin'] = self.apiClient.toPathValue(params['scheduleOrigin'])









        if ('applicationDTOList' in params):
            bodyParam = params['applicationDTOList']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getApplicationCount(self, **kwargs):
        """Return total count of application(s)

        Args:


        Returns: CountResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getApplicationCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/application/count'
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

        responseObject = self.apiClient.deserialize(response, 'CountResult')
        return responseObject




    def getApplication(self, **kwargs):
        """Return an application given an id

        Args:

            id, str: id (required)



        Returns: ApplicationResult
        """

        allParams = ['id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getApplication" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/application/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'ApplicationResult')
        return responseObject




    def deleteApplication(self, **kwargs):
        """Delete an application by id

        Args:

            scheduleAt, str: scheduleAt (required)


            scheduleDesc, str: scheduleDesc (required)


            scheduleOrigin, str: scheduleOrigin (required)


            id, str: id (required)



        Returns: TaskIdResult
        """

        allParams = ['scheduleAt', 'scheduleDesc', 'scheduleOrigin', 'id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteApplication" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/application/{id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('scheduleAt' in params):
            queryParams['scheduleAt'] = self.apiClient.toPathValue(params['scheduleAt'])

        if ('scheduleDesc' in params):
            queryParams['scheduleDesc'] = self.apiClient.toPathValue(params['scheduleDesc'])

        if ('scheduleOrigin' in params):
            queryParams['scheduleOrigin'] = self.apiClient.toPathValue(params['scheduleOrigin'])





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






