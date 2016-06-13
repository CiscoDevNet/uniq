#!/usr/bin/env python
#pylint: skip-file
"""
LicenseApi.py
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


class LicenseApi(object):

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


            deployPendingList, list[str]: deployPendingList (required)


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


            scope, str: Authorization Scope for RBAC (required)



        Returns: LicenseInfoListResult
        """

        allParams = ['deviceId', 'limit', 'offset', 'sortBy', 'order', 'countedList', 'deployPendingList', 'eulaStatusList', 'evalPeriodLeftList', 'evalPeriodUsedList', 'expiredDateList', 'expiredPeriodList', 'featureVersionList', 'hostIdList', 'isCountedList', 'isEulaAcceptedList', 'isEulaApplicableList', 'isTechnologyLicenseList', 'licenseFileCountList', 'licenseFileNameList', 'licenseIndexList', 'maxUsageCountList', 'parentIdList', 'physicalIndexList', 'priorityList', 'provisionStateList', 'statusList', 'storedUsedList', 'storeNameList', 'totalCountList', 'licenseTypeList', 'usageCountList', 'usageCountRemainingList', 'validityPeriodList', 'validityPeriodRemainingList', 'scope']

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

        if ('deployPendingList' in params):
            queryParams['deployPendingList'] = self.apiClient.toPathValue(params['deployPendingList'])

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



        if ('scope' in params):
            headerParams['scope'] = params['scope']



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


            deployPendingList, list[str]: deployPendingList (required)


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


            scope, str: Authorization Scope for RBAC (required)



        Returns: CountResult
        """

        allParams = ['deviceId', 'countedList', 'deployPendingList', 'eulaStatusList', 'evalPeriodLeftList', 'evalPeriodUsedList', 'expiredDateList', 'expiredPeriodList', 'featureVersionList', 'hostIdList', 'isCountedList', 'isEulaAcceptedList', 'isEulaApplicableList', 'isTechnologyLicenseList', 'licenseFileCountList', 'licenseFileNameList', 'licenseIndexList', 'maxUsageCountList', 'parentIdList', 'physicalIndexList', 'priorityList', 'provisionStateList', 'statusList', 'storedUsedList', 'storeNameList', 'totalCountList', 'licenseTypeList', 'usageCountList', 'usageCountRemainingList', 'validityPeriodList', 'validityPeriodRemainingList', 'scope']

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

        if ('deployPendingList' in params):
            queryParams['deployPendingList'] = self.apiClient.toPathValue(params['deployPendingList'])

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



        if ('scope' in params):
            headerParams['scope'] = params['scope']



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




    def getDeviceIdByFilename(self, **kwargs):
        """Retrieves the list of devices with given license filenames

        Args:

            licenseFileName, str: License file name (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: SuccessResultList
        """

        allParams = ['licenseFileName', 'scope']

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




        if ('scope' in params):
            headerParams['scope'] = params['scope']



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






