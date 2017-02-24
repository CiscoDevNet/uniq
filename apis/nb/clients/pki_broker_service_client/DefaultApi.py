#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class DefaultApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient



    def getCertificateBriefList(self, **kwargs):
        """getCertificateBriefList

        Args:


        Returns: CertificateBriefListResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
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
        for (key, val) in list(params['kwargs'].items()):
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
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'multipart/form-data'


        if ('pkPassword' in params):
            queryParams['pkPassword'] = self.apiClient.toPathValue(params['pkPassword'])







        if ('certFileUpload' in params):
            files['certFileUpload'] = params['certFileUpload']

        if ('pkFileUpload' in params):
            files['pkFileUpload'] = params['pkFileUpload']




        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getDefaultCaPem(self, **kwargs):
        """getDefaultCaPem

        Args:

            id, str: Certificate ID (required)


            type, str: Certificate type (required)



        Returns:
        """

        allParams = ['id', 'type']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
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

        headerParams['Accept'] = 'application/json'
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
        for (key, val) in list(params['kwargs'].items()):
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

        headerParams['Accept'] = 'application/json'
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
        for (key, val) in list(params['kwargs'].items()):
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

        headerParams['Accept'] = 'application/json'
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
        for (key, val) in list(params['kwargs'].items()):
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
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'multipart/form-data'


        if ('p12Password' in params):
            queryParams['p12Password'] = self.apiClient.toPathValue(params['p12Password'])

        if ('pkPassword' in params):
            queryParams['pkPassword'] = self.apiClient.toPathValue(params['pkPassword'])







        if ('p12FileUpload' in params):
            files['p12FileUpload'] = params['p12FileUpload']




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
        for (key, val) in list(params['kwargs'].items()):
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
        for (key, val) in list(params['kwargs'].items()):
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
        for (key, val) in list(params['kwargs'].items()):
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
        for (key, val) in list(params['kwargs'].items()):
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

            certificateProxyStatus, CertificateProxyStatus: Enable/Disable proxy certificate (required)



        Returns: TaskIdResult
        """

        allParams = ['certificateProxyStatus']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
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
        for (key, val) in list(params['kwargs'].items()):
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
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'multipart/form-data'








        if ('certFileUpload' in params):
            files['certFileUpload'] = params['certFileUpload']




        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def pkiTrustPointListGet(self, **kwargs):
        """pkiTrustPointListGet

        Args:


        Returns: PkiTrustPointListResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
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
        for (key, val) in list(params['kwargs'].items()):
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
        for (key, val) in list(params['kwargs'].items()):
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
        for (key, val) in list(params['kwargs'].items()):
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
        for (key, val) in list(params['kwargs'].items()):
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
        for (key, val) in list(params['kwargs'].items()):
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
        for (key, val) in list(params['kwargs'].items()):
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
        for (key, val) in list(params['kwargs'].items()):
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
        for (key, val) in list(params['kwargs'].items()):
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
        for (key, val) in list(params['kwargs'].items()):
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
        for (key, val) in list(params['kwargs'].items()):
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
        for (key, val) in list(params['kwargs'].items()):
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




    def getDefaultCaPemChain(self, **kwargs):
        """getDefaultCaPemChain

        Args:

            id, str: Certificate ID (required)


            type, str: Certificate type (required)



        Returns:
        """

        allParams = ['id', 'type']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getDefaultCaPemChain" % key)
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

        headerParams['Accept'] = 'application/json'
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


    def getDefaultCaPemChain(self, **kwargs):
        """getDefaultCaPemChain

        Args:

            id, str: Certificate ID (required)


            type, str: Certificate type (required)



        Returns:
        """

        allParams = ['id', 'type']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getDefaultCaPemChain" % key)
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

        headerParams['Accept'] = 'application/json'
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



