#!/usr/bin/env python
#pylint: skip-file
"""
TopologyApi.py
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


class TopologyApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient



    def getTopologyApplications(self, **kwargs):
        """getTopologyApplications

        Args:


        Returns: TopologyApplicationListResult
        """

        allParams = []

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getTopologyApplications" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/application'
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

        responseObject = self.apiClient.deserialize(response, 'TopologyApplicationListResult')
        return responseObject




    def updateTopologyApplication(self, **kwargs):
        """updateTopologyApplications

        Args:

            topologyApplicationDtoList, list[TopologyApplicationDto]: application (required)



        Returns: TaskIdResult
        """

        allParams = ['topologyApplicationDtoList']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateTopologyApplication" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/application'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'










        if ('topologyApplicationDtoList' in params):
            bodyParam = params['topologyApplicationDtoList']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def createTopologyApplications(self, **kwargs):
        """createTopologyApplications

        Args:

            topologyApplicationDtoList, list[TopologyApplicationDto]: application (required)



        Returns: TaskIdResult
        """

        allParams = ['topologyApplicationDtoList']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createTopologyApplications" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/application'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'










        if ('topologyApplicationDtoList' in params):
            bodyParam = params['topologyApplicationDtoList']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getTopologyApplication(self, **kwargs):
        """getTopologyApplication

        Args:

            applicationUuid, str: Topology Application Uuid (required)



        Returns: TopologyApplicationResult
        """

        allParams = ['applicationUuid']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getTopologyApplication" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/application/{applicationUuid}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('applicationUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['applicationUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'applicationUuid' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TopologyApplicationResult')
        return responseObject




    def deleteTopologyApplication(self, **kwargs):
        """deleteTopologyApplication

        Args:

            applicationUuid, str: Topology Application Uuid (required)



        Returns: TaskIdResult
        """

        allParams = ['applicationUuid']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteTopologyApplication" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/application/{applicationUuid}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('applicationUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['applicationUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'applicationUuid' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getTopologyApplicationPages(self, **kwargs):
        """getTopologyApplicationPages

        Args:

            applicationUuid, str: Topology Application Uuid (required)



        Returns: TopologyPageListResult
        """

        allParams = ['applicationUuid']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getTopologyApplicationPages" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/application/{applicationUuid}/page'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('applicationUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['applicationUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'applicationUuid' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TopologyPageListResult')
        return responseObject




    def updateTopologyPages(self, **kwargs):
        """updateTopologyPages

        Args:

            applicationUuid, str: Topology Application Uuid (required)


            topologyPageDtoList, list[TopologyPageDto]: page (required)



        Returns: TaskIdResult
        """

        allParams = ['applicationUuid', 'topologyPageDtoList']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateTopologyPages" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/application/{applicationUuid}/page'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('applicationUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['applicationUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'applicationUuid' + '}',
                                                replacement)





        if ('topologyPageDtoList' in params):
            bodyParam = params['topologyPageDtoList']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def createTopologyPages(self, **kwargs):
        """createTopologyPages

        Args:

            applicationUuid, str: Topology Application Uuid (required)


            topologyPageDtoList, list[TopologyPageDto]: page (required)



        Returns: TaskIdResult
        """

        allParams = ['applicationUuid', 'topologyPageDtoList']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createTopologyPages" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/application/{applicationUuid}/page'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('applicationUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['applicationUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'applicationUuid' + '}',
                                                replacement)





        if ('topologyPageDtoList' in params):
            bodyParam = params['topologyPageDtoList']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getTopologyApplicationPage(self, **kwargs):
        """getTopologyApplicationPage

        Args:

            applicationUuid, str: Topology Application Uuid (required)


            pageUuid, str: Topology Application Page Uuid (required)



        Returns: TopologyPageResult
        """

        allParams = ['applicationUuid', 'pageUuid']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getTopologyApplicationPage" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/application/{applicationUuid}/page/{pageUuid}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('applicationUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['applicationUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'applicationUuid' + '}',
                                                replacement)

        if ('pageUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['pageUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'pageUuid' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TopologyPageResult')
        return responseObject




    def deleteTopologyPage(self, **kwargs):
        """deleteTopologyPage

        Args:

            applicationUuid, str: Topology Application Uuid (required)


            pageUuid, str: Topology Application Page Uuid (required)



        Returns: TaskIdResult
        """

        allParams = ['applicationUuid', 'pageUuid']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteTopologyPage" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/application/{applicationUuid}/page/{pageUuid}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('applicationUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['applicationUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'applicationUuid' + '}',
                                                replacement)

        if ('pageUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['pageUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'pageUuid' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getTopologyApplicationPageViews(self, **kwargs):
        """getTopologyApplicationPageViews

        Args:

            applicationUuid, str: Topology Application Uuid (required)


            pageUuid, str: Topology Application Page Uuid (required)



        Returns: TopologyViewListResult
        """

        allParams = ['applicationUuid', 'pageUuid']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getTopologyApplicationPageViews" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/application/{applicationUuid}/page/{pageUuid}/view'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('applicationUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['applicationUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'applicationUuid' + '}',
                                                replacement)

        if ('pageUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['pageUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'pageUuid' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TopologyViewListResult')
        return responseObject




    def updateTopologyViews(self, **kwargs):
        """updateTopologyViews

        Args:

            applicationUuid, str: Topology Application Uuid (required)


            pageUuid, str: Topology Application Page Uuid (required)


            topologyViewDtoList, list[TopologyViewDto]: page (required)



        Returns: TaskIdResult
        """

        allParams = ['applicationUuid', 'pageUuid', 'topologyViewDtoList']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateTopologyViews" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/application/{applicationUuid}/page/{pageUuid}/view'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('applicationUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['applicationUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'applicationUuid' + '}',
                                                replacement)

        if ('pageUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['pageUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'pageUuid' + '}',
                                                replacement)





        if ('topologyViewDtoList' in params):
            bodyParam = params['topologyViewDtoList']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def createTopologyViews(self, **kwargs):
        """createTopologyViews

        Args:

            applicationUuid, str: Topology Application Uuid (required)


            pageUuid, str: Topology Application Page Uuid (required)


            topologyViewDtoList, list[TopologyViewDto]: view (required)



        Returns: TaskIdResult
        """

        allParams = ['applicationUuid', 'pageUuid', 'topologyViewDtoList']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createTopologyViews" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/application/{applicationUuid}/page/{pageUuid}/view'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('applicationUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['applicationUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'applicationUuid' + '}',
                                                replacement)

        if ('pageUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['pageUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'pageUuid' + '}',
                                                replacement)





        if ('topologyViewDtoList' in params):
            bodyParam = params['topologyViewDtoList']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getTopologyApplicationPageView(self, **kwargs):
        """getTopologyApplicationPageView

        Args:

            applicationUuid, str: Topology Application Uuid (required)


            pageUuid, str: Topology Application Page Uuid (required)


            viewUuid, str: Topology Application Page View Uuid (required)



        Returns: TopologyViewResult
        """

        allParams = ['applicationUuid', 'pageUuid', 'viewUuid']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getTopologyApplicationPageView" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/application/{applicationUuid}/page/{pageUuid}/view/{viewUuid}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('applicationUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['applicationUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'applicationUuid' + '}',
                                                replacement)

        if ('pageUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['pageUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'pageUuid' + '}',
                                                replacement)

        if ('viewUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['viewUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'viewUuid' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TopologyViewResult')
        return responseObject




    def deleteTopologyView(self, **kwargs):
        """deleteTopologyView

        Args:

            applicationUuid, str: Topology Application Uuid (required)


            pageUuid, str: Topology Application Page Uuid (required)


            viewUuid, str: Topology Application View Uuid (required)



        Returns: TaskIdResult
        """

        allParams = ['applicationUuid', 'pageUuid', 'viewUuid']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteTopologyView" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/application/{applicationUuid}/page/{pageUuid}/view/{viewUuid}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('applicationUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['applicationUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'applicationUuid' + '}',
                                                replacement)

        if ('pageUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['pageUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'pageUuid' + '}',
                                                replacement)

        if ('viewUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['viewUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'viewUuid' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getTopologyApplications(self, **kwargs):
        """getTopologyApplications

        Args:


        Returns: TopologyApplicationListResult
        """

        allParams = []

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getTopologyApplications" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/controllerapp'
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

        responseObject = self.apiClient.deserialize(response, 'TopologyApplicationListResult')
        return responseObject




    def updateTopologyApplication(self, **kwargs):
        """updateTopologyApplications

        Args:

            topologyApplicationDtoList, list[TopologyApplicationDto]: application (required)



        Returns: TaskIdResult
        """

        allParams = ['topologyApplicationDtoList']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateTopologyApplication" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/controllerapp'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'










        if ('topologyApplicationDtoList' in params):
            bodyParam = params['topologyApplicationDtoList']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def createTopologyApplications(self, **kwargs):
        """createTopologyApplications

        Args:

            topologyApplicationDtoList, list[TopologyApplicationDto]: application (required)



        Returns: TaskIdResult
        """

        allParams = ['topologyApplicationDtoList']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createTopologyApplications" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/controllerapp'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'










        if ('topologyApplicationDtoList' in params):
            bodyParam = params['topologyApplicationDtoList']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getTopologyApplication(self, **kwargs):
        """getTopologyApplication

        Args:

            applicationUuid, str: Topology Application Uuid (required)



        Returns: TopologyApplicationResult
        """

        allParams = ['applicationUuid']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getTopologyApplication" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/controllerapp/{applicationUuid}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('applicationUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['applicationUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'applicationUuid' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TopologyApplicationResult')
        return responseObject




    def deleteTopologyApplication(self, **kwargs):
        """deleteTopologyApplication

        Args:

            applicationUuid, str: Topology Application Uuid (required)



        Returns: TaskIdResult
        """

        allParams = ['applicationUuid']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteTopologyApplication" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/controllerapp/{applicationUuid}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('applicationUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['applicationUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'applicationUuid' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getTopologyApplicationPages(self, **kwargs):
        """getTopologyApplicationPages

        Args:

            applicationUuid, str: Topology Application Uuid (required)



        Returns: TopologyPageListResult
        """

        allParams = ['applicationUuid']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getTopologyApplicationPages" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/controllerapp/{applicationUuid}/page'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('applicationUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['applicationUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'applicationUuid' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TopologyPageListResult')
        return responseObject




    def updateTopologyPages(self, **kwargs):
        """updateTopologyPages

        Args:

            applicationUuid, str: Topology Application Uuid (required)


            topologyPageDtoList, list[TopologyPageDto]: page (required)



        Returns: TaskIdResult
        """

        allParams = ['applicationUuid', 'topologyPageDtoList']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateTopologyPages" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/controllerapp/{applicationUuid}/page'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('applicationUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['applicationUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'applicationUuid' + '}',
                                                replacement)





        if ('topologyPageDtoList' in params):
            bodyParam = params['topologyPageDtoList']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def createTopologyPages(self, **kwargs):
        """createTopologyPages

        Args:

            applicationUuid, str: Topology Application Uuid (required)


            topologyPageDtoList, list[TopologyPageDto]: page (required)



        Returns: TaskIdResult
        """

        allParams = ['applicationUuid', 'topologyPageDtoList']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createTopologyPages" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/controllerapp/{applicationUuid}/page'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('applicationUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['applicationUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'applicationUuid' + '}',
                                                replacement)





        if ('topologyPageDtoList' in params):
            bodyParam = params['topologyPageDtoList']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getTopologyApplicationPage(self, **kwargs):
        """getTopologyApplicationPage

        Args:

            applicationUuid, str: Topology Application Uuid (required)


            pageUuid, str: Topology Application Page Uuid (required)



        Returns: TopologyPageResult
        """

        allParams = ['applicationUuid', 'pageUuid']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getTopologyApplicationPage" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/controllerapp/{applicationUuid}/page/{pageUuid}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('applicationUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['applicationUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'applicationUuid' + '}',
                                                replacement)

        if ('pageUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['pageUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'pageUuid' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TopologyPageResult')
        return responseObject




    def deleteTopologyPage(self, **kwargs):
        """deleteTopologyPage

        Args:

            applicationUuid, str: Topology Application Uuid (required)


            pageUuid, str: Topology Application Page Uuid (required)



        Returns: TaskIdResult
        """

        allParams = ['applicationUuid', 'pageUuid']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteTopologyPage" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/controllerapp/{applicationUuid}/page/{pageUuid}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('applicationUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['applicationUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'applicationUuid' + '}',
                                                replacement)

        if ('pageUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['pageUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'pageUuid' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getTopologyApplicationPageViews(self, **kwargs):
        """getTopologyApplicationPageViews

        Args:

            applicationUuid, str: Topology Application Uuid (required)


            pageUuid, str: Topology Application Page Uuid (required)



        Returns: TopologyViewListResult
        """

        allParams = ['applicationUuid', 'pageUuid']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getTopologyApplicationPageViews" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/controllerapp/{applicationUuid}/page/{pageUuid}/view'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('applicationUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['applicationUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'applicationUuid' + '}',
                                                replacement)

        if ('pageUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['pageUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'pageUuid' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TopologyViewListResult')
        return responseObject




    def updateTopologyViews(self, **kwargs):
        """updateTopologyViews

        Args:

            applicationUuid, str: Topology Application Uuid (required)


            pageUuid, str: Topology Application Page Uuid (required)


            topologyViewDtoList, list[TopologyViewDto]: page (required)



        Returns: TaskIdResult
        """

        allParams = ['applicationUuid', 'pageUuid', 'topologyViewDtoList']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateTopologyViews" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/controllerapp/{applicationUuid}/page/{pageUuid}/view'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('applicationUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['applicationUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'applicationUuid' + '}',
                                                replacement)

        if ('pageUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['pageUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'pageUuid' + '}',
                                                replacement)





        if ('topologyViewDtoList' in params):
            bodyParam = params['topologyViewDtoList']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def createTopologyViews(self, **kwargs):
        """createTopologyViews

        Args:

            applicationUuid, str: Topology Application Uuid (required)


            pageUuid, str: Topology Application Page Uuid (required)


            topologyViewDtoList, list[TopologyViewDto]: view (required)



        Returns: TaskIdResult
        """

        allParams = ['applicationUuid', 'pageUuid', 'topologyViewDtoList']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createTopologyViews" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/controllerapp/{applicationUuid}/page/{pageUuid}/view'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('applicationUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['applicationUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'applicationUuid' + '}',
                                                replacement)

        if ('pageUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['pageUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'pageUuid' + '}',
                                                replacement)





        if ('topologyViewDtoList' in params):
            bodyParam = params['topologyViewDtoList']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getTopologyApplicationPageView(self, **kwargs):
        """getTopologyApplicationPageView

        Args:

            applicationUuid, str: Topology Application Uuid (required)


            pageUuid, str: Topology Application Page Uuid (required)


            viewUuid, str: Topology Application Page View Uuid (required)



        Returns: TopologyViewResult
        """

        allParams = ['applicationUuid', 'pageUuid', 'viewUuid']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getTopologyApplicationPageView" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/controllerapp/{applicationUuid}/page/{pageUuid}/view/{viewUuid}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('applicationUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['applicationUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'applicationUuid' + '}',
                                                replacement)

        if ('pageUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['pageUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'pageUuid' + '}',
                                                replacement)

        if ('viewUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['viewUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'viewUuid' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TopologyViewResult')
        return responseObject




    def deleteTopologyView(self, **kwargs):
        """deleteTopologyView

        Args:

            applicationUuid, str: Topology Application Uuid (required)


            pageUuid, str: Topology Application Page Uuid (required)


            viewUuid, str: Topology Application View Uuid (required)



        Returns: TaskIdResult
        """

        allParams = ['applicationUuid', 'pageUuid', 'viewUuid']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteTopologyView" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/controllerapp/{applicationUuid}/page/{pageUuid}/view/{viewUuid}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('applicationUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['applicationUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'applicationUuid' + '}',
                                                replacement)

        if ('pageUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['pageUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'pageUuid' + '}',
                                                replacement)

        if ('viewUuid' in params):
            replacement = str(self.apiClient.toPathValue(params['viewUuid']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'viewUuid' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def loadCustomTopology(self, **kwargs):
        """loadCustomTopology

        Args:


        Returns: TopologyResult
        """

        allParams = []

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method loadCustomTopology" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/custom'
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

        responseObject = self.apiClient.deserialize(response, 'TopologyResult')
        return responseObject




    def saveCustomTopology(self, **kwargs):
        """saveCustomTopology

        Args:

            topo, Topology: Topology (required)



        Returns: TaskIdResult
        """

        allParams = ['topo']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method saveCustomTopology" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/custom'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'










        if ('topo' in params):
            bodyParam = params['topo']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getL2Topology(self, **kwargs):
        """getL2Topology

        Args:

            vlanID, str: ID of VLAN (required)



        Returns: TopologyResult
        """

        allParams = ['vlanID']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getL2Topology" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/l2/{vlanID}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('vlanID' in params):
            replacement = str(self.apiClient.toPathValue(params['vlanID']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'vlanID' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TopologyResult')
        return responseObject




    def getL3TopologyForVrf(self, **kwargs):
        """getL3TopologyForVrf

        Args:

            vrfName, str: VRF Name (required)



        Returns: TopologyResult
        """

        allParams = ['vrfName']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getL3TopologyForVrf" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/l3/vrf/{vrfName}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('vrfName' in params):
            replacement = str(self.apiClient.toPathValue(params['vrfName']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'vrfName' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TopologyResult')
        return responseObject




    def getL3Topology(self, **kwargs):
        """getL3Topology

        Args:

            topologyType, str: Type of topology(OSPF,ISIS,etc) (required)



        Returns: TopologyResult
        """

        allParams = ['topologyType']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getL3Topology" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/l3/{topologyType}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('topologyType' in params):
            replacement = str(self.apiClient.toPathValue(params['topologyType']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'topologyType' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TopologyResult')
        return responseObject




    def getPhysicalTopology(self, **kwargs):
        """getPhysicalTopology

        Args:


        Returns: TopologyResult
        """

        allParams = []

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPhysicalTopology" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/topology/physical-topology'
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

        responseObject = self.apiClient.deserialize(response, 'TopologyResult')
        return responseObject






