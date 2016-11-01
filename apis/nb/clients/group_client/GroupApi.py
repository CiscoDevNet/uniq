#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class GroupApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getGroup(self, **kwargs):
        """Returns groups by name and/or type

        Args:
            
            groupType, str: groupType (required)
            
            
            groupName, str: groupName (required)
            
            
        
        Returns: ResourceGroupListResult
        """

        allParams = ['groupType', 'groupName']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getGroup" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/group'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('groupType' in params):
            queryParams['groupType'] = self.apiClient.toPathValue(params['groupType'])
        
        if ('groupName' in params):
            queryParams['groupName'] = self.apiClient.toPathValue(params['groupName'])
        

        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ResourceGroupListResult')
        return responseObject
        
        
        
    
    def updateGroup(self, **kwargs):
        """Updates a group specified by id

        Args:
            
            groupDTO, ResourceGroupDTO: Grouping request that holds the group information (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['groupDTO']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateGroup" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/group'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('groupDTO' in params):
            bodyParam = params['groupDTO']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def createGroup(self, **kwargs):
        """Creates a group with the information passed in the request

        Args:
            
            groupDTO, ResourceGroupDTO: Grouping request that holds the group information (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['groupDTO']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createGroup" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/group'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        

        

        

        
        if ('groupDTO' in params):
            bodyParam = params['groupDTO']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getGroupCount(self, **kwargs):
        """Returns the number of groups

        Args:
            
            groupType, str: groupType (required)
            
            
            groupName, str: groupName (required)
            
            
        
        Returns: CountResult
        """

        allParams = ['groupType', 'groupName']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getGroupCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/group/count'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('groupType' in params):
            queryParams['groupType'] = self.apiClient.toPathValue(params['groupType'])
        
        if ('groupName' in params):
            queryParams['groupName'] = self.apiClient.toPathValue(params['groupName'])
        

        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'CountResult')
        return responseObject
        
        
        
    
    def getSupportedClassNameAliases(self, **kwargs):
        """Retrieves the names for supported resource types

        Args:
            
        
        Returns: GroupTypesResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getSupportedClassNameAliases" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/group/member/type'
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

        responseObject = self.apiClient.deserialize(response, 'GroupTypesResult')
        return responseObject
        
        
        
    
    def getGroupsByMemberId(self, **kwargs):
        """Returns the groups containing the member

        Args:
            
            id, str: Member ID (required)
            
            
            groupType, str: groupType (required)
            
            
        
        Returns: ResourceGroupListResult
        """

        allParams = ['id', 'groupType']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getGroupsByMemberId" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/group/member/{id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('groupType' in params):
            queryParams['groupType'] = self.apiClient.toPathValue(params['groupType'])
        

        

        
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

        responseObject = self.apiClient.deserialize(response, 'ResourceGroupListResult')
        return responseObject
        
        
        
    
    def getGroupTypes(self, **kwargs):
        """Returns the group types supported

        Args:
            
        
        Returns: GroupTypesResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getGroupTypes" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/group/type'
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

        responseObject = self.apiClient.deserialize(response, 'GroupTypesResult')
        return responseObject
        
        
        
    
    def getGroupById(self, **kwargs):
        """Returns the group by id

        Args:
            
            id, str: Group ID (required)
            
            
        
        Returns: ResourceGroupResult
        """

        allParams = ['id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getGroupById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/group/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'ResourceGroupResult')
        return responseObject
        
        
        
    
    def deleteGroup(self, **kwargs):
        """Deletes a group specified by id

        Args:
            
            id, str: Group ID (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteGroup" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/group/{id}'
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
        
        
        
    
    def getMembersByGroupId(self, **kwargs):
        """Returns the members from the group specified by id

        Args:
            
            id, str: Group ID (required)
            
            
            offset, int: offset (required)
            
            
            limit, int: limit (required)
            
            
            memberType, str: memberType (required)
            
            
        
        Returns: GroupMembersResult
        """

        allParams = ['id', 'offset', 'limit', 'memberType']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getMembersByGroupId" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/group/{id}/member'
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
        
        if ('memberType' in params):
            queryParams['memberType'] = self.apiClient.toPathValue(params['memberType'])
        

        

        
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

        responseObject = self.apiClient.deserialize(response, 'GroupMembersResult')
        return responseObject
        
        
        
    
    def addMember(self, **kwargs):
        """Adds members to the group specified by id

        Args:
            
            id, str: Group ID (required)
            
            
            members, List[Entry«string,List«string»»]: Map of member type and member ids, for example, {&lt;br&gt;\&quot;networkdevice\&quot;:[\&quot;803ccafc-3458-49a2-9eff-0b2e47e491f7\&quot;,\&quot;203ccafc-3453-49a2-9eff-0b2e47e491f1\&quot;]&lt;br&gt;}&lt;br&gt;Refer /group/member/type for the supported member types. (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['id', 'members']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addMember" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/group/{id}/member'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

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
        

        

        
        if ('members' in params):
            bodyParam = params['members']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def removeMember(self, **kwargs):
        """Removes members from the group specified by id

        Args:
            
            id, str: Group ID (required)
            
            
            memberUuids, Set: Set of member ids to be removed from group (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['id', 'memberUuids']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method removeMember" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/group/{id}/member'
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
        

        

        
        if ('memberUuids' in params):
            bodyParam = params['memberUuids']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getGroupMemberCount(self, **kwargs):
        """Returns the number of members in a given group

        Args:
            
            id, str: Group ID (required)
            
            
            memberType, str: memberType (required)
            
            
        
        Returns: CountResult
        """

        allParams = ['id', 'memberType']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getGroupMemberCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/group/{id}/member/count'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('memberType' in params):
            queryParams['memberType'] = self.apiClient.toPathValue(params['memberType'])
        

        

        
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
        
        
        
    


