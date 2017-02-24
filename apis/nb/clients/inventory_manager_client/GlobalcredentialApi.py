#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class GlobalcredentialApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getGlobalCredential(self, **kwargs):
        """Retrieves global credential for the given credential sub type

        Args:
            
            credentialSubType, str: Credential type as CLI / SNMPV2_READ_COMMUNITY / SNMPV2_WRITE_COMMUNITY / SNMPV3 (required)
            
            
        
        Returns: GlobalCredentialListResult
        """

        allParams = ['credentialSubType']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getGlobalCredential" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/global-credential'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('credentialSubType' in params):
            queryParams['credentialSubType'] = self.apiClient.toPathValue(params['credentialSubType'])
        

        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GlobalCredentialListResult')
        return responseObject
        
        
        
    
    def updateCliCredential(self, **kwargs):
        """Updates global CLI credential

        Args:
            
            globalCredentialNio, CLICredentialDTO: CLI credentials (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['globalCredentialNio']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateCliCredential" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/global-credential/cli'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('globalCredentialNio' in params):
            bodyParam = params['globalCredentialNio']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def addCliCredential(self, **kwargs):
        """Creates global CLI credential

        Args:
            
            globalCredentialNioList, list[CLICredentialDTO]: List of CLI credentials (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['globalCredentialNioList']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addCliCredential" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/global-credential/cli'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('globalCredentialNioList' in params):
            bodyParam = params['globalCredentialNioList']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def updateSnmpReadCommunity(self, **kwargs):
        """Updates global SNMP read community

        Args:
            
            globalCredentialNio, SNMPv2ReadCommunityDTO: SNMP read community details (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['globalCredentialNio']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateSnmpReadCommunity" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/global-credential/snmpv2-read-community'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('globalCredentialNio' in params):
            bodyParam = params['globalCredentialNio']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def addSnmpReadCommunity(self, **kwargs):
        """Creates global SNMP read community

        Args:
            
            globalCredentialNioList, List[SNMPv2ReadCommunityDTO]: List of SNMP read communities (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['globalCredentialNioList']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addSnmpReadCommunity" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/global-credential/snmpv2-read-community'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('globalCredentialNioList' in params):
            bodyParam = params['globalCredentialNioList']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def updateSnmpWriteCommunity(self, **kwargs):
        """Updates global SNMP write community

        Args:
            
            globalCredentialNio, SNMPv2WriteCommunityDTO: SNMP write community details (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['globalCredentialNio']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateSnmpWriteCommunity" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/global-credential/snmpv2-write-community'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('globalCredentialNio' in params):
            bodyParam = params['globalCredentialNio']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def addSnmpWriteCommunity(self, **kwargs):
        """Creates global SNMP write community

        Args:
            
            globalCredentialNioList, List[SNMPv2WriteCommunityDTO]: List of SNMP write communities (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['globalCredentialNioList']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addSnmpWriteCommunity" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/global-credential/snmpv2-write-community'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('globalCredentialNioList' in params):
            bodyParam = params['globalCredentialNioList']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def updateSnmpv3Credential(self, **kwargs):
        """Updates global SNMPv3 credential

        Args:
            
            globalCredentialNio, SNMPv3CredentialDTO: SNMPv3 credential details (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['globalCredentialNio']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateSnmpv3Credential" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/global-credential/snmpv3'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('globalCredentialNio' in params):
            bodyParam = params['globalCredentialNio']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def addSnmpv3Credential(self, **kwargs):
        """Creates global SNMPv3 credential

        Args:
            
            globalCredentialNioList, List[SNMPv3CredentialDTO]: List of SNMPv3 credentials (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['globalCredentialNioList']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addSnmpv3Credential" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/global-credential/snmpv3'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('globalCredentialNioList' in params):
            bodyParam = params['globalCredentialNioList']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def deleteGlobalCredential(self, **kwargs):
        """Retrieves global credential by ID

        Args:
            
            globalCredentialId, str: ID of global-credential (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['globalCredentialId']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteGlobalCredential" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/global-credential/{globalCredentialId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        
        if ('globalCredentialId' in params):
            replacement = str(self.apiClient.toPathValue(params['globalCredentialId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'globalCredentialId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getGlobalCredentialSubTypeByID(self, **kwargs):
        """Retrieves credential sub type for the given credential Id

        Args:
            
            id, str: Global Credential ID (required)
            
            
        
        Returns: GlobalCredentialSubTypeResult
        """

        allParams = ['id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getGlobalCredentialSubTypeByID" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/global-credential/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'GlobalCredentialSubTypeResult')
        return responseObject
        
        
        
    


