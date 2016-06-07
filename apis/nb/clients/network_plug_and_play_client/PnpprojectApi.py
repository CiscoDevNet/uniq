#!/usr/bin/env python
#pylint: skip-file
"""
PnpprojectApi.py
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


class PnpprojectApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient



    def getPnpSiteByRange(self, **kwargs):
        """Retrieves a list of projects

        Args:

            siteName, str: Project Name (required)


            state, str: State of a project.Allowed states are PRE-PROVISIONED,IN_PROGRESS,ERROR,PROVISIONED. (required)


            provisionedOn, str: Provisioned date. (required)


            provisionedBy, str: User who provisioned the project. (required)


            sortBy, str: Sort response based on field (required)


            order, str: Order response in ascending (asc) or descending (des) order (required)


            offset, int: Starting index of the response. Minimum value is 1 (required)


            limit, int: Limit the number of responses. Maximum value supported is 500. Minimum value is 1 (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: ZtdSiteListResult
        """

        allParams = ['siteName', 'state', 'provisionedOn', 'provisionedBy', 'sortBy', 'order', 'offset', 'limit', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPnpSiteByRange" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-project'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('siteName' in params):
            queryParams['siteName'] = self.apiClient.toPathValue(params['siteName'])

        if ('state' in params):
            queryParams['state'] = self.apiClient.toPathValue(params['state'])

        if ('provisionedOn' in params):
            queryParams['provisionedOn'] = self.apiClient.toPathValue(params['provisionedOn'])

        if ('provisionedBy' in params):
            queryParams['provisionedBy'] = self.apiClient.toPathValue(params['provisionedBy'])

        if ('sortBy' in params):
            queryParams['sortBy'] = self.apiClient.toPathValue(params['sortBy'])

        if ('order' in params):
            queryParams['order'] = self.apiClient.toPathValue(params['order'])

        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])

        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])



        if ('scope' in params):
            headerParams['scope'] = params['scope']








        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ZtdSiteListResult')
        return responseObject




    def updatePnpSite(self, **kwargs):
        """Updates a project with its ID

        Args:

            project, list[ZtdSite]: PnP project. Site ID is mandatory (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['project', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updatePnpSite" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-project'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']







        if ('project' in params):
            bodyParam = params['project']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def createPnpSite(self, **kwargs):
        """Creates a new project

        Args:

            project, list[ZtdSite]: PnP project. Project name is mandatory. (required)


            source, str: Project ID to clone from. Only the new project name is required in the request body for clone (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['project', 'source', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createPnpSite" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-project'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('source' in params):
            queryParams['source'] = self.apiClient.toPathValue(params['source'])



        if ('scope' in params):
            headerParams['scope'] = params['scope']







        if ('project' in params):
            bodyParam = params['project']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getPnpSiteCount(self, **kwargs):
        """Retrieves a count of projects

        Args:

            siteName, str: Project Name (required)


            state, str: State of a project.Allowed states are PRE_PROVISIONED, IN_PROGRESS, ERROR, PROVISIONED. (required)


            provisionedOn, str: Provisioned date. (required)


            provisionedBy, str: User who provisioned the project. (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: CountResult
        """

        allParams = ['siteName', 'state', 'provisionedOn', 'provisionedBy', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPnpSiteCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-project/count'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('siteName' in params):
            queryParams['siteName'] = self.apiClient.toPathValue(params['siteName'])

        if ('state' in params):
            queryParams['state'] = self.apiClient.toPathValue(params['state'])

        if ('provisionedOn' in params):
            queryParams['provisionedOn'] = self.apiClient.toPathValue(params['provisionedOn'])

        if ('provisionedBy' in params):
            queryParams['provisionedBy'] = self.apiClient.toPathValue(params['provisionedBy'])



        if ('scope' in params):
            headerParams['scope'] = params['scope']








        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'CountResult')
        return responseObject




    def exportPnpSitesAndDevices(self, **kwargs):
        """Retrieves the projects and their associated rules in a file of the given format

        Args:

            format, str: Format of the file. Currently only csv is supported (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: Void
        """

        allParams = ['format', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method exportPnpSitesAndDevices" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-project/seed-file'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('format' in params):
            queryParams['format'] = self.apiClient.toPathValue(params['format'])



        if ('scope' in params):
            headerParams['scope'] = params['scope']








        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Void')
        return responseObject




    def importPnpSitesAndDevices(self, **kwargs):
        """Imports projects and associated rules in bulk

        Args:

            seedFile, file: Seed file (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['seedFile', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method importPnpSitesAndDevices" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-project/seed-file'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = {}

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'multipart/form-data'




        if ('scope' in params):
            headerParams['scope'] = params['scope']





        if ('seedFile' in params):
            bodyParam['seedFile'] = params['seedFile']




        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getAllPnpBulkImportJobs(self, **kwargs):
        """Retrieves the status of previous import jobs

        Args:

            scope, str: Authorization Scope for RBAC (required)



        Returns: ZtdBulkStatusListResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAllPnpBulkImportJobs" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-project/seed-file/status'
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








        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ZtdBulkStatusListResult')
        return responseObject




    def getPnpBulkStatus(self, **kwargs):
        """Retrieves the status of an import job with its ID

        Args:

            importId, str: Import ID (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: ZtdBulkStatusResult
        """

        allParams = ['importId', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPnpBulkStatus" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-project/seed-file/{importId}/status'
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



        if ('importId' in params):
            replacement = str(self.apiClient.toPathValue(params['importId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'importId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ZtdBulkStatusResult')
        return responseObject




    def getPnpBulkReport(self, **kwargs):
        """Retrieves the report of an import job with its ID

        Args:

            importId, str: Import ID (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: Void
        """

        allParams = ['importId', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPnpBulkReport" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-project/seed-file/{importId}/status/report'
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



        if ('importId' in params):
            replacement = str(self.apiClient.toPathValue(params['importId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'importId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Void')
        return responseObject




    def getPnpTemplate(self, **kwargs):
        """Retrieves a template file for an import job

        Args:

            format, str: Format of the file. Currently only csv is supported (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: Void
        """

        allParams = ['format', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPnpTemplate" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-project/template-file'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('format' in params):
            queryParams['format'] = self.apiClient.toPathValue(params['format'])



        if ('scope' in params):
            headerParams['scope'] = params['scope']








        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Void')
        return responseObject




    def getPnpSiteById(self, **kwargs):
        """Retrieves a project with its ID

        Args:

            projectId, str: Project ID (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: ZtdSiteResult
        """

        allParams = ['projectId', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPnpSiteById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-project/{projectId}'
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



        if ('projectId' in params):
            replacement = str(self.apiClient.toPathValue(params['projectId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'projectId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ZtdSiteResult')
        return responseObject




    def deletePnpSiteByID(self, **kwargs):
        """Deletes a project with its ID

        Args:

            projectId, str: Project ID (required)


            deleteRule, int: Delete project rules (true) or not (false) (required)


            deleteDevice, int: Delete project devices (true) or not (false) (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['projectId', 'deleteRule', 'deleteDevice', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deletePnpSiteByID" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-project/{projectId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('deleteRule' in params):
            queryParams['deleteRule'] = self.apiClient.toPathValue(params['deleteRule'])

        if ('deleteDevice' in params):
            queryParams['deleteDevice'] = self.apiClient.toPathValue(params['deleteDevice'])



        if ('scope' in params):
            headerParams['scope'] = params['scope']



        if ('projectId' in params):
            replacement = str(self.apiClient.toPathValue(params['projectId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'projectId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getPnpSiteDevicesBySiteNameAndRange(self, **kwargs):
        """Retrieves a list of devices under a given project

        Args:

            projectId, str: Project ID (required)


            serialNumber, str: Serial number (required)


            productId, str: Product ID (required)


            hostName, str: Host name (required)


            pkiEnabled, str: Device certificate provisioned (true) or not (false) (required)


            state, str: State of device. PENDING, PROVISIONED. Accepts a list of states (required)


            authStatus, str: Authentication status of device: authenticated, error, unsupported (required)


            startLastStateTransitionTime, str: Start of last state transition time (format: yyyy-MM-dd HH:mm:ss) (required)


            endLastStateTransitionTime, str: End of last state transition time (format: yyyy-MM-dd HH:mm:ss) (required)


            sortBy, str: Sort response based on field (required)


            order, str: Order response in ascending (asc) or descending (des) order (required)


            offset, int: Starting index of the response. Minimum value is 1 (required)


            limit, int: Limit the number of responses. Maximum value supported is 500. Minimum value is 1 (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: ZtdSiteDeviceListResult
        """

        allParams = ['projectId', 'serialNumber', 'productId', 'hostName', 'pkiEnabled', 'state', 'authStatus', 'startLastStateTransitionTime', 'endLastStateTransitionTime', 'sortBy', 'order', 'offset', 'limit', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPnpSiteDevicesBySiteNameAndRange" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-project/{projectId}/device'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('serialNumber' in params):
            queryParams['serialNumber'] = self.apiClient.toPathValue(params['serialNumber'])

        if ('productId' in params):
            queryParams['productId'] = self.apiClient.toPathValue(params['productId'])

        if ('hostName' in params):
            queryParams['hostName'] = self.apiClient.toPathValue(params['hostName'])

        if ('pkiEnabled' in params):
            queryParams['pkiEnabled'] = self.apiClient.toPathValue(params['pkiEnabled'])

        if ('state' in params):
            queryParams['state'] = self.apiClient.toPathValue(params['state'])

        if ('authStatus' in params):
            queryParams['authStatus'] = self.apiClient.toPathValue(params['authStatus'])

        if ('startLastStateTransitionTime' in params):
            queryParams['startLastStateTransitionTime'] = self.apiClient.toPathValue(params['startLastStateTransitionTime'])

        if ('endLastStateTransitionTime' in params):
            queryParams['endLastStateTransitionTime'] = self.apiClient.toPathValue(params['endLastStateTransitionTime'])

        if ('sortBy' in params):
            queryParams['sortBy'] = self.apiClient.toPathValue(params['sortBy'])

        if ('order' in params):
            queryParams['order'] = self.apiClient.toPathValue(params['order'])

        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])

        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])



        if ('scope' in params):
            headerParams['scope'] = params['scope']



        if ('projectId' in params):
            replacement = str(self.apiClient.toPathValue(params['projectId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'projectId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ZtdSiteDeviceListResult')
        return responseObject




    def updatePnpSiteDevice(self, **kwargs):
        """Updates a device under a given project with its ID

        Args:

            projectId, str: Project ID (required)


            rule, list[ZtdRule]: PnP rule. Rule ID is mandatory (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['projectId', 'rule', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updatePnpSiteDevice" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-project/{projectId}/device'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']



        if ('projectId' in params):
            replacement = str(self.apiClient.toPathValue(params['projectId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'projectId' + '}',
                                                replacement)





        if ('rule' in params):
            bodyParam = params['rule']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def createPnpSiteDevice(self, **kwargs):
        """Creates a new device under a given project

        Args:

            projectId, str: Project ID (required)


            rule, list[ZtdRule]: PnP rule. Host name, Platform ID are mandatory (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['projectId', 'rule', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createPnpSiteDevice" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-project/{projectId}/device'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']



        if ('projectId' in params):
            replacement = str(self.apiClient.toPathValue(params['projectId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'projectId' + '}',
                                                replacement)





        if ('rule' in params):
            bodyParam = params['rule']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def downloadPnpBootStrap(self, **kwargs):
        """Retrieves the device bootstrap file under a given project

        Args:

            projectId, str: Project ID (required)


            fileId, str: File ID (required)



        Returns: Void
        """

        allParams = ['projectId', 'fileId']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method downloadPnpBootStrap" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-project/{projectId}/device-bootstrap/{fileId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('projectId' in params):
            replacement = str(self.apiClient.toPathValue(params['projectId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'projectId' + '}',
                                                replacement)

        if ('fileId' in params):
            replacement = str(self.apiClient.toPathValue(params['fileId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'fileId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Void')
        return responseObject




    def getPnpSiteDeviceCount(self, **kwargs):
        """Retrieves a count of devices under a given project

        Args:

            projectId, str: Project ID (required)


            serialNumber, str: Serial number (required)


            productId, str: Product ID (required)


            hostName, str: Host name (required)


            pkiEnabled, str: Device certificate provisioned (true) or not (false) (required)


            state, str: State of device. PENDING, PROVISIONED. Accepts a list of states (required)


            authStatus, str: Authentication status of device: authenticated, error, unsupported (required)


            startLastStateTransitionTime, str: Start of last state transition time (format: yyyy-MM-dd HH:mm:ss) (required)


            endLastStateTransitionTime, str: End of last state transition time (format: yyyy-MM-dd HH:mm:ss) (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: CountResult
        """

        allParams = ['projectId', 'serialNumber', 'productId', 'hostName', 'pkiEnabled', 'state', 'authStatus', 'startLastStateTransitionTime', 'endLastStateTransitionTime', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPnpSiteDeviceCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-project/{projectId}/device/count'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('serialNumber' in params):
            queryParams['serialNumber'] = self.apiClient.toPathValue(params['serialNumber'])

        if ('productId' in params):
            queryParams['productId'] = self.apiClient.toPathValue(params['productId'])

        if ('hostName' in params):
            queryParams['hostName'] = self.apiClient.toPathValue(params['hostName'])

        if ('pkiEnabled' in params):
            queryParams['pkiEnabled'] = self.apiClient.toPathValue(params['pkiEnabled'])

        if ('state' in params):
            queryParams['state'] = self.apiClient.toPathValue(params['state'])

        if ('authStatus' in params):
            queryParams['authStatus'] = self.apiClient.toPathValue(params['authStatus'])

        if ('startLastStateTransitionTime' in params):
            queryParams['startLastStateTransitionTime'] = self.apiClient.toPathValue(params['startLastStateTransitionTime'])

        if ('endLastStateTransitionTime' in params):
            queryParams['endLastStateTransitionTime'] = self.apiClient.toPathValue(params['endLastStateTransitionTime'])



        if ('scope' in params):
            headerParams['scope'] = params['scope']



        if ('projectId' in params):
            replacement = str(self.apiClient.toPathValue(params['projectId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'projectId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'CountResult')
        return responseObject




    def deletePnpSiteDeviceById(self, **kwargs):
        """Deletes a device under a given project with its ID

        Args:

            projectId, str: Project ID (required)


            deviceId, str: Device ID (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['projectId', 'deviceId', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deletePnpSiteDeviceById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-project/{projectId}/device/{deviceId}'
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



        if ('projectId' in params):
            replacement = str(self.apiClient.toPathValue(params['projectId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'projectId' + '}',
                                                replacement)

        if ('deviceId' in params):
            replacement = str(self.apiClient.toPathValue(params['deviceId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'deviceId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject






