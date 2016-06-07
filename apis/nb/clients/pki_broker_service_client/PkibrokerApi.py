#!/usr/bin/env python
#pylint: skip-file
"""
PkibrokerApi.py
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


class PkibrokerApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient



    def getDefaultCaPem(self, **kwargs):
        """getDefaultCaPem

        Args:

            id, str: Certificate ID (required)


            type, str: Certificate type (required)



        Returns:
        """

        allParams = ['id', 'type']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getDefaultCaPem" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/certificate-authority/ca/{id}/{type}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = ''
        headerParams['Content-Type'] = 'application/json'






        if ('id' in params):
            replacement = str(self.apiClient.toPathValue(params['id']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'id' + '}',
                                                replacement)

        if ('type' in params):
            replacement = str(self.apiClient.toPathValue(params['type']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'type' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)





    def legacyUpdateDefaultCaPem(self, **kwargs):
        """updateDefaultCaPem

        Args:

            id, str: Certificate ID (required)


            type, str: Certificate type (required)


            param, TrustpoolUpdateParam: param (required)



        Returns: TrustpoolUpdateStatusResult
        """

        allParams = ['id', 'type', 'param']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method legacyUpdateDefaultCaPem" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/certificate-authority/update/{id}/{type}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = ''
        headerParams['Content-Type'] = 'application/json'






        if ('id' in params):
            replacement = str(self.apiClient.toPathValue(params['id']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'id' + '}',
                                                replacement)

        if ('type' in params):
            replacement = str(self.apiClient.toPathValue(params['type']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'type' + '}',
                                                replacement)





        if ('param' in params):
            bodyParam = params['param']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TrustpoolUpdateStatusResult')
        return responseObject




    def updateDefaultCaPem(self, **kwargs):
        """updateDefaultCaPem

        Args:

            id, str: Certificate ID (required)


            type, str: Certificate type (required)


            param, TrustpoolUpdateParam: param (required)



        Returns: TrustpoolUpdateStatusResult
        """

        allParams = ['id', 'type', 'param']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateDefaultCaPem" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/certificate-authority/{id}/{type}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = ''
        headerParams['Content-Type'] = 'application/json'






        if ('id' in params):
            replacement = str(self.apiClient.toPathValue(params['id']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'id' + '}',
                                                replacement)

        if ('type' in params):
            replacement = str(self.apiClient.toPathValue(params['type']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'type' + '}',
                                                replacement)





        if ('param' in params):
            bodyParam = params['param']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TrustpoolUpdateStatusResult')
        return responseObject




    def pkiTrustPointListGet(self, **kwargs):
        """pkiTrustPointListGet

        Args:


        Returns: PkiTrustPointListResult
        """

        allParams = []

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method pkiTrustPointListGet" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/trust-point'
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

        responseObject = self.apiClient.deserialize(response, 'PkiTrustPointListResult')
        return responseObject




    def pkiTrustPointPost(self, **kwargs):
        """pkiTrustPointPost

        Args:

            pkiTrustPointInput, PkiTrustPoint: pkiTrustPointInput (required)



        Returns: TaskIdResult
        """

        allParams = ['pkiTrustPointInput']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method pkiTrustPointPost" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/trust-point'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'










        if ('pkiTrustPointInput' in params):
            bodyParam = params['pkiTrustPointInput']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def pkiTrustPointCount(self, **kwargs):
        """pkiTrustPointListGet

        Args:


        Returns: CountResult
        """

        allParams = []

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method pkiTrustPointCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/trust-point/count'
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




    def pkiTrustPointPkcs12Download(self, **kwargs):
        """pkiTrustPointPkcs12Download

        Args:

            trustPointId, str: Trust-point ID (required)


            token, str: Download token (required)



        Returns:
        """

        allParams = ['trustPointId', 'token']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method pkiTrustPointPkcs12Download" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/trust-point/pkcs12/{trustPointId}/{token}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('trustPointId' in params):
            replacement = str(self.apiClient.toPathValue(params['trustPointId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'trustPointId' + '}',
                                                replacement)

        if ('token' in params):
            replacement = str(self.apiClient.toPathValue(params['token']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'token' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)





    def pkiTrustPointGetByDeviceSN(self, **kwargs):
        """pkiTrustPointGetByDeviceSN

        Args:

            serialNumber, str: Device serial-number (required)



        Returns: PkiTrustPointResult
        """

        allParams = ['serialNumber']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method pkiTrustPointGetByDeviceSN" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/trust-point/serial-number/{serialNumber}'
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
            replacement = str(self.apiClient.toPathValue(params['serialNumber']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'serialNumber' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'PkiTrustPointResult')
        return responseObject




    def pkiTrustPointDeleteByDeviceSN(self, **kwargs):
        """pkiTrustPointDeleteByDeviceSN

        Args:

            serialNumber, str: Device serial-number (required)



        Returns: TaskIdResult
        """

        allParams = ['serialNumber']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method pkiTrustPointDeleteByDeviceSN" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/trust-point/serial-number/{serialNumber}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('serialNumber' in params):
            replacement = str(self.apiClient.toPathValue(params['serialNumber']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'serialNumber' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def pkiTrustPointListGetByRange(self, **kwargs):
        """getCertificateBriefList

        Args:

            startIndex, int: Index to start returning records from (required)


            recordsToReturn, int: Number of records to return (required)



        Returns: PkiTrustPointListResult
        """

        allParams = ['startIndex', 'recordsToReturn']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method pkiTrustPointListGetByRange" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/trust-point/{startIndex}/{recordsToReturn}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('startIndex' in params):
            replacement = str(self.apiClient.toPathValue(params['startIndex']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'startIndex' + '}',
                                                replacement)

        if ('recordsToReturn' in params):
            replacement = str(self.apiClient.toPathValue(params['recordsToReturn']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'recordsToReturn' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'PkiTrustPointListResult')
        return responseObject




    def pkiTrustPointGet(self, **kwargs):
        """pkiTrustPointGet

        Args:

            trustPointId, str: Trust-point ID (required)



        Returns: PkiTrustPointResult
        """

        allParams = ['trustPointId']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method pkiTrustPointGet" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/trust-point/{trustPointId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('trustPointId' in params):
            replacement = str(self.apiClient.toPathValue(params['trustPointId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'trustPointId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'PkiTrustPointResult')
        return responseObject




    def pkiTrustPointPush(self, **kwargs):
        """pkiTrustPointPush

        Args:

            trustPointId, str: Trust-point ID (required)



        Returns: TaskIdResult
        """

        allParams = ['trustPointId']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method pkiTrustPointPush" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/trust-point/{trustPointId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('trustPointId' in params):
            replacement = str(self.apiClient.toPathValue(params['trustPointId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'trustPointId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def pkiTrustPointDelete(self, **kwargs):
        """pkiTrustPointDelete

        Args:

            trustPointId, str: Trust-point ID (required)



        Returns: TaskIdResult
        """

        allParams = ['trustPointId']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method pkiTrustPointDelete" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/trust-point/{trustPointId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('trustPointId' in params):
            replacement = str(self.apiClient.toPathValue(params['trustPointId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'trustPointId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def pkiTrustPointConfigGet(self, **kwargs):
        """pkiTrustPointConfigGet

        Args:

            trustPointId, str: Trust-point ID (required)



        Returns: PkiTrustPointConfigResult
        """

        allParams = ['trustPointId']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method pkiTrustPointConfigGet" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/trust-point/{trustPointId}/config'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('trustPointId' in params):
            replacement = str(self.apiClient.toPathValue(params['trustPointId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'trustPointId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'PkiTrustPointConfigResult')
        return responseObject




    def checkPKCS12Downloaded(self, **kwargs):
        """checkPKCS12Downloaded

        Args:

            trustPointId, str: Trust-point ID (required)


            scope, str: Authorization Scope for RBAC (required)


            username, str: requestUsername (required)



        Returns: SuccessResult
        """

        allParams = ['trustPointId', 'scope', 'username']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method checkPKCS12Downloaded" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/trust-point/{trustPointId}/downloaded'
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

        if ('username' in params):
            headerParams['username'] = params['username']



        if ('trustPointId' in params):
            replacement = str(self.apiClient.toPathValue(params['trustPointId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'trustPointId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SuccessResult')
        return responseObject






