#!/usr/bin/env python
#pylint: skip-file
"""
PolicyApi.py
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


class PolicyApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient



    def getFilterPolicies(self, **kwargs):
        """Retrieves policies based on a given filter

        Args:

            policyScope, str: Retrieve policies for a given scope (required)


            scopeWirelessSegment, str: Retrieve policies for a given wireless segment, within a policyScope (policyScope is mandatory for this) (required)


            applicationId, str: Retrieve policies for a given Resource Application Id (required)


            offset, str: Starting index of the resources (1 based) (required)


            limit, str: Number of resources to return (required)



        Returns: PolicyListResult
        """

        allParams = ['policyScope', 'scopeWirelessSegment', 'applicationId', 'offset', 'limit']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getFilterPolicies" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('policyScope' in params):
            queryParams['policyScope'] = self.apiClient.toPathValue(params['policyScope'])

        if ('scopeWirelessSegment' in params):
            queryParams['scopeWirelessSegment'] = self.apiClient.toPathValue(params['scopeWirelessSegment'])

        if ('applicationId' in params):
            queryParams['applicationId'] = self.apiClient.toPathValue(params['applicationId'])

        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])

        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])










        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'PolicyListResult')
        return responseObject




    def update(self, **kwargs):
        """Update policy(s)

        Args:

            scheduleAt, str: Epoch Time (The number of milli-seconds since January 1 1970 UTC) at which the policy should be scheduled (Optional)  (required)


            scheduleDesc, str: Custom Description (Optional) (required)


            scheduleOrigin, str: Originator of this call (Optional) (required)


            policyList, list[Policy]: Policy Object (required)



        Returns: TaskIdResult
        """

        allParams = ['scheduleAt', 'scheduleDesc', 'scheduleOrigin', 'policyList']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method update" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy'
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









        if ('policyList' in params):
            bodyParam = params['policyList']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def add(self, **kwargs):
        """Create policy(s)

        Args:

            scheduleAt, str: Epoch Time (The number of milli-seconds since January 1 1970 UTC) at which the policy should be scheduled (Optional)  (required)


            scheduleDesc, str: Custom Description (Optional) (required)


            scheduleOrigin, str: Originator of this call (Optional) (required)


            policyList, list[Policy]: Policy Object (required)



        Returns: TaskIdResult
        """

        allParams = ['scheduleAt', 'scheduleDesc', 'scheduleOrigin', 'policyList']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method add" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy'
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









        if ('policyList' in params):
            bodyParam = params['policyList']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def deleteFilterPolicies(self, **kwargs):
        """Delete policies based on a given filter

        Args:

            policyScope, str: Delete policies for a given scope (required)


            scopeWirelessSegment, str: Delete policies for a given wireless segment, within a policyScope (policyScope is mandatory for this) (required)



        Returns: TaskIdResult
        """

        allParams = ['policyScope', 'scopeWirelessSegment']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteFilterPolicies" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('policyScope' in params):
            queryParams['policyScope'] = self.apiClient.toPathValue(params['policyScope'])

        if ('scopeWirelessSegment' in params):
            queryParams['scopeWirelessSegment'] = self.apiClient.toPathValue(params['scopeWirelessSegment'])










        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getCount(self, **kwargs):
        """Return total count of policies

        Args:


        Returns: CountResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy/count'
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




    def getPolicyDiff(self, **kwargs):
        """Retrieves the policy diff

        Args:

            version, str: Retrieve policy diffs for the given version (required)


            policyScope, str: Retrieve policy diffs for the given scope (required)


            scopeWirelessSegment, str: Retrieve policy diffs for the given scopeWirelessSegment (required)



        Returns: VersionDiffResult
        """

        allParams = ['version', 'policyScope', 'scopeWirelessSegment']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPolicyDiff" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy/diff'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('version' in params):
            queryParams['version'] = self.apiClient.toPathValue(params['version'])

        if ('policyScope' in params):
            queryParams['policyScope'] = self.apiClient.toPathValue(params['policyScope'])

        if ('scopeWirelessSegment' in params):
            queryParams['scopeWirelessSegment'] = self.apiClient.toPathValue(params['scopeWirelessSegment'])










        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'VersionDiffResult')
        return responseObject




    def addPolicyDiff(self, **kwargs):
        """Adds the policy diff

        Args:

            versionDiffDTO, VersionDiffDTO: VersionDiff (required)



        Returns: TaskIdResult
        """

        allParams = ['versionDiffDTO']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addPolicyDiff" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy/diff'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'










        if ('versionDiffDTO' in params):
            bodyParam = params['versionDiffDTO']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getFlows(self, **kwargs):
        """Retrieves flows with search criteria

        Args:

            offset, str: Starting index of the resources (1 based) (required)


            limit, str: Number of resources to return (required)



        Returns: FlowListResult
        """

        allParams = ['offset', 'limit']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getFlows" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy/flow'
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
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])

        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])










        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'FlowListResult')
        return responseObject




    def addFlow(self, **kwargs):
        """Creates a new traffic flow for which qos policies will be applied

        Args:

            flowDTO, FlowDTO: flowDTO (required)



        Returns: FlowIdResult
        """

        allParams = ['flowDTO']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addFlow" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy/flow'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'










        if ('flowDTO' in params):
            bodyParam = params['flowDTO']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'FlowIdResult')
        return responseObject




    def deleteFlowsByClientReference(self, **kwargs):
        """Deletes flows based on clientReference prefix

        Args:

            clientReference, str: clientReference (required)



        Returns: TaskIdResult
        """

        allParams = ['clientReference']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteFlowsByClientReference" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy/flow'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('clientReference' in params):
            queryParams['clientReference'] = self.apiClient.toPathValue(params['clientReference'])










        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getPolicyFlowSetting(self, **kwargs):
        """Retrieves dynamic policy flow setting

        Args:


        Returns: PolicyFlowSettingResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPolicyFlowSetting" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy/flow/setting'
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

        responseObject = self.apiClient.deserialize(response, 'PolicyFlowSettingResult')
        return responseObject




    def updateFlowPolicySetting(self, **kwargs):
        """Update the dynamic policy flow setting. This setting will be used to allow/disallow dynamic flows /policy/flow requests.

        Args:

            policyFlowSettingDTO, PolicyFlowSettingDTO: policyFlowSettingDTO (required)



        Returns: TaskIdResult
        """

        allParams = ['policyFlowSettingDTO']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateFlowPolicySetting" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy/flow/setting'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'










        if ('policyFlowSettingDTO' in params):
            bodyParam = params['policyFlowSettingDTO']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getFlow(self, **kwargs):
        """Retrieves a flow by its id

        Args:

            id, str: id (required)



        Returns: FlowResult
        """

        allParams = ['id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getFlow" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy/flow/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'FlowResult')
        return responseObject




    def deleteFlow(self, **kwargs):
        """Delete a policy for the flow by its id

        Args:

            id, str: id (required)



        Returns: TaskIdResult
        """

        allParams = ['id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteFlow" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy/flow/{id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

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

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getPolicyStatus(self, **kwargs):
        """Retrieves policy statuses based on a given filter

        Args:

            networkDeviceId, str: Retrieve policies for a given networkDeviceId (required)


            policyScope, str: Retrieve policies for a given scope (required)


            offset, str: Starting index of the resources (1 based) (required)


            limit, str: Number of resources to return (Use smaller limit value for better response times. Max 50) (required)



        Returns: PolicyStatusListResult
        """

        allParams = ['networkDeviceId', 'policyScope', 'offset', 'limit']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPolicyStatus" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy/status'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('networkDeviceId' in params):
            queryParams['networkDeviceId'] = self.apiClient.toPathValue(params['networkDeviceId'])

        if ('policyScope' in params):
            queryParams['policyScope'] = self.apiClient.toPathValue(params['policyScope'])

        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])

        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])










        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'PolicyStatusListResult')
        return responseObject




    def getCountByPolicyScope(self, **kwargs):
        """Retrieves count of policy status(es) based on a given policyScope &amp; scopeWirelessSegment

        Args:

            policyScope, str: Retrieve count of policy status(es) based on a given policyScope (required)


            scopeWirelessSegment, str: Retrieve count of policy status(es) based on a given scopeWirelessSegment (required)



        Returns: CountResult
        """

        allParams = ['policyScope', 'scopeWirelessSegment']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getCountByPolicyScope" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy/status/count'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('policyScope' in params):
            queryParams['policyScope'] = self.apiClient.toPathValue(params['policyScope'])

        if ('scopeWirelessSegment' in params):
            queryParams['scopeWirelessSegment'] = self.apiClient.toPathValue(params['scopeWirelessSegment'])










        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'CountResult')
        return responseObject




    def getPolicyStatusSummary(self, **kwargs):
        """Retrieves policy statuses summary based on a given filter

        Args:

            policyScope, str: Retrieve policy status(es) for a given scope (required)


            offset, str: Starting index of the resources (1 based) (required)


            limit, str: Number of resources to return (Use smaller limit value for better response times. Max 50) (required)



        Returns: PolicyStatusListResult
        """

        allParams = ['policyScope', 'offset', 'limit']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPolicyStatusSummary" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy/status/summary'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('policyScope' in params):
            queryParams['policyScope'] = self.apiClient.toPathValue(params['policyScope'])

        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])

        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])










        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'PolicyStatusListResult')
        return responseObject




    def getPolicyTags(self, **kwargs):
        """Retrieves policy tags

        Args:

            policyTag, str: policyTag search substring (required)


            filterOperation, str: type of search (startsWith, endsWith, contains (required)



        Returns: PolicyTagListResult
        """

        allParams = ['policyTag', 'filterOperation']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPolicyTags" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy/tag'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('policyTag' in params):
            queryParams['policyTag'] = self.apiClient.toPathValue(params['policyTag'])

        if ('filterOperation' in params):
            queryParams['filterOperation'] = self.apiClient.toPathValue(params['filterOperation'])










        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'PolicyTagListResult')
        return responseObject




    def addPolicyTag(self, **kwargs):
        """Create a policy tag

        Args:

            policyTagDTO, PolicyTagDTO: policyTagDTO (required)



        Returns: TaskIdResult
        """

        allParams = ['policyTagDTO']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addPolicyTag" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy/tag'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'










        if ('policyTagDTO' in params):
            bodyParam = params['policyTagDTO']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def deletePolicyTag(self, **kwargs):
        """Delete a policy tag.

        Args:

            policyTag, str: Policy Tag (required)



        Returns: TaskIdResult
        """

        allParams = ['policyTag']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deletePolicyTag" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy/tag'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('policyTag' in params):
            queryParams['policyTag'] = self.apiClient.toPathValue(params['policyTag'])










        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getPolicyTagAssociation(self, **kwargs):
        """Retrieves network device ids that have the policy tag

        Args:

            policyTag, str: Policy Tag (required)


            networkDeviceId, str: Network device Id (required)


            offset, str: Starting index of the resources (1 based) (required)


            limit, str: Number of resources to return (required)



        Returns: PolicyTagAssociationListResult
        """

        allParams = ['policyTag', 'networkDeviceId', 'offset', 'limit']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPolicyTagAssociation" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy/tag/association'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('policyTag' in params):
            queryParams['policyTag'] = self.apiClient.toPathValue(params['policyTag'])

        if ('networkDeviceId' in params):
            queryParams['networkDeviceId'] = self.apiClient.toPathValue(params['networkDeviceId'])

        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])

        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])










        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'PolicyTagAssociationListResult')
        return responseObject




    def addPolicyTagAssociation(self, **kwargs):
        """Add a policy tag to network devices.

        Args:

            policyTagAssociationDTO, PolicyTagAssociationDTO: policyTagAssociationDTO (required)



        Returns: TaskIdResult
        """

        allParams = ['policyTagAssociationDTO']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addPolicyTagAssociation" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy/tag/association'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'










        if ('policyTagAssociationDTO' in params):
            bodyParam = params['policyTagAssociationDTO']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def deletePolicyTagAssociation(self, **kwargs):
        """Remove a policy tag from network device.

        Args:

            policyTag, str: Policy Tag (required)


            networkDeviceId, str: NetworkDeviceId (required)



        Returns: TaskIdResult
        """

        allParams = ['policyTag', 'networkDeviceId']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deletePolicyTagAssociation" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy/tag/association'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('policyTag' in params):
            queryParams['policyTag'] = self.apiClient.toPathValue(params['policyTag'])

        if ('networkDeviceId' in params):
            queryParams['networkDeviceId'] = self.apiClient.toPathValue(params['networkDeviceId'])










        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getPolicyTagsCount(self, **kwargs):
        """Retrieves the number of policy tags

        Args:


        Returns: CountResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPolicyTagsCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy/tag/count'
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




    def getPolicyVersionNumbers(self, **kwargs):
        """Retrieves the policy version numbers

        Args:

            policyScope, str: Retrieve policy version numbers for the given scope (required)


            scopeWirelessSegment, str: Retrieve policy version numbers for the given scopeWirelessSegment (required)


            offset, str: Starting index of the resources (1 based) (required)


            limit, str: Number of resources to return (required)



        Returns: PolicyVersionNumberListResult
        """

        allParams = ['policyScope', 'scopeWirelessSegment', 'offset', 'limit']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPolicyVersionNumbers" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy/version'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('policyScope' in params):
            queryParams['policyScope'] = self.apiClient.toPathValue(params['policyScope'])

        if ('scopeWirelessSegment' in params):
            queryParams['scopeWirelessSegment'] = self.apiClient.toPathValue(params['scopeWirelessSegment'])

        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])

        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])










        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'PolicyVersionNumberListResult')
        return responseObject




    def getPolicyVersionNumbersCount(self, **kwargs):
        """Retrieves the count of policy version numbers

        Args:

            policyScope, str: Retrieve the count of policy version numbers for the given scope (required)


            scopeWirelessSegment, str: Retrieve the count of policy version numbers for the given scopeWirelessSegment (required)



        Returns: CountResult
        """

        allParams = ['policyScope', 'scopeWirelessSegment']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPolicyVersionNumbersCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy/version/count'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('policyScope' in params):
            queryParams['policyScope'] = self.apiClient.toPathValue(params['policyScope'])

        if ('scopeWirelessSegment' in params):
            queryParams['scopeWirelessSegment'] = self.apiClient.toPathValue(params['scopeWirelessSegment'])










        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'CountResult')
        return responseObject




    def get(self, **kwargs):
        """Retrieves a policy based on its id

        Args:

            id, str: id (required)



        Returns: PolicyResult
        """

        allParams = ['id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'PolicyResult')
        return responseObject




    def delete(self, **kwargs):
        """Deletes a policy by its id

        Args:

            id, str: id (required)



        Returns: TaskIdResult
        """

        allParams = ['id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method delete" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/policy/{id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

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

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject






