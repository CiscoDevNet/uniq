#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class DiscoveryApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def updateDiscovery(self, **kwargs):
        """Updates an existing discovery specified by id - only for starting/stopping the discovery

        Args:
            
            discovery, DiscoveryNIO: Discovery request that holds the status of discovery as active / inactive (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['discovery']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateDiscovery" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/discovery'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('discovery' in params):
            bodyParam = params['discovery']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def insertDiscovery(self, **kwargs):
        """Starts a new discovery process and returns a task-id

        Args:
            
            request, InventoryRequest: Discovery request that holds the parameters required for discovery (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['request']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method insertDiscovery" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/discovery'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('request' in params):
            bodyParam = params['request']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def deleteAllDiscovery(self, **kwargs):
        """Deletes all discovery

        Args:
            
        
        Returns: TaskIdResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteAllDiscovery" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/discovery'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

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

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getDiscoveryCount(self, **kwargs):
        """Retrieves the number of discoveries

        Args:
            
        
        Returns: CountResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getDiscoveryCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/discovery/count'
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
        
        
        
    
    def getDiscoveryJobsByIp(self, **kwargs):
        """Retrieves the list of discovery jobs for the given IP

        Args:
            
            offset, int: offset (required)
            
            
            limit, int: limit (required)
            
            
            ipAddress, str: ipAddress (required)
            
            
        
        Returns: DiscoveryJobNIOListResult
        """

        allParams = ['offset', 'limit', 'ipAddress']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getDiscoveryJobsByIp" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/discovery/job'
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
        
        if ('ipAddress' in params):
            queryParams['ipAddress'] = self.apiClient.toPathValue(params['ipAddress'])
        

        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'DiscoveryJobNIOListResult')
        return responseObject
        
        
        
    
    def getDiscoveryById(self, **kwargs):
        """Retrieves the discovery specified by id

        Args:
            
            id, str: Discovery ID (required)
            
            
        
        Returns: DiscoveryNIOResult
        """

        allParams = ['id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getDiscoveryById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/discovery/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'DiscoveryNIOResult')
        return responseObject
        
        
        
    
    def deleteDiscoveryById(self, **kwargs):
        """Deletes the discovery specified by id

        Args:
            
            id, str: Discovery ID (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteDiscoveryById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/discovery/{id}'
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
        
        
        
    
    def getDiscoveryJobsById(self, **kwargs):
        """Retrieves list of discovery jobs for the specified discovery id

        Args:
            
            id, str: Discovery ID (required)
            
            
            offset, int: offset (required)
            
            
            limit, int: limit (required)
            
            
            ipAddress, str: ipAddress (required)
            
            
        
        Returns: DiscoveryJobNIOListResult
        """

        allParams = ['id', 'offset', 'limit', 'ipAddress']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getDiscoveryJobsById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/discovery/{id}/job'
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
        
        if ('ipAddress' in params):
            queryParams['ipAddress'] = self.apiClient.toPathValue(params['ipAddress'])
        

        

        
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

        responseObject = self.apiClient.deserialize(response, 'DiscoveryJobNIOListResult')
        return responseObject
        
        
        
    
    def getNetworkDeviceByDiscoveryId(self, **kwargs):
        """Retrieves the network devices discovered in the discovery specified by id

        Args:
            
            taskId, str: taskId (required)
            
            
            id, str: id (required)
            
            
        
        Returns: NetworkDeviceNIOListResult
        """

        allParams = ['taskId', 'id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getNetworkDeviceByDiscoveryId" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/discovery/{id}/network-device'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('taskId' in params):
            queryParams['taskId'] = self.apiClient.toPathValue(params['taskId'])
        

        

        
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

        responseObject = self.apiClient.deserialize(response, 'NetworkDeviceNIOListResult')
        return responseObject
        
        
        
    
    def getNetworkDeviceCountByDiscoveryId(self, **kwargs):
        """Retrieves the number of network devices discovered in the discovery specified by id

        Args:
            
            taskId, str: taskId (required)
            
            
            id, str: Discovery ID (required)
            
            
        
        Returns: CountResult
        """

        allParams = ['taskId', 'id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getNetworkDeviceCountByDiscoveryId" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/discovery/{id}/network-device/count'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('taskId' in params):
            queryParams['taskId'] = self.apiClient.toPathValue(params['taskId'])
        

        

        
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

        responseObject = self.apiClient.deserialize(response, 'CountResult')
        return responseObject
        
        
        
    
    def getNetworkDeviceByDiscoveryIdByRange(self, **kwargs):
        """Retrieves the range of network devices discovered for the given discovery

        Args:
            
            taskId, str: taskId (required)
            
            
            id, str: Discovery ID (required)
            
            
            startIndex, int: Start index (required)
            
            
            recordsToReturn, int: Number of records to return (required)
            
            
        
        Returns: NetworkDeviceNIOListResult
        """

        allParams = ['taskId', 'id', 'startIndex', 'recordsToReturn']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getNetworkDeviceByDiscoveryIdByRange" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/discovery/{id}/network-device/{startIndex}/{recordsToReturn}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('taskId' in params):
            queryParams['taskId'] = self.apiClient.toPathValue(params['taskId'])
        

        

        
        if ('id' in params):
            replacement = str(self.apiClient.toPathValue(params['id']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'id' + '}',
                                                replacement)
        
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

        responseObject = self.apiClient.deserialize(response, 'NetworkDeviceNIOListResult')
        return responseObject
        
        
        
    
    def deleteDiscoveryByRange(self, **kwargs):
        """Deletes the discovery in the given range

        Args:
            
            startIndex, int: Start index (required)
            
            
            recordsToDelete, int: Number of records to delete (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['startIndex', 'recordsToDelete']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteDiscoveryByRange" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/discovery/{startIndex}/{recordsToDelete}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

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
        
        if ('recordsToDelete' in params):
            replacement = str(self.apiClient.toPathValue(params['recordsToDelete']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'recordsToDelete' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getDiscoveryByRange(self, **kwargs):
        """Retrieves the discovery in the given range

        Args:
            
            startIndex, int: Start index (required)
            
            
            recordsToReturn, int: Number of records to return (required)
            
            
        
        Returns: DiscoveryNIOListResult
        """

        allParams = ['startIndex', 'recordsToReturn']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getDiscoveryByRange" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/discovery/{startIndex}/{recordsToReturn}'
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

        responseObject = self.apiClient.deserialize(response, 'DiscoveryNIOListResult')
        return responseObject
        
        
        
    


