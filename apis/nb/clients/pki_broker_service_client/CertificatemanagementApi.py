#!/usr/bin/env python
#pylint: skip-file
"""
CertificatemanagementApi.py
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


class CertificatemanagementApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient



    def getCertificateBriefList(self, **kwargs):
        """getCertificateBriefList

        Args:

        Returns: CertificateBriefListResult
        """

        allParams = []

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getCertificateBriefList" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/certificate'
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

        responseObject = self.apiClient.deserialize(response, 'CertificateBriefListResult')
        return responseObject




    def importCertificate(self, **kwargs):
        """importCertificate

        Args:


            certFileUpload, file: Specify the name of Certificate file to upload (required)


            pkFileUpload, file: Specify the name of Private Key file to upload (required)


            pkPassword, str: Private Key Passsword (required)



        Returns: TaskIdResult

        """

        allParams = ['certFileUpload', 'pkFileUpload', 'pkPassword']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method importCertificate" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/certificate'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}

        bodyParam = {}

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'multipart/form-data'


        if ('pkPassword' in params):
            queryParams['pkPassword'] = self.apiClient.toPathValue(params['pkPassword'])


        if ('certFileUpload' in params):
            bodyParam['certFileUpload'] = params['certFileUpload']

        if ('pkFileUpload' in params):
            bodyParam['pkFileUpload'] = params['pkFileUpload']




        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)



        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')

        return responseObject




    def importCertificateP12(self, **kwargs):
        """importCertificateP12

        Args:


            p12FileUpload, file: Specify the name of PKCS#12 file to upload (required)


            p12Password, str: P12 Passsword (required)


            pkPassword, str: Private Key Passsword (required)



        Returns: TaskIdResult
        """

        allParams = ['p12FileUpload', 'p12Password', 'pkPassword']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method importCertificateP12" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/certificate-p12'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}

        bodyParam = {}

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'multipart/form-data'


        if ('p12Password' in params):
            queryParams['p12Password'] = self.apiClient.toPathValue(params['p12Password'])

        if ('pkPassword' in params):
            queryParams['pkPassword'] = self.apiClient.toPathValue(params['pkPassword'])







        if ('p12FileUpload' in params):
            bodyParam['p12FileUpload'] = params['p12FileUpload']





        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getCertificateCount(self, **kwargs):
        """getCertificateBriefList

        Args:



        Returns: CountResult
        """

        allParams = []

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getCertificateCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/certificate/count'
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




    def getCertificateBrief(self, **kwargs):
        """getCertificateBrief

        Args:


            certificateId, str: Certificate ID (required)



        Returns: CertificateBriefResult
        """

        allParams = ['certificateId']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getCertificateBrief" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/certificate/{certificateId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'







        if ('certificateId' in params):
            replacement = str(self.apiClient.toPathValue(params['certificateId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'certificateId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'CertificateBriefResult')
        return responseObject




    def getCertificateBriefListByRange(self, **kwargs):
        """getCertificateBriefList

        Args:


            startIndex, int: Index to start returning records from (required)


            recordsToReturn, int: Number of records to return (required)



        Returns: CertificateBriefListResult
        """

        allParams = ['startIndex', 'recordsToReturn']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getCertificateBriefListByRange" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/certificate/{startIndex}/{recordsToReturn}'
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

        responseObject = self.apiClient.deserialize(response, 'CertificateBriefListResult')
        return responseObject




    def getProxyCertificate(self, **kwargs):
        """getProxyCertificate

        Args:



        Returns: CertificateBriefResult
        """

        allParams = []

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getProxyCertificate" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/proxy-certificate'
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

        responseObject = self.apiClient.deserialize(response, 'CertificateBriefResult')
        return responseObject




    def updateProxyCertState(self, **kwargs):
        """updateProxyCertState

        Args:


            certificateProxyStatus, CertificateProxyStatus: certificateProxyStatus (required)




        Returns: TaskIdResult
        """

        allParams = ['certificateProxyStatus']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateProxyCertState" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/proxy-certificate'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'












        if ('certificateProxyStatus' in params):
            bodyParam = params['certificateProxyStatus']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def postProxyCertificate(self, **kwargs):
        """postProxyCertificate

        Args:


            certFileUpload, file: Specify the name of proxy certificate file to upload (required)



        Returns: TaskIdResult
        """

        allParams = ['certFileUpload']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method postProxyCertificate" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/proxy-certificate'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}

        bodyParam = {}

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'multipart/form-data'




        if ('certFileUpload' in params):
            bodyParam['certFileUpload'] = params['certFileUpload']




        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None


        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject






