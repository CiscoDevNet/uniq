#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class PnpsmartaccountApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getSmartAccountDevices(self, **kwargs):
        """Retrieves synced devices

        Args:
            
            userId, str: User ID (required)
            
            
            syncedAccountId, str: Synced Account Id (required)
            
            
            serialNumber, str: Serial number (required)
            
            
            macAddress, str: MAC address (required)
            
            
            productId, str: Product ID (required)
            
            
            state, str: State (required)
            
            
            offset, int: Starting index of the response. Minimum value is 1 (required)
            
            
            limit, int: Limit the number of responses. Maximum value supported is 500. Minimum value is 1 (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: ZtdSmartAccountDeviceListResult
        """

        allParams = ['userId', 'syncedAccountId', 'serialNumber', 'macAddress', 'productId', 'state', 'offset', 'limit', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getSmartAccountDevices" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-smart-account/device'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('userId' in params):
            queryParams['userId'] = self.apiClient.toPathValue(params['userId'])
        
        if ('syncedAccountId' in params):
            queryParams['syncedAccountId'] = self.apiClient.toPathValue(params['syncedAccountId'])
        
        if ('serialNumber' in params):
            queryParams['serialNumber'] = self.apiClient.toPathValue(params['serialNumber'])
        
        if ('macAddress' in params):
            queryParams['macAddress'] = self.apiClient.toPathValue(params['macAddress'])
        
        if ('productId' in params):
            queryParams['productId'] = self.apiClient.toPathValue(params['productId'])
        
        if ('state' in params):
            queryParams['state'] = self.apiClient.toPathValue(params['state'])
        
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

        responseObject = self.apiClient.deserialize(response, 'ZtdSmartAccountDeviceListResult')
        return responseObject
        
        
        
    
    def syncSmartAccountDevices(self, **kwargs):
        """Sync the devices from cloud

        Args:
            
            syncedAccount, list[ZtdSyncedAccount]: Synced Account (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['syncedAccount', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method syncSmartAccountDevices" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-smart-account/device'
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
        

        

        

        
        if ('syncedAccount' in params):
            bodyParam = params['syncedAccount']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getSmartAccountDeviceCount(self, **kwargs):
        """Retrieves count of synced devices

        Args:
            
            userId, str: User ID (required)
            
            
            syncedAccountId, str: Synced Account Id (required)
            
            
            serialNumber, str: Serial number (required)
            
            
            macAddress, str: MAC address (required)
            
            
            productId, str: Product ID (required)
            
            
            state, str: State (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: str
        """

        allParams = ['userId', 'syncedAccountId', 'serialNumber', 'macAddress', 'productId', 'state', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getSmartAccountDeviceCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-smart-account/device/count'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('userId' in params):
            queryParams['userId'] = self.apiClient.toPathValue(params['userId'])
        
        if ('syncedAccountId' in params):
            queryParams['syncedAccountId'] = self.apiClient.toPathValue(params['syncedAccountId'])
        
        if ('serialNumber' in params):
            queryParams['serialNumber'] = self.apiClient.toPathValue(params['serialNumber'])
        
        if ('macAddress' in params):
            queryParams['macAddress'] = self.apiClient.toPathValue(params['macAddress'])
        
        if ('productId' in params):
            queryParams['productId'] = self.apiClient.toPathValue(params['productId'])
        
        if ('state' in params):
            queryParams['state'] = self.apiClient.toPathValue(params['state'])
        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    
    def getApicEmNetworkInfo(self, **kwargs):
        """Retrieves APIC-EM external network endpoints and gateway proxy status

        Args:
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: ZtdApicEmNetworkInfoResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getApicEmNetworkInfo" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-smart-account/netinfo'
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

        responseObject = self.apiClient.deserialize(response, 'ZtdApicEmNetworkInfoResult')
        return responseObject
        
        
        
    
    def getZtdSycnedAccounts(self, **kwargs):
        """Retrieves synced accounts for a user id

        Args:
            
            userId, str: User ID (required)
            
            
            smartAccountId, str: Smart Account ID (required)
            
            
            virtualAccountId, str: Virtual Account ID (required)
            
            
            state, str: State (required)
            
            
            offset, int: Starting index of the response. Minimum value is 1 (required)
            
            
            limit, int: Limit the number of responses. Maximum value supported is 500. Minimum value is 1 (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: ZtdSyncedAccountListResult
        """

        allParams = ['userId', 'smartAccountId', 'virtualAccountId', 'state', 'offset', 'limit', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getZtdSycnedAccounts" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-smart-account/synced-account'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('userId' in params):
            queryParams['userId'] = self.apiClient.toPathValue(params['userId'])
        
        if ('smartAccountId' in params):
            queryParams['smartAccountId'] = self.apiClient.toPathValue(params['smartAccountId'])
        
        if ('virtualAccountId' in params):
            queryParams['virtualAccountId'] = self.apiClient.toPathValue(params['virtualAccountId'])
        
        if ('state' in params):
            queryParams['state'] = self.apiClient.toPathValue(params['state'])
        
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

        responseObject = self.apiClient.deserialize(response, 'ZtdSyncedAccountListResult')
        return responseObject
        
        
        
    
    def createZtdSyncedAccount(self, **kwargs):
        """Create selected smart account and virtual account in PnP

        Args:
            
            syncedAccount, list[ZtdSyncedAccount]: Synced Account (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['syncedAccount', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createZtdSyncedAccount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-smart-account/synced-account'
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
        

        

        

        
        if ('syncedAccount' in params):
            bodyParam = params['syncedAccount']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getZtdSycnedAccountCount(self, **kwargs):
        """Retrieves count of synced accounts for a user id

        Args:
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: str
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getZtdSycnedAccountCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-smart-account/synced-account/count'
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

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    
    def getZtdSycnedAccountById(self, **kwargs):
        """Retrieves a synced account with its ID

        Args:
            
            syncedAccountId, str: Synced Account ID (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: ZtdSyncedAccountResult
        """

        allParams = ['syncedAccountId', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getZtdSycnedAccountById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-smart-account/synced-account/{syncedAccountId}'
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
        

        
        if ('syncedAccountId' in params):
            replacement = str(self.apiClient.toPathValue(params['syncedAccountId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'syncedAccountId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ZtdSyncedAccountResult')
        return responseObject
        
        
        
    
    def updateZtdSyncedAccount(self, **kwargs):
        """Updates a synced account with its ID

        Args:
            
            syncedAccount, list[ZtdSyncedAccount]: Synced Account (required)
            
            
            syncedAccountId, str: Synced Account ID (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['syncedAccount', 'syncedAccountId', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateZtdSyncedAccount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-smart-account/synced-account/{syncedAccountId}'
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
        

        
        if ('syncedAccountId' in params):
            replacement = str(self.apiClient.toPathValue(params['syncedAccountId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'syncedAccountId' + '}',
                                                replacement)
        

        

        
        if ('syncedAccount' in params):
            bodyParam = params['syncedAccount']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def deleteZtdSyncedAccountById(self, **kwargs):
        """Deletes a synced account with its ID

        Args:
            
            syncedAccount, ZtdSyncedAccount: Synced Account (required)
            
            
            syncedAccountId, str: Synced Account ID (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['syncedAccount', 'syncedAccountId', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteZtdSyncedAccountById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-smart-account/synced-account/{syncedAccountId}'
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
        

        
        if ('syncedAccountId' in params):
            replacement = str(self.apiClient.toPathValue(params['syncedAccountId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'syncedAccountId' + '}',
                                                replacement)
        

        

        
        if ('syncedAccount' in params):
            bodyParam = params['syncedAccount']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getSmartAccountProfiles(self, **kwargs):
        """Retrieves a list of profiles

        Args:
            
            syncedAccountId, str: Synced Account ID (required)
            
            
            offset, int: Starting index of the response. Minimum value is 1 (required)
            
            
            limit, int: Limit the number of responses. Maximum value supported is 500. Minimum value is 1 (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: ZtdSmartAccountProfileListResult
        """

        allParams = ['syncedAccountId', 'offset', 'limit', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getSmartAccountProfiles" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-smart-account/synced-account/{syncedAccountId}/profile'
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
        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        
        if ('syncedAccountId' in params):
            replacement = str(self.apiClient.toPathValue(params['syncedAccountId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'syncedAccountId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ZtdSmartAccountProfileListResult')
        return responseObject
        
        
        
    
    def updateProfile(self, **kwargs):
        """Update a profile

        Args:
            
            syncedAccountId, str: Synced Account ID (required)
            
            
            profile, list[ZtdSmartAccountProfile]: Profile  (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['syncedAccountId', 'profile', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateProfile" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-smart-account/synced-account/{syncedAccountId}/profile'
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
        

        
        if ('syncedAccountId' in params):
            replacement = str(self.apiClient.toPathValue(params['syncedAccountId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'syncedAccountId' + '}',
                                                replacement)
        

        

        
        if ('profile' in params):
            bodyParam = params['profile']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def createProfile(self, **kwargs):
        """Create a profile

        Args:
            
            syncedAccountId, str: Synced Account ID (required)
            
            
            profile, list[ZtdSmartAccountProfile]: Profile  (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['syncedAccountId', 'profile', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createProfile" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-smart-account/synced-account/{syncedAccountId}/profile'
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
        

        
        if ('syncedAccountId' in params):
            replacement = str(self.apiClient.toPathValue(params['syncedAccountId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'syncedAccountId' + '}',
                                                replacement)
        

        

        
        if ('profile' in params):
            bodyParam = params['profile']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getSmartAccountProfileById(self, **kwargs):
        """Retrieves profile by id

        Args:
            
            syncedAccountId, str: Synced Account ID (required)
            
            
            profileId, str: Profile Id (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: ZtdSmartAccountProfileListResult
        """

        allParams = ['syncedAccountId', 'profileId', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getSmartAccountProfileById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-smart-account/synced-account/{syncedAccountId}/profile/{profileId}'
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
        

        
        if ('syncedAccountId' in params):
            replacement = str(self.apiClient.toPathValue(params['syncedAccountId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'syncedAccountId' + '}',
                                                replacement)
        
        if ('profileId' in params):
            replacement = str(self.apiClient.toPathValue(params['profileId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'profileId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ZtdSmartAccountProfileListResult')
        return responseObject
        
        
        
    
    def deleteProfile(self, **kwargs):
        """Delete a profile

        Args:
            
            syncedAccountId, str: Synced Account ID (required)
            
            
            profileId, str: Profile Id (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['syncedAccountId', 'profileId', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteProfile" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-smart-account/synced-account/{syncedAccountId}/profile/{profileId}'
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
        

        
        if ('syncedAccountId' in params):
            replacement = str(self.apiClient.toPathValue(params['syncedAccountId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'syncedAccountId' + '}',
                                                replacement)
        
        if ('profileId' in params):
            replacement = str(self.apiClient.toPathValue(params['profileId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'profileId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getUsers(self, **kwargs):
        """Retrieves a list of smart account users

        Args:
            
            username, str: Username (required)
            
            
            state, str: State (required)
            
            
            offset, int: Starting index of the response. Minimum value is 1 (required)
            
            
            limit, int: Limit the number of responses. Maximum value supported is 500. Minimum value is 1 (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: ZtdSmartAccountUserListResult
        """

        allParams = ['username', 'state', 'offset', 'limit', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getUsers" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-smart-account/user'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('username' in params):
            queryParams['username'] = self.apiClient.toPathValue(params['username'])
        
        if ('state' in params):
            queryParams['state'] = self.apiClient.toPathValue(params['state'])
        
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

        responseObject = self.apiClient.deserialize(response, 'ZtdSmartAccountUserListResult')
        return responseObject
        
        
        
    
    def createUser(self, **kwargs):
        """Generates a smart account token

        Args:
            
            user, ZtdSmartAccountUser: Smart Account user (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['user', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createUser" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-smart-account/user'
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
        

        

        

        
        if ('user' in params):
            bodyParam = params['user']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def deleteUserById(self, **kwargs):
        """Deletes a smart account user with its ID

        Args:
            
            userId, str: User ID (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['userId', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteUserById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-smart-account/user/{userId}'
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
        

        
        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getSmartAccounts(self, **kwargs):
        """Retrieves a list of smart accounts

        Args:
            
            userId, str: User ID (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: ZtdSmartAccountListResult
        """

        allParams = ['userId', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getSmartAccounts" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-smart-account/user/{userId}/account'
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
        

        
        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ZtdSmartAccountListResult')
        return responseObject
        
        
        
    


