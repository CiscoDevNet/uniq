#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class IpspaceApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getGlobalIpPools(self, **kwargs):
        """Retrieves list of configured global IP space for IWAN

        Args:
            
            limit, str: limit (required)
            
            
            offset, str: offset (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: GenericIpAddressPoolListResult
        """

        allParams = ['limit', 'offset', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getGlobalIpPools" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ip-space/global'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])
        
        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])
        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GenericIpAddressPoolListResult')
        return responseObject
        
        
        
    
    def createIwanGlobalIpPools(self, **kwargs):
        """API to create Global IP Space for IWAN

        Args:
            
            iwanGlobalIpPools, list[GenericIpAddressPoolDTO]: iwanGlobalIpPools (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['iwanGlobalIpPools', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createIwanGlobalIpPools" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ip-space/global'
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
        
        if ('username' in params):
            headerParams['username'] = params['username']
        

        

        

        
        if ('iwanGlobalIpPools' in params):
            bodyParam = params['iwanGlobalIpPools']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getIpPoolGlobalSettings(self, **kwargs):
        """Retrieves IP space global setting for IWAN

        Args:
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: IpAddressGlobalSettingsResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getIpPoolGlobalSettings" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ip-space/global-setting'
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

        responseObject = self.apiClient.deserialize(response, 'IpAddressGlobalSettingsResult')
        return responseObject
        
        
        
    
    def updateIwanIpPoolGlobalSetting(self, **kwargs):
        """API to update Global Setting IP Space for IWAN

        Args:
            
            globalSetting, IpAddressGlobalDTO: globalSetting (required)
            
            
            scheduleAt, str: scheduleAt (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['globalSetting', 'scheduleAt', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateIwanIpPoolGlobalSetting" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ip-space/global-setting'
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
        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        
        if ('username' in params):
            headerParams['username'] = params['username']
        

        

        

        
        if ('globalSetting' in params):
            bodyParam = params['globalSetting']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def createIwanIpPoolGlobalSetting(self, **kwargs):
        """API to create Global Setting IP Space for IWAN

        Args:
            
            globalSetting, IpAddressGlobalDTO: globalSetting (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['globalSetting', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createIwanIpPoolGlobalSetting" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ip-space/global-setting'
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
        
        if ('username' in params):
            headerParams['username'] = params['username']
        

        

        

        
        if ('globalSetting' in params):
            bodyParam = params['globalSetting']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def deleteGlobalAddressPool(self, **kwargs):
        """Deletes global IP space for IWAN

        Args:
            
            id, str: IP Address Pool ID (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['id', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteGlobalAddressPool" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ip-space/global/{id}'
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
        
        if ('username' in params):
            headerParams['username'] = params['username']
        

        
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
        
        
        
    
    def scheduleIwanGlobalIpPoolsDeletion(self, **kwargs):
        """Schedule deletion of global ip-pool by id

        Args:
            
            id, str: IP Address Pool ID (required)
            
            
            scheduleTime, long: Schedule Time (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['id', 'scheduleTime', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method scheduleIwanGlobalIpPoolsDeletion" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ip-space/global/{id}/{scheduleTime}'
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
        
        if ('username' in params):
            headerParams['username'] = params['username']
        

        
        if ('id' in params):
            replacement = str(self.apiClient.toPathValue(params['id']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'id' + '}',
                                                replacement)
        
        if ('scheduleTime' in params):
            replacement = str(self.apiClient.toPathValue(params['scheduleTime']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'scheduleTime' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def scheduleIwanGlobalIpPoolsCreation(self, **kwargs):
        """Schedule Creation of global ip-pool(s)

        Args:
            
            iwanGlobalIpPools, list[GenericIpAddressPoolDTO]: iwanGlobalIpPools (required)
            
            
            scheduleTime, long: Schedule Time (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['iwanGlobalIpPools', 'scheduleTime', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method scheduleIwanGlobalIpPoolsCreation" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ip-space/global/{scheduleTime}'
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
        
        if ('username' in params):
            headerParams['username'] = params['username']
        

        
        if ('scheduleTime' in params):
            replacement = str(self.apiClient.toPathValue(params['scheduleTime']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'scheduleTime' + '}',
                                                replacement)
        

        

        
        if ('iwanGlobalIpPools' in params):
            bodyParam = params['iwanGlobalIpPools']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def reserveIwanIpSubnets(self, **kwargs):
        """API to create Site IP Space for IWAN

        Args:
            
            iwanReserveIpSubnets, list[ReserveIpSubnetDTO]: iwanReserveIpSubnets (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['iwanReserveIpSubnets', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method reserveIwanIpSubnets" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ip-space/reserve-subnet'
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
        
        if ('username' in params):
            headerParams['username'] = params['username']
        

        

        

        
        if ('iwanReserveIpSubnets' in params):
            bodyParam = params['iwanReserveIpSubnets']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getSiteIpPools(self, **kwargs):
        """Retrieves list of configured site IP space for IWAN

        Args:
            
            limit, str: limit (required)
            
            
            offset, str: offset (required)
            
            
            serialNumbers, str: Comma Separated Serial Numbers (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: SiteIPAddressPoolListResult
        """

        allParams = ['limit', 'offset', 'serialNumbers', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getSiteIpPools" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ip-space/site'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])
        
        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])
        
        if ('serialNumbers' in params):
            queryParams['serialNumbers'] = self.apiClient.toPathValue(params['serialNumbers'])
        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SiteIPAddressPoolListResult')
        return responseObject
        
        
        
    
    def createIwanSiteIpPools(self, **kwargs):
        """API to create Site IP Space for IWAN

        Args:
            
            iwanSiteIpPools, list[SiteIPAddressPoolDTO]: iwanSiteIpPools (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['iwanSiteIpPools', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createIwanSiteIpPools" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ip-space/site'
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
        
        if ('username' in params):
            headerParams['username'] = params['username']
        

        

        

        
        if ('iwanSiteIpPools' in params):
            bodyParam = params['iwanSiteIpPools']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def deleteSiteAddressPool(self, **kwargs):
        """Deletes site IP space for IWAN

        Args:
            
            iwanSiteIpPoolIds, List: List of Site IP Pool ids (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['iwanSiteIpPoolIds', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteSiteAddressPool" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ip-space/site'
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
        
        if ('username' in params):
            headerParams['username'] = params['username']
        

        

        

        
        if ('iwanSiteIpPoolIds' in params):
            bodyParam = params['iwanSiteIpPoolIds']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def scheduleIwanSiteIpPoolsCreation(self, **kwargs):
        """Schedule Creation of site ip-pool(s)

        Args:
            
            iwanSiteIpPools, list[SiteIPAddressPoolDTO]: iwanSiteIpPools (required)
            
            
            scheduleTime, long: Schedule Time (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['iwanSiteIpPools', 'scheduleTime', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method scheduleIwanSiteIpPoolsCreation" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ip-space/site/{scheduleTime}'
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
        
        if ('username' in params):
            headerParams['username'] = params['username']
        

        
        if ('scheduleTime' in params):
            replacement = str(self.apiClient.toPathValue(params['scheduleTime']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'scheduleTime' + '}',
                                                replacement)
        

        

        
        if ('iwanSiteIpPools' in params):
            bodyParam = params['iwanSiteIpPools']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def scheduleIwanSiteIpPoolsDeletion(self, **kwargs):
        """Schedule deletion of list of site ip-pools by id

        Args:
            
            iwanSiteIpPoolIds, List: List of Site IP Pool ids (required)
            
            
            scheduleTime, long: Schedule Time (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['iwanSiteIpPoolIds', 'scheduleTime', 'scope', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method scheduleIwanSiteIpPoolsDeletion" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ip-space/site/{scheduleTime}'
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
        
        if ('username' in params):
            headerParams['username'] = params['username']
        

        
        if ('scheduleTime' in params):
            replacement = str(self.apiClient.toPathValue(params['scheduleTime']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'scheduleTime' + '}',
                                                replacement)
        

        

        
        if ('iwanSiteIpPoolIds' in params):
            bodyParam = params['iwanSiteIpPoolIds']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    


