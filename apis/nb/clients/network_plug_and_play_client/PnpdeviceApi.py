#!/usr/bin/env python
#pylint: skip-file
"""
PnpdeviceApi.py
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


class PnpdeviceApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient



    def getPnpDevices(self, **kwargs):
        """Retrieves a list of devices

        Args:

            serialNumber, str: Serial number (required)


            macAddress, str: MAC address (required)


            ipAddress, str: IP address (required)


            productId, str: Product ID (required)


            hostName, str: Host name (required)


            pkiEnabled, str: Device certificate provisioned (true) or not (false) (required)


            provisioningType, str: Provisioning type. Can be one of: new-device-adhoc, new-device-auto-provision, replacement-device (required)


            deviceType, str: Type of device. Currently only AP (Access Point) is supported (required)


            state, str: State of device. UNCLAIMED, IGNORED, PROVISIONED etc. Accepts a list of states (required)


            authStatus, str: Authentication status of device: authenticated, error, unsupported (required)


            startLastStateTransitionTime, str: Start of last state transition time (format: yyyy-MM-dd HH:mm:ss) (required)


            endLastStateTransitionTime, str: End of last state transition time (format: yyyy-MM-dd HH:mm:ss) (required)


            matchDeviceState, bool: Match device state. Boolean to match the given state (true) or not (false) (required)


            deviceMatchesARule, bool: Should device match a rule (true) or not (false) (required)


            sortBy, str: Sort response based on field (required)


            order, str: Order response in ascending (asc) or descending (des) order (required)


            offset, int: Starting index of the response. Minimum value is 1 (required)


            limit, int: Limit the number of responses. Maximum value supported is 500. Minimum value is 1 (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: ZtdDeviceListResult
        """

        allParams = ['serialNumber', 'macAddress', 'ipAddress', 'productId', 'hostName', 'pkiEnabled', 'provisioningType', 'deviceType', 'state', 'authStatus', 'startLastStateTransitionTime', 'endLastStateTransitionTime', 'matchDeviceState', 'deviceMatchesARule', 'sortBy', 'order', 'offset', 'limit', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPnpDevices" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-device'
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
            queryParams['serialNumber'] = self.apiClient.toPathValue(params['serialNumber'])

        if ('macAddress' in params):
            queryParams['macAddress'] = self.apiClient.toPathValue(params['macAddress'])

        if ('ipAddress' in params):
            queryParams['ipAddress'] = self.apiClient.toPathValue(params['ipAddress'])

        if ('productId' in params):
            queryParams['productId'] = self.apiClient.toPathValue(params['productId'])

        if ('hostName' in params):
            queryParams['hostName'] = self.apiClient.toPathValue(params['hostName'])

        if ('pkiEnabled' in params):
            queryParams['pkiEnabled'] = self.apiClient.toPathValue(params['pkiEnabled'])

        if ('provisioningType' in params):
            queryParams['provisioningType'] = self.apiClient.toPathValue(params['provisioningType'])

        if ('deviceType' in params):
            queryParams['deviceType'] = self.apiClient.toPathValue(params['deviceType'])

        if ('state' in params):
            queryParams['state'] = self.apiClient.toPathValue(params['state'])

        if ('authStatus' in params):
            queryParams['authStatus'] = self.apiClient.toPathValue(params['authStatus'])

        if ('startLastStateTransitionTime' in params):
            queryParams['startLastStateTransitionTime'] = self.apiClient.toPathValue(params['startLastStateTransitionTime'])

        if ('endLastStateTransitionTime' in params):
            queryParams['endLastStateTransitionTime'] = self.apiClient.toPathValue(params['endLastStateTransitionTime'])

        if ('matchDeviceState' in params):
            queryParams['matchDeviceState'] = self.apiClient.toPathValue(params['matchDeviceState'])

        if ('deviceMatchesARule' in params):
            queryParams['deviceMatchesARule'] = self.apiClient.toPathValue(params['deviceMatchesARule'])

        if ('sortBy' in params):
            queryParams['sortBy'] = self.apiClient.toPathValue(params['sortBy'])

        if ('order' in params):
            queryParams['order'] = self.apiClient.toPathValue(params['order'])

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

        responseObject = self.apiClient.deserialize(response, 'ZtdDeviceListResult')
        return responseObject




    def updatePnpDevice(self, **kwargs):
        """Updates a device with its ID

        Args:

            device, list[ZtdDevice]: PnP Device. The only modifiable properties are 1) state 2) configId and 3) imageId. Following are the only allowed combinations: 1) state = START_PROVISIONING, imageId = &lt;&gt; and/or configId = &lt;&gt;. 2) state = IGNORED 3) state = UNCLAIMED. Any other combinations of user input are rejected.  (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['device', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updatePnpDevice" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-device'
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







        if ('device' in params):
            bodyParam = params['device']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getPnpDeviceHistory(self, **kwargs):
        """Retrieves a device&#39;s history with its serial number

        Args:

            serialNumber, str: Serial number (required)


            order, str: Order response in ascending (asc) or descending (des) order of serial number (required)


            offset, int: Starting index of the response. Minimum value is 1 (required)


            limit, int: Limit the number of responses. Maximum value supported is 500. Minimum value is 1 (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: ZtdHistoryListResult
        """

        allParams = ['serialNumber', 'order', 'offset', 'limit', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPnpDeviceHistory" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-device-history'
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
            queryParams['serialNumber'] = self.apiClient.toPathValue(params['serialNumber'])

        if ('order' in params):
            queryParams['order'] = self.apiClient.toPathValue(params['order'])

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

        responseObject = self.apiClient.deserialize(response, 'ZtdHistoryListResult')
        return responseObject




    def getPnpDeviceHistoryCount(self, **kwargs):
        """Retrieves a count of a device&#39;s history with its serial number

        Args:

            serialNumber, str: Serial number (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: CountResult
        """

        allParams = ['serialNumber', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPnpDeviceHistoryCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-device-history/count'
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
            queryParams['serialNumber'] = self.apiClient.toPathValue(params['serialNumber'])



        if ('scope' in params):
            headerParams['scope'] = params['scope']








        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'CountResult')
        return responseObject




    def getPnpDeviceStateMap(self, **kwargs):
        """Retrieves a map of internal and external device states

        Args:

            scope, str: Authorization Scope for RBAC (required)



        Returns: ZtdDeviceStateMapResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPnpDeviceStateMap" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-device-state-map'
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

        responseObject = self.apiClient.deserialize(response, 'ZtdDeviceStateMapResult')
        return responseObject




    def getPnpDeviceCount(self, **kwargs):
        """Retrieves a count of devices

        Args:

            serialNumber, str: Serial number (required)


            macAddress, str: MAC address (required)


            ipAddress, str: IP address (required)


            productId, str: Product ID (required)


            hostName, str: Host name (required)


            pkiEnabled, str: Device certificate provisioned (true) or not (false) (required)


            provisioningType, str: Provisioning type. Can be one of: new-device-adhoc, new-device-auto-provision, replacement-device (required)


            deviceType, str: Type of device. Currently only AP (Access Point) is supported (required)


            state, str: State of device. UNCLAIMED, IGNORED, PROVISIONED. Accepts a list of states (required)


            authStatus, str: Authentication status of device: authenticated, error, unsupported (required)


            startLastStateTransitionTime, str: Start of last state transition time (format: yyyy-MM-dd HH:mm:ss) (required)


            endLastStateTransitionTime, str: End of last state transition time (format: yyyy-MM-dd HH:mm:ss) (required)


            matchDeviceState, bool: Match device state. Boolean to match the given state (true) or not (false) (required)


            deviceMatchesARule, bool: Should device match a rule (true) or not (false) (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: CountResult
        """

        allParams = ['serialNumber', 'macAddress', 'ipAddress', 'productId', 'hostName', 'pkiEnabled', 'provisioningType', 'deviceType', 'state', 'authStatus', 'startLastStateTransitionTime', 'endLastStateTransitionTime', 'matchDeviceState', 'deviceMatchesARule', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPnpDeviceCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-device/count'
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
            queryParams['serialNumber'] = self.apiClient.toPathValue(params['serialNumber'])

        if ('macAddress' in params):
            queryParams['macAddress'] = self.apiClient.toPathValue(params['macAddress'])

        if ('ipAddress' in params):
            queryParams['ipAddress'] = self.apiClient.toPathValue(params['ipAddress'])

        if ('productId' in params):
            queryParams['productId'] = self.apiClient.toPathValue(params['productId'])

        if ('hostName' in params):
            queryParams['hostName'] = self.apiClient.toPathValue(params['hostName'])

        if ('pkiEnabled' in params):
            queryParams['pkiEnabled'] = self.apiClient.toPathValue(params['pkiEnabled'])

        if ('provisioningType' in params):
            queryParams['provisioningType'] = self.apiClient.toPathValue(params['provisioningType'])

        if ('deviceType' in params):
            queryParams['deviceType'] = self.apiClient.toPathValue(params['deviceType'])

        if ('state' in params):
            queryParams['state'] = self.apiClient.toPathValue(params['state'])

        if ('authStatus' in params):
            queryParams['authStatus'] = self.apiClient.toPathValue(params['authStatus'])

        if ('startLastStateTransitionTime' in params):
            queryParams['startLastStateTransitionTime'] = self.apiClient.toPathValue(params['startLastStateTransitionTime'])

        if ('endLastStateTransitionTime' in params):
            queryParams['endLastStateTransitionTime'] = self.apiClient.toPathValue(params['endLastStateTransitionTime'])

        if ('matchDeviceState' in params):
            queryParams['matchDeviceState'] = self.apiClient.toPathValue(params['matchDeviceState'])

        if ('deviceMatchesARule' in params):
            queryParams['deviceMatchesARule'] = self.apiClient.toPathValue(params['deviceMatchesARule'])



        if ('scope' in params):
            headerParams['scope'] = params['scope']








        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'CountResult')
        return responseObject




    def getPnpDeviceByDeviceId(self, **kwargs):
        """Retrieves a device with its ID

        Args:

            deviceId, str: Device ID (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: ZtdDeviceResult
        """

        allParams = ['deviceId', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPnpDeviceByDeviceId" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-device/{deviceId}'
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

        responseObject = self.apiClient.deserialize(response, 'ZtdDeviceResult')
        return responseObject




    def deletePnpDeviceByDeviceId(self, **kwargs):
        """Deletes a device with its ID

        Args:

            deviceId, str: Device ID (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['deviceId', 'scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deletePnpDeviceByDeviceId" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-device/{deviceId}'
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

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject






