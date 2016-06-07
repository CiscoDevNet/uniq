#!/usr/bin/env python
#pylint: skip-file
"""
NetworkdeviceidvlanApi.py
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


class NetworkdeviceidvlanApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient



    def getDeviceVLANData(self, **kwargs):
        """API to get the List of VLAN Data for a device

        Args:

            id, str: deviceUUID (required)


            interfaceType, str: Vlan assocaited with sub-interface (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: VlanListResult
        """

        allParams = ['id', 'interfaceType', 'scope']

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



        if ('scope' in params):
            headerParams['scope'] = params['scope']



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






