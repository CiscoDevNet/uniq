#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.
# changed the name of the file manually from ScheduledjobApi.py to SchedulerApi.py

import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *

#changed the name of the class manually from ScheduledjobApi to SchedulerApi
class SchedulerApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient



    def getAllScheduledTasks(self, **kwargs):
        """List scheduled tasks (Pagination)

        Args:

            sortBy, str: sortBy (required)


            order, str: orderBy (required)


            groupName, str: filterByGroup (required)


            origin, str: filterByOrigin (required)


            operation, str: filterByOperation (required)


            taskId, str: filterByTaskId (required)


            limit, str: limit (required)


            offset, str: offset (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: ScheduleInfoOutputListResult
        """

        allParams = ['sortBy', 'order', 'groupName', 'origin', 'operation', 'taskId', 'limit', 'offset', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAllScheduledTasks" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/scheduled-job'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('sortBy' in params):
            queryParams['sortBy'] = self.apiClient.toPathValue(params['sortBy'])

        if ('order' in params):
            queryParams['order'] = self.apiClient.toPathValue(params['order'])

        if ('groupName' in params):
            queryParams['groupName'] = self.apiClient.toPathValue(params['groupName'])

        if ('origin' in params):
            queryParams['origin'] = self.apiClient.toPathValue(params['origin'])

        if ('operation' in params):
            queryParams['operation'] = self.apiClient.toPathValue(params['operation'])

        if ('taskId' in params):
            queryParams['taskId'] = self.apiClient.toPathValue(params['taskId'])

        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])

        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])



        if ('scope' in params):
            headerParams['scope'] = params['scope']








        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ScheduleInfoOutputListResult')
        return responseObject




    def getScheduledTask(self, **kwargs):
        """Retrieves a specific scheduled task

        Args:

            scheduledWorkSpecId, str: ScheduledWorkSpecification Id (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: ScheduleInfoOutputResult
        """

        allParams = ['scheduledWorkSpecId', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getScheduledTask" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/scheduled-job/{scheduledWorkSpecId}'
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



        if ('scheduledWorkSpecId' in params):
            replacement = str(self.apiClient.toPathValue(params['scheduledWorkSpecId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'scheduledWorkSpecId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ScheduleInfoOutputResult')
        return responseObject




    def deleteScheduledTask(self, **kwargs):
        """Deletes a specific scheduled task

        Args:

            scheduledWorkSpecId, str: ScheduledWorkSpecification Id (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['scheduledWorkSpecId', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteScheduledTask" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/scheduled-job/{scheduledWorkSpecId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']



        if ('scheduledWorkSpecId' in params):
            replacement = str(self.apiClient.toPathValue(params['scheduledWorkSpecId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'scheduledWorkSpecId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject






