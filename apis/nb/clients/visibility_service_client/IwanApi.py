#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class IwanApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def addDeviceToSiteOnIgnoreValidation(self, **kwargs):
        """Adds the device to the site on click of ignore of config validation errors

        Args:
            
            ipAddress, str: ipAddress (required)
            
            
            siteName, str: siteName (required)
            
            
            username, str: requestorUsername (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['ipAddress', 'siteName', 'username', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addDeviceToSiteOnIgnoreValidation" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/add-device-on-ignoring-config-warnings/{ipAddress}/{siteName}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        
        if ('username' in params):
            headerParams['username'] = params['username']
        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        
        if ('ipAddress' in params):
            replacement = str(self.apiClient.toPathValue(params['ipAddress']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'ipAddress' + '}',
                                                replacement)
        
        if ('siteName' in params):
            replacement = str(self.apiClient.toPathValue(params['siteName']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'siteName' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def addDeviceToSite(self, **kwargs):
        """Validates a device&#39;s credentials and adds the device to the site

        Args:
            
            ipAddress, str: ipAddress (required)
            
            
            isExternalMasterController, str: isExternalMasterController (required)
            
            
            siteName, str: Site Name (required)
            
            
            username, str: requestorUsername (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['ipAddress', 'isExternalMasterController', 'siteName', 'username', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addDeviceToSite" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/add-device/{ipAddress}/{isExternalMasterController}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('siteName' in params):
            queryParams['siteName'] = self.apiClient.toPathValue(params['siteName'])
        

        
        if ('username' in params):
            headerParams['username'] = params['username']
        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        
        if ('ipAddress' in params):
            replacement = str(self.apiClient.toPathValue(params['ipAddress']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'ipAddress' + '}',
                                                replacement)
        
        if ('isExternalMasterController' in params):
            replacement = str(self.apiClient.toPathValue(params['isExternalMasterController']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'isExternalMasterController' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def isLockAcquired(self, **kwargs):
        """Check if lock is acquired for given workflow

        Args:
            
            workflowName, str: workflowName (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: bool
        """

        allParams = ['workflowName', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method isLockAcquired" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/check-lock/{workflowName}'
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
        

        
        if ('workflowName' in params):
            replacement = str(self.apiClient.toPathValue(params['workflowName']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'workflowName' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'bool')
        return responseObject
        
        
        
    
    def getIPPoolAllocationForDownload(self, **kwargs):
        """getIPPoolAllocationForDownload

        Args:
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: 
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getIPPoolAllocationForDownload" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/export-dhcp-addr-pools'
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

        
        
        
    
    def getInterfaceInfo(self, **kwargs):
        """API to get the Interface Information

        Args:
            
            deviceIP, str: deviceIP (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: InterfaceInfoDTOResult
        """

        allParams = ['deviceIP', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getInterfaceInfo" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/interface-info/{deviceIP}'
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
        

        
        if ('deviceIP' in params):
            replacement = str(self.apiClient.toPathValue(params['deviceIP']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'deviceIP' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'InterfaceInfoDTOResult')
        return responseObject
        
        
        
    
    def getIPPoolAllocationForNetwork(self, **kwargs):
        """API to get IP address allocation details for the network

        Args:
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: IPPoolAllocationListResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getIPPoolAllocationForNetwork" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/ippool-allocation'
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

        responseObject = self.apiClient.deserialize(response, 'IPPoolAllocationListResult')
        return responseObject
        
        
        
    
    def getIppoolAllocationSuggestion(self, **kwargs):
        """API to get the suggestion for the subnet allocation for Overlay/Loopback and VLAN

        Args:
            
            numberOfSites, int: numberOfSites (required)
            
            
            numberOfSPs, int: numberOfSPs (required)
            
            
            numberOfIPsPerVLAN, int: numberOfIPsPerVLAN (required)
            
            
            numberOfVLANs, int: numberOfVLANs (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: IPPoolAllocationSuggestionResult
        """

        allParams = ['numberOfSites', 'numberOfSPs', 'numberOfIPsPerVLAN', 'numberOfVLANs', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getIppoolAllocationSuggestion" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/ippool-allocation-suggestion/{numberOfSites}/{numberOfSPs}/{numberOfIPsPerVLAN}/{numberOfVLANs}'
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
        

        
        if ('numberOfSites' in params):
            replacement = str(self.apiClient.toPathValue(params['numberOfSites']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'numberOfSites' + '}',
                                                replacement)
        
        if ('numberOfSPs' in params):
            replacement = str(self.apiClient.toPathValue(params['numberOfSPs']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'numberOfSPs' + '}',
                                                replacement)
        
        if ('numberOfIPsPerVLAN' in params):
            replacement = str(self.apiClient.toPathValue(params['numberOfIPsPerVLAN']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'numberOfIPsPerVLAN' + '}',
                                                replacement)
        
        if ('numberOfVLANs' in params):
            replacement = str(self.apiClient.toPathValue(params['numberOfVLANs']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'numberOfVLANs' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'IPPoolAllocationSuggestionResult')
        return responseObject
        
        
        
    
    def getIPPoolAllocationForSite(self, **kwargs):
        """API to get IP address allocation details for a site

        Args:
            
            siteId, str: siteId (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: IPPoolAllocationListResult
        """

        allParams = ['siteId', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getIPPoolAllocationForSite" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/ippool-allocation/{siteId}'
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
        

        
        if ('siteId' in params):
            replacement = str(self.apiClient.toPathValue(params['siteId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'siteId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'IPPoolAllocationListResult')
        return responseObject
        
        
        
    
    def getIWANSiteNames(self, **kwargs):
        """API to get the List of IWAN Configured Site Names

        Args:
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: IWANSiteNamesDTOResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getIWANSiteNames" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/iwan-site-names'
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

        responseObject = self.apiClient.deserialize(response, 'IWANSiteNamesDTOResult')
        return responseObject
        
        
        
    
    def getNetworkWideSettings(self, **kwargs):
        """API to get the network wide settings

        Args:
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: NetworkWideSettingsResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getNetworkWideSettings" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/network-wide-settings'
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

        responseObject = self.apiClient.deserialize(response, 'NetworkWideSettingsResult')
        return responseObject
        
        
        
    
    def siteRecovery(self, **kwargs):
        """Recover&#39;s site from failure&#39;s

        Args:
            
            scope, str: Authorization Scope for RBAC (required)
            
            
            apicSiteId, str: apicSiteId (required)
            
            
            username, str: requestorUsername (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['scope', 'apicSiteId', 'username']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method siteRecovery" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/recovery/{apicSiteId}'
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
        

        
        if ('apicSiteId' in params):
            replacement = str(self.apiClient.toPathValue(params['apicSiteId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'apicSiteId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getSiteRoutingInfo(self, **kwargs):
        """API to Get DC Prefix and AS number for site using managementIps

        Args:
            
            managementIps, str: managementIps (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: DCRoutingInfoDTOResult
        """

        allParams = ['managementIps', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getSiteRoutingInfo" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/routing-info'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('managementIps' in params):
            queryParams['managementIps'] = self.apiClient.toPathValue(params['managementIps'])
        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'DCRoutingInfoDTOResult')
        return responseObject
        
        
        
    
    def getSiteDCPrefix(self, **kwargs):
        """API to Get DC Prefix and AS number for site using sitename

        Args:
            
            siteName, str: siteName (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: DCRoutingInfoDTOResult
        """

        allParams = ['siteName', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getSiteDCPrefix" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/routing-info/{siteName}'
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
        

        
        if ('siteName' in params):
            replacement = str(self.apiClient.toPathValue(params['siteName']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'siteName' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'DCRoutingInfoDTOResult')
        return responseObject
        
        
        
    
    def getSpokeBandwidthList(self, **kwargs):
        """Gets the list of supported bandwidth values for a spoke.

        Args:
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: IwanSpokeWanBandwidthListResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getSpokeBandwidthList" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/site-bandwidths'
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

        responseObject = self.apiClient.deserialize(response, 'IwanSpokeWanBandwidthListResult')
        return responseObject
        
        
        
    
    def getAllSitesConfigStatus(self, **kwargs):
        """Check if Configuration is changed OOB for all Sites

        Args:
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: str
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAllSitesConfigStatus" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/site-cfg-status'
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
        
        
        
    
    def getSiteConfigStatus(self, **kwargs):
        """Check if Site Configuration is changed OOB for a given Site

        Args:
            
            siteName, str: siteName (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: str
        """

        allParams = ['siteName', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getSiteConfigStatus" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/site-cfg-status/{siteName}'
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
        

        
        if ('siteName' in params):
            replacement = str(self.apiClient.toPathValue(params['siteName']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'siteName' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    
    def getSiteProvisionSettings(self, **kwargs):
        """API to Get Site Device Data

        Args:
            
            siteName, str: siteName (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: SiteDTOResult
        """

        allParams = ['siteName', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getSiteProvisionSettings" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/site-provision/{siteName}'
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
        

        
        if ('siteName' in params):
            replacement = str(self.apiClient.toPathValue(params['siteName']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'siteName' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SiteDTOResult')
        return responseObject
        
        
        
    
    def getSiteVLANData(self, **kwargs):
        """API to get the List of VLAN Data for a particular spoke Site

        Args:
            
            serialNumbers, str: serialNumbers (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: SiteVLANDTOResult
        """

        allParams = ['serialNumbers', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getSiteVLANData" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/site-vlan-data/{serialNumbers}'
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
        

        
        if ('serialNumbers' in params):
            replacement = str(self.apiClient.toPathValue(params['serialNumbers']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'serialNumbers' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SiteVLANDTOResult')
        return responseObject
        
        
        
    
    def getIwanTaggedDevices(self, **kwargs):
        """getIwanTaggedDevices

        Args:
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: IWANTaggedDevicesResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getIwanTaggedDevices" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/tagged-devices'
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

        responseObject = self.apiClient.deserialize(response, 'IWANTaggedDevicesResult')
        return responseObject
        
        
        
    
    def getUnclaimedDevices(self, **kwargs):
        """API to get unclaimed devices

        Args:
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: UnclaimedDeviceListResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getUnclaimedDevices" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/unclaimed-devices'
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

        responseObject = self.apiClient.deserialize(response, 'UnclaimedDeviceListResult')
        return responseObject
        
        
        
    
    def validateDeviceAndAddToHub(self, **kwargs):
        """Validates a device&#39;s credentials and adds the device to the hub site

        Args:
            
            ipAddress, str: ipAddress (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['ipAddress', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method validateDeviceAndAddToHub" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/validate-and-add/{ipAddress}'
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
        

        
        if ('ipAddress' in params):
            replacement = str(self.apiClient.toPathValue(params['ipAddress']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'ipAddress' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getWANLabels(self, **kwargs):
        """API to get the List of WAN Labels

        Args:
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: WANLabelsDTOResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getWANLabels" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/wan-labels'
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

        responseObject = self.apiClient.deserialize(response, 'WANLabelsDTOResult')
        return responseObject
        
        
        
    


