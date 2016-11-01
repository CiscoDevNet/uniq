#!/usr/bin/env python
#pylint: skip-file

# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class SiteProvisionApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    def provisionBranch(self, **kwargs):
        """ Provisions an IWAN branch

        Args:
            scheduleAt, str: scheduleAt (required)
            scheduleDesc, str: scheduleDesc (required)
            scheduleOrigin, str: scheduleOrigin (required)
            branchSiteDTO, BranchSiteDTO: branchSiteDTO (required)
            scope, str: Authorization Scope for RBAC (required)
            username, str: requestUsername (required)

        Returns: TaskIdResult
        """

        allParams = ['scheduleAt', 'scheduleDesc', 'scheduleOrigin', 'branchSiteDTO', 'scope',
                     'username']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError(
                  "Got an unexpected keyword argument '%s' to method addApplication" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/site-provision'
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

        if ('scope' in params):
            headerParams['scope'] = params['scope']

        if ('username' in params):
            headerParams['username'] = params['username']

        if ('branchSiteDTO' in params):
            bodyParam = params['branchSiteDTO']

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
