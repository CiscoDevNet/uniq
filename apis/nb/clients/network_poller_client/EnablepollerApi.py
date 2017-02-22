#!/usr/bin/env python
# pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error
from .models import *


class EnablepollerApi(object):
    def __init__(self, apiClient):
        self.apiClient = apiClient

    def initializeApi(self, **kwargs):
        """Enable and disable command runner Api in APIC-EM

        Args:

            propertyvalue, str: propertyvalue (required)


            username, str: requestorUsername (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['propertyValue', 'username', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addDeviceToSite" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/inventory/global-settings?propertyName=CLI_RUNNER_INSTALLED'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        if ('propertyValue' in params):
            queryParams['propertyValue'] = self.apiClient.toPathValue(params['propertyValue'])

        if ('username' in params):
            headerParams['username'] = params['username']

        if ('scope' in params):
            headerParams['scope'] = params['scope']

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
