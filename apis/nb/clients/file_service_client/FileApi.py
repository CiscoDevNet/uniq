#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class FileApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient



    def getNameSpaceList(self, **kwargs):
        """Returns list of available namespaces

        Args:

            scope, str: Authorization Scope for RBAC (required)



        Returns: NameSpaceListResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
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
        """Returns list of files under a specific namespace

        Args:

            nameSpace, str: A listing of fileId&#39;s (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: FileObjectListResult
        """

        allParams = ['nameSpace', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
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

        headerParams['Accept'] = 'application/json'
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




    def downLoadFile(self, **kwargs):
        """Downloads a file referred by the fileId

        Args:

            fileId, str: File Identification number (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns:
        """

        allParams = ['fileId', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
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
        #changed this manually from 'application/json' to 'multipart/form-data'
        headerParams['Content-Type'] = 'multipart/form-data'



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

        return response


    def deleteFile(self, **kwargs):
        """Deletes a file with the specified fileId

        Args:

            fileId, str: File Identification number (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: SuccessResult
        """

        allParams = ['fileId', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
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
        """Retrieves checksum for the file referred to by the fileId

        Args:

            fileId, str: File Identification number (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: SuccessResult
        """

        allParams = ['fileId', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
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
        """Uploads a new file within a specific nameSpace

        Args:

            nameSpace, str: Specify File&#39;s namespace,namespace is a grouping of multiple files (required)


            toEncrypt, bool: toEncrypt (required)


            scope, str: Authorization Scope for RBAC (required)


            fileUpload, :  (required)



        Returns: FileObjectResult
        """

        allParams = ['nameSpace', 'toEncrypt', 'scope', 'fileUpload']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
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


        if ('toEncrypt' in params):
            queryParams['toEncrypt'] = self.apiClient.toPathValue(params['toEncrypt'])



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
        """Updates an existing file within a specific nameSpace

        Args:

            nameSpace, str: Specify File&#39;s namespace,namespace is a grouping of multiple files (required)


            fileId, str: Specify File Identification number (required)


            scope, str: Authorization Scope for RBAC (required)


            fileUpload, :  (required)



        Returns: FileObjectResult
        """

        allParams = ['nameSpace', 'fileId', 'scope', 'fileUpload']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
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
        #changed this manually from 'application/json' to 'multipart/form-data'
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






