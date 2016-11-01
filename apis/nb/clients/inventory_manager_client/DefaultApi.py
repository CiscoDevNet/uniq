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

    
    
    def getLicenseInfo(self, **kwargs):
        """Retrieves the license info for a network devices by filters

        Args:
            
            deviceId, str: Network Device Id (required)
            
            
            limit, str: limit (required)
            
            
            offset, str: offset (required)
            
            
            sortBy, str: sortBy (required)
            
            
            order, str: order (required)
            
            
            countedList, list[str]: countedList (required)
            
            
            eulaStatusList, list[str]: eulaStatusList (required)
            
            
            evalPeriodLeftList, list[str]: evalPeriodLeftList (required)
            
            
            evalPeriodUsedList, list[str]: evalPeriodUsedList (required)
            
            
            expiredDateList, list[str]: expiredDateList (required)
            
            
            expiredPeriodList, list[str]: expiredPeriodList (required)
            
            
            featureVersionList, list[str]: featureVersionList (required)
            
            
            hostIdList, list[str]: hostIdList (required)
            
            
            isCountedList, list[str]: isCountedList (required)
            
            
            isEulaAcceptedList, list[str]: isEulaAcceptedList (required)
            
            
            isEulaApplicableList, list[str]: isEulaApplicableList (required)
            
            
            isTechnologyLicenseList, list[str]: isTechnologyLicenseList (required)
            
            
            licenseFileCountList, list[str]: licenseFileCountList (required)
            
            
            licenseFileNameList, list[str]: licenseFileNameList (required)
            
            
            licenseIndexList, list[str]: licenseIndexList (required)
            
            
            maxUsageCountList, list[str]: maxUsageCountList (required)
            
            
            parentIdList, list[str]: parentIdList (required)
            
            
            physicalIndexList, list[str]: physicalIndexList (required)
            
            
            priorityList, list[str]: priorityList (required)
            
            
            provisionStateList, list[str]: provisionStateList (required)
            
            
            statusList, list[str]: statusList (required)
            
            
            storedUsedList, list[str]: storedUsedList (required)
            
            
            storeNameList, list[str]: storeNameList (required)
            
            
            totalCountList, list[str]: totalCountList (required)
            
            
            licenseTypeList, list[str]: licenseTypeList (required)
            
            
            usageCountList, list[str]: usageCountList (required)
            
            
            usageCountRemainingList, list[str]: usageCountRemainingList (required)
            
            
            validityPeriodList, list[str]: validityPeriodList (required)
            
            
            validityPeriodRemainingList, list[str]: validityPeriodRemainingList (required)
            
            
        
        Returns: LicenseInfoListResult
        """

        allParams = ['deviceId', 'limit', 'offset', 'sortBy', 'order', 'countedList', 'eulaStatusList', 'evalPeriodLeftList', 'evalPeriodUsedList', 'expiredDateList', 'expiredPeriodList', 'featureVersionList', 'hostIdList', 'isCountedList', 'isEulaAcceptedList', 'isEulaApplicableList', 'isTechnologyLicenseList', 'licenseFileCountList', 'licenseFileNameList', 'licenseIndexList', 'maxUsageCountList', 'parentIdList', 'physicalIndexList', 'priorityList', 'provisionStateList', 'statusList', 'storedUsedList', 'storeNameList', 'totalCountList', 'licenseTypeList', 'usageCountList', 'usageCountRemainingList', 'validityPeriodList', 'validityPeriodRemainingList']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getLicenseInfo" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/license-info/network-device/{deviceId}'
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
        
        if ('sortBy' in params):
            queryParams['sortBy'] = self.apiClient.toPathValue(params['sortBy'])
        
        if ('order' in params):
            queryParams['order'] = self.apiClient.toPathValue(params['order'])
        
        if ('countedList' in params):
            queryParams['countedList'] = self.apiClient.toPathValue(params['countedList'])
        
        if ('eulaStatusList' in params):
            queryParams['eulaStatusList'] = self.apiClient.toPathValue(params['eulaStatusList'])
        
        if ('evalPeriodLeftList' in params):
            queryParams['evalPeriodLeftList'] = self.apiClient.toPathValue(params['evalPeriodLeftList'])
        
        if ('evalPeriodUsedList' in params):
            queryParams['evalPeriodUsedList'] = self.apiClient.toPathValue(params['evalPeriodUsedList'])
        
        if ('expiredDateList' in params):
            queryParams['expiredDateList'] = self.apiClient.toPathValue(params['expiredDateList'])
        
        if ('expiredPeriodList' in params):
            queryParams['expiredPeriodList'] = self.apiClient.toPathValue(params['expiredPeriodList'])
        
        if ('featureVersionList' in params):
            queryParams['featureVersionList'] = self.apiClient.toPathValue(params['featureVersionList'])
        
        if ('hostIdList' in params):
            queryParams['hostIdList'] = self.apiClient.toPathValue(params['hostIdList'])
        
        if ('isCountedList' in params):
            queryParams['isCountedList'] = self.apiClient.toPathValue(params['isCountedList'])
        
        if ('isEulaAcceptedList' in params):
            queryParams['isEulaAcceptedList'] = self.apiClient.toPathValue(params['isEulaAcceptedList'])
        
        if ('isEulaApplicableList' in params):
            queryParams['isEulaApplicableList'] = self.apiClient.toPathValue(params['isEulaApplicableList'])
        
        if ('isTechnologyLicenseList' in params):
            queryParams['isTechnologyLicenseList'] = self.apiClient.toPathValue(params['isTechnologyLicenseList'])
        
        if ('licenseFileCountList' in params):
            queryParams['licenseFileCountList'] = self.apiClient.toPathValue(params['licenseFileCountList'])
        
        if ('licenseFileNameList' in params):
            queryParams['licenseFileNameList'] = self.apiClient.toPathValue(params['licenseFileNameList'])
        
        if ('licenseIndexList' in params):
            queryParams['licenseIndexList'] = self.apiClient.toPathValue(params['licenseIndexList'])
        
        if ('maxUsageCountList' in params):
            queryParams['maxUsageCountList'] = self.apiClient.toPathValue(params['maxUsageCountList'])
        
        if ('parentIdList' in params):
            queryParams['parentIdList'] = self.apiClient.toPathValue(params['parentIdList'])
        
        if ('physicalIndexList' in params):
            queryParams['physicalIndexList'] = self.apiClient.toPathValue(params['physicalIndexList'])
        
        if ('priorityList' in params):
            queryParams['priorityList'] = self.apiClient.toPathValue(params['priorityList'])
        
        if ('provisionStateList' in params):
            queryParams['provisionStateList'] = self.apiClient.toPathValue(params['provisionStateList'])
        
        if ('statusList' in params):
            queryParams['statusList'] = self.apiClient.toPathValue(params['statusList'])
        
        if ('storedUsedList' in params):
            queryParams['storedUsedList'] = self.apiClient.toPathValue(params['storedUsedList'])
        
        if ('storeNameList' in params):
            queryParams['storeNameList'] = self.apiClient.toPathValue(params['storeNameList'])
        
        if ('totalCountList' in params):
            queryParams['totalCountList'] = self.apiClient.toPathValue(params['totalCountList'])
        
        if ('licenseTypeList' in params):
            queryParams['licenseTypeList'] = self.apiClient.toPathValue(params['licenseTypeList'])
        
        if ('usageCountList' in params):
            queryParams['usageCountList'] = self.apiClient.toPathValue(params['usageCountList'])
        
        if ('usageCountRemainingList' in params):
            queryParams['usageCountRemainingList'] = self.apiClient.toPathValue(params['usageCountRemainingList'])
        
        if ('validityPeriodList' in params):
            queryParams['validityPeriodList'] = self.apiClient.toPathValue(params['validityPeriodList'])
        
        if ('validityPeriodRemainingList' in params):
            queryParams['validityPeriodRemainingList'] = self.apiClient.toPathValue(params['validityPeriodRemainingList'])
        

        

        
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

        responseObject = self.apiClient.deserialize(response, 'LicenseInfoListResult')
        return responseObject
        
        
        
    
    def getLicenseInfoCount(self, **kwargs):
        """Retrieves the license info for a network devices by filters

        Args:
            
            deviceId, str: Network Device Id (required)
            
            
            countedList, list[str]: countedList (required)
            
            
            eulaStatusList, list[str]: eulaStatusList (required)
            
            
            evalPeriodLeftList, list[str]: evalPeriodLeftList (required)
            
            
            evalPeriodUsedList, list[str]: evalPeriodUsedList (required)
            
            
            expiredDateList, list[str]: expiredDateList (required)
            
            
            expiredPeriodList, list[str]: expiredPeriodList (required)
            
            
            featureVersionList, list[str]: featureVersionList (required)
            
            
            hostIdList, list[str]: hostIdList (required)
            
            
            isCountedList, list[str]: isCountedList (required)
            
            
            isEulaAcceptedList, list[str]: isEulaAcceptedList (required)
            
            
            isEulaApplicableList, list[str]: isEulaApplicableList (required)
            
            
            isTechnologyLicenseList, list[str]: isTechnologyLicenseList (required)
            
            
            licenseFileCountList, list[str]: licenseFileCountList (required)
            
            
            licenseFileNameList, list[str]: licenseFileNameList (required)
            
            
            licenseIndexList, list[str]: licenseIndexList (required)
            
            
            maxUsageCountList, list[str]: maxUsageCountList (required)
            
            
            parentIdList, list[str]: parentIdList (required)
            
            
            physicalIndexList, list[str]: physicalIndexList (required)
            
            
            priorityList, list[str]: priorityList (required)
            
            
            provisionStateList, list[str]: provisionStateList (required)
            
            
            statusList, list[str]: statusList (required)
            
            
            storedUsedList, list[str]: storedUsedList (required)
            
            
            storeNameList, list[str]: storeNameList (required)
            
            
            totalCountList, list[str]: totalCountList (required)
            
            
            licenseTypeList, list[str]: licenseTypeList (required)
            
            
            usageCountList, list[str]: usageCountList (required)
            
            
            usageCountRemainingList, list[str]: usageCountRemainingList (required)
            
            
            validityPeriodList, list[str]: validityPeriodList (required)
            
            
            validityPeriodRemainingList, list[str]: validityPeriodRemainingList (required)
            
            
        
        Returns: CountResult
        """

        allParams = ['deviceId', 'countedList', 'eulaStatusList', 'evalPeriodLeftList', 'evalPeriodUsedList', 'expiredDateList', 'expiredPeriodList', 'featureVersionList', 'hostIdList', 'isCountedList', 'isEulaAcceptedList', 'isEulaApplicableList', 'isTechnologyLicenseList', 'licenseFileCountList', 'licenseFileNameList', 'licenseIndexList', 'maxUsageCountList', 'parentIdList', 'physicalIndexList', 'priorityList', 'provisionStateList', 'statusList', 'storedUsedList', 'storeNameList', 'totalCountList', 'licenseTypeList', 'usageCountList', 'usageCountRemainingList', 'validityPeriodList', 'validityPeriodRemainingList']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getLicenseInfoCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/license-info/network-device/{deviceId}/count'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('countedList' in params):
            queryParams['countedList'] = self.apiClient.toPathValue(params['countedList'])
        
        if ('eulaStatusList' in params):
            queryParams['eulaStatusList'] = self.apiClient.toPathValue(params['eulaStatusList'])
        
        if ('evalPeriodLeftList' in params):
            queryParams['evalPeriodLeftList'] = self.apiClient.toPathValue(params['evalPeriodLeftList'])
        
        if ('evalPeriodUsedList' in params):
            queryParams['evalPeriodUsedList'] = self.apiClient.toPathValue(params['evalPeriodUsedList'])
        
        if ('expiredDateList' in params):
            queryParams['expiredDateList'] = self.apiClient.toPathValue(params['expiredDateList'])
        
        if ('expiredPeriodList' in params):
            queryParams['expiredPeriodList'] = self.apiClient.toPathValue(params['expiredPeriodList'])
        
        if ('featureVersionList' in params):
            queryParams['featureVersionList'] = self.apiClient.toPathValue(params['featureVersionList'])
        
        if ('hostIdList' in params):
            queryParams['hostIdList'] = self.apiClient.toPathValue(params['hostIdList'])
        
        if ('isCountedList' in params):
            queryParams['isCountedList'] = self.apiClient.toPathValue(params['isCountedList'])
        
        if ('isEulaAcceptedList' in params):
            queryParams['isEulaAcceptedList'] = self.apiClient.toPathValue(params['isEulaAcceptedList'])
        
        if ('isEulaApplicableList' in params):
            queryParams['isEulaApplicableList'] = self.apiClient.toPathValue(params['isEulaApplicableList'])
        
        if ('isTechnologyLicenseList' in params):
            queryParams['isTechnologyLicenseList'] = self.apiClient.toPathValue(params['isTechnologyLicenseList'])
        
        if ('licenseFileCountList' in params):
            queryParams['licenseFileCountList'] = self.apiClient.toPathValue(params['licenseFileCountList'])
        
        if ('licenseFileNameList' in params):
            queryParams['licenseFileNameList'] = self.apiClient.toPathValue(params['licenseFileNameList'])
        
        if ('licenseIndexList' in params):
            queryParams['licenseIndexList'] = self.apiClient.toPathValue(params['licenseIndexList'])
        
        if ('maxUsageCountList' in params):
            queryParams['maxUsageCountList'] = self.apiClient.toPathValue(params['maxUsageCountList'])
        
        if ('parentIdList' in params):
            queryParams['parentIdList'] = self.apiClient.toPathValue(params['parentIdList'])
        
        if ('physicalIndexList' in params):
            queryParams['physicalIndexList'] = self.apiClient.toPathValue(params['physicalIndexList'])
        
        if ('priorityList' in params):
            queryParams['priorityList'] = self.apiClient.toPathValue(params['priorityList'])
        
        if ('provisionStateList' in params):
            queryParams['provisionStateList'] = self.apiClient.toPathValue(params['provisionStateList'])
        
        if ('statusList' in params):
            queryParams['statusList'] = self.apiClient.toPathValue(params['statusList'])
        
        if ('storedUsedList' in params):
            queryParams['storedUsedList'] = self.apiClient.toPathValue(params['storedUsedList'])
        
        if ('storeNameList' in params):
            queryParams['storeNameList'] = self.apiClient.toPathValue(params['storeNameList'])
        
        if ('totalCountList' in params):
            queryParams['totalCountList'] = self.apiClient.toPathValue(params['totalCountList'])
        
        if ('licenseTypeList' in params):
            queryParams['licenseTypeList'] = self.apiClient.toPathValue(params['licenseTypeList'])
        
        if ('usageCountList' in params):
            queryParams['usageCountList'] = self.apiClient.toPathValue(params['usageCountList'])
        
        if ('usageCountRemainingList' in params):
            queryParams['usageCountRemainingList'] = self.apiClient.toPathValue(params['usageCountRemainingList'])
        
        if ('validityPeriodList' in params):
            queryParams['validityPeriodList'] = self.apiClient.toPathValue(params['validityPeriodList'])
        
        if ('validityPeriodRemainingList' in params):
            queryParams['validityPeriodRemainingList'] = self.apiClient.toPathValue(params['validityPeriodRemainingList'])
        

        

        
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

        responseObject = self.apiClient.deserialize(response, 'CountResult')
        return responseObject
        
        
        
    
    def getAllLocation(self, **kwargs):
        """Retrieves all locations

        Args:
            
        
        Returns: LocationNIOListResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAllLocation" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/location'
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

        responseObject = self.apiClient.deserialize(response, 'LocationNIOListResult')
        return responseObject
        
        
        
    
    def updateLocation(self, **kwargs):
        """Updates location

        Args:
            
            locationNIO, LocationNIO: Attributes of a location (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['locationNIO']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateLocation" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/location'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('locationNIO' in params):
            bodyParam = params['locationNIO']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def addLocation(self, **kwargs):
        """Creates location

        Args:
            
            locationNIO, LocationNIO: Attributes of a location (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['locationNIO']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addLocation" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/location'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('locationNIO' in params):
            bodyParam = params['locationNIO']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getLocationCount(self, **kwargs):
        """Retrieves location count

        Args:
            
        
        Returns: CountResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getLocationCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/location/count'
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
        
        
        
    
    def getLocationByName(self, **kwargs):
        """Retrieves location by location name

        Args:
            
            locationName, str: Location name (required)
            
            
        
        Returns: LocationNIOResult
        """

        allParams = ['locationName']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getLocationByName" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/location/location-name/{locationName}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        
        if ('locationName' in params):
            replacement = str(self.apiClient.toPathValue(params['locationName']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'locationName' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'LocationNIOResult')
        return responseObject
        
        
        
    
    def updateLocationTag(self, **kwargs):
        """Associate a tag to a location

        Args:
            
            tagNIO, TagNIO: TagNIO with tag ID and location ID (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['tagNIO']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateLocationTag" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/location/tag'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('tagNIO' in params):
            bodyParam = params['tagNIO']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getLocationById(self, **kwargs):
        """Retrieves location by ID

        Args:
            
            id, str: Location ID (required)
            
            
        
        Returns: LocationNIOResult
        """

        allParams = ['id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getLocationById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/location/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'LocationNIOResult')
        return responseObject
        
        
        
    
    def deleteLocationById(self, **kwargs):
        """Deletes location by ID

        Args:
            
            id, str: Location ID (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteLocationById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/location/{id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

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

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def deleteLocationTag(self, **kwargs):
        """Deletes location tag by location ID

        Args:
            
            id, str: Location ID (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteLocationTag" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/location/{id}/tag'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

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

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getLocationByRange(self, **kwargs):
        """Retrieves location range

        Args:
            
            startIndex, int: Start index (required)
            
            
            recordsToReturn, int: Number of records to return (required)
            
            
        
        Returns: LocationNIOListResult
        """

        allParams = ['startIndex', 'recordsToReturn']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getLocationByRange" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/location/{startIndex}/{recordsToReturn}'
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

        responseObject = self.apiClient.deserialize(response, 'LocationNIOListResult')
        return responseObject
        
        
        
    
    def getDeviceIdByFilename(self, **kwargs):
        """Retrieves the list of devices with given license filenames

        Args:
            
            licenseFileName, str: License file name (required)
            
            
        
        Returns: SuccessResultList
        """

        allParams = ['licenseFileName']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getDeviceIdByFilename" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device/license/{licenseFileName}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        
        if ('licenseFileName' in params):
            replacement = str(self.apiClient.toPathValue(params['licenseFileName']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'licenseFileName' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SuccessResultList')
        return responseObject
        
        
        
    
    def getLocationByTag(self, **kwargs):
        """Retrieves location by tag

        Args:
            
            tagId, str: Tag ID (required)
            
            
        
        Returns: LocationNIOListResult
        """

        allParams = ['tagId']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getLocationByTag" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/tag/{tagId}/location'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        
        if ('tagId' in params):
            replacement = str(self.apiClient.toPathValue(params['tagId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'tagId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'LocationNIOListResult')
        return responseObject
        
        
        
    


