#!/usr/bin/env python
#pylint: skip-file
"""
FileApi.py
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


class FileApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient



    def uploadFileWithInternalUploadUrl(self, **kwargs):
        """uploadFileWithInternalUploadUrl

        Args:

            internalUploadId, str: internalUploadId (required)


            fileUpload, :  (required)



        Returns: FileObjectResult
        """

        allParams = ['internalUploadId', 'fileUpload']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method uploadFileWithInternalUploadUrl" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/file/internalupload/{internalUploadId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('internalUploadId' in params):
            replacement = str(self.apiClient.toPathValue(params['internalUploadId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'internalUploadId' + '}',
                                                replacement)





        if ('fileUpload' in params):
            bodyParam = params['fileUpload']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'FileObjectResult')
        return responseObject




    def getNameSpaceList(self, **kwargs):
        """getNameSpaceList

        Args:

            scope, str: Authorization Scope for RBAC (required)



        Returns: NameSpaceListResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getNameSpaceList" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/file/namespace'
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

        responseObject = self.apiClient.deserialize(response, 'NameSpaceListResult')
        return responseObject




    def getFilesByNamespace(self, **kwargs):
        """getFilesByNamespace

        Args:

            nameSpace, str: A listing of fileId&#39;s (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: FileObjectListResult
        """

        allParams = ['nameSpace', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getFilesByNamespace" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/file/namespace/{nameSpace}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = ''
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']



        if ('nameSpace' in params):
            replacement = str(self.apiClient.toPathValue(params['nameSpace']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'nameSpace' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'FileObjectListResult')
        return responseObject




    def downloadFileWithOneTimeDownloadUrl(self, **kwargs):
        """downloadFileWithOneTimeDownloadUrl

        Args:

            onetimeDownloadId, str: URL pointing to the location of the file (required)



        Returns: object
        """

        allParams = ['onetimeDownloadId']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method downloadFileWithOneTimeDownloadUrl" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/file/onetimedownload/{onetimeDownloadId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/octet-stream'
        headerParams['Content-Type'] = 'application/json'






        if ('onetimeDownloadId' in params):
            replacement = str(self.apiClient.toPathValue(params['onetimeDownloadId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'onetimeDownloadId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'object')
        return responseObject




    def downloadFileWithTemporaryDownloadUrl(self, **kwargs):
        """Download file via timedDownloadId.

        Args:

            temporaryDownloadId, str: URL pointing to the location of the file (required)



        Returns: object
        """

        allParams = ['temporaryDownloadId']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method downloadFileWithTemporaryDownloadUrl" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/file/temporary/{temporaryDownloadId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/octet-stream'
        headerParams['Content-Type'] = 'application/json'






        if ('temporaryDownloadId' in params):
            replacement = str(self.apiClient.toPathValue(params['temporaryDownloadId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'temporaryDownloadId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'object')
        return responseObject




    def downLoadFile(self, **kwargs):
        """downloadFile

        Notes:
            This method has been modified. A parameter 'stream' is added to support the scenario
            that same api is called with different headers.


        Args:

            fileId, str: File Identification number (required)


            scope, str: Authorization Scope for RBAC (required)


            stream, bool: Return stream object.



        Returns: File content
        """

        allParams = ['fileId', 'scope', 'stream']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method downLoadFile" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/file/{fileId}'
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



        if ('fileId' in params):
            replacement = str(self.apiClient.toPathValue(params['fileId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'fileId' + '}',
                                                replacement)

        stream = False
        if ('stream' in params) and params['stream']:
            headerParams['Accept'] = 'application/octet-stream'
            headerParams['Content-Type'] = 'application/octet-stream'
            stream = params['stream']

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files, stream=stream)


        if not response:
            return None

        #responseObject = self.apiClient.deserialize(response, 'object')
        #return responseObject

        return response

    def deleteFile(self, **kwargs):
        """deleteFile

        Args:

            fileId, str: File Identification number (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: SuccessResult
        """

        allParams = ['fileId', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteFile" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/file/{fileId}'
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

        responseObject = self.apiClient.deserialize(response, 'SuccessResult')
        return responseObject




    def getChecksumOfFile(self, **kwargs):
        """getChecksumOfFile

        Args:

            fileId, str: File Identification number (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: SuccessResult
        """

        allParams = ['fileId', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getChecksumOfFile" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/file/{fileId}/checksum'
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

        responseObject = self.apiClient.deserialize(response, 'SuccessResult')
        return responseObject




    def uploadFile(self, **kwargs):
        """uploadFile

        Args:

            nameSpace, str: Specify File&#39;s namespace,namespace is a grouping of multiple files (required)


            scope, str: Authorization Scope for RBAC (required)


            fileUpload, :  (required)



        Returns: FileObjectResult
        """

        allParams = ['nameSpace', 'scope', 'fileUpload']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method uploadFile" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/file/{nameSpace}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'multipart/form-data'




        if ('scope' in params):
            headerParams['scope'] = params['scope']



        if ('nameSpace' in params):
            replacement = str(self.apiClient.toPathValue(params['nameSpace']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'nameSpace' + '}',
                                                replacement)





        if ('fileUpload' in params):
            bodyParam = params['fileUpload']


        postData = (formParams if formParams else bodyParam)
        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'FileObjectResult')
        return responseObject




    def updateFile(self, **kwargs):
        """updateFile

        Args:

            nameSpace, str: Specify File&#39;s namespace,namespace is a grouping of multiple files (required)


            fileId, str: Specify File Identification number (required)


            scope, str: Authorization Scope for RBAC (required)


            fileUpload, :  (required)



        Returns: FileObjectResult
        """

        allParams = ['nameSpace', 'fileId', 'scope', 'fileUpload']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateFile" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/file/{nameSpace}/{fileId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'multipart/form-data'




        if ('scope' in params):
            headerParams['scope'] = params['scope']



        if ('nameSpace' in params):
            replacement = str(self.apiClient.toPathValue(params['nameSpace']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'nameSpace' + '}',
                                                replacement)

        if ('fileId' in params):
            replacement = str(self.apiClient.toPathValue(params['fileId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'fileId' + '}',
                                                replacement)





        if ('fileUpload' in params):
            bodyParam = params['fileUpload']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'FileObjectResult')
        return responseObject






