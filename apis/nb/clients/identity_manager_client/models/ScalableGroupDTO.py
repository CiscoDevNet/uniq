#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ScalableGroupDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'description': 'str',
            
            
            'name': 'str',
            
            
            'id': 'str',
            
            
            'state': 'str',
            
            
            'createTime': 'int',
            
            
            'lastUpdateTime': 'int',
            
            
            'scalableGroupExternalHandle': 'str',
            
            
            'applicationGroups': 'list[ApplicationGroupDTOBrief]',
            
            
            'parentScalableGroup': 'ScalableGroupBriefDTO',
            
            
            'applications': 'list[ApplicationV2DTOBrief]',
            
            
            'identitySourceId': 'str',
            
            
            'identitySourceType': 'str',
            
            
            'identitySourceIpAddress': 'str'
            
        }

        self.attributeMap = {
            
            'description': 'description',
            
            'name': 'name',
            
            'id': 'id',
            
            'state': 'state',
            
            'createTime': 'createTime',
            
            'lastUpdateTime': 'lastUpdateTime',
            
            'scalableGroupExternalHandle': 'scalableGroupExternalHandle',
            
            'applicationGroups': 'applicationGroups',
            
            'parentScalableGroup': 'parentScalableGroup',
            
            'applications': 'applications',
            
            'identitySourceId': 'identitySourceId',
            
            'identitySourceType': 'identitySourceType',
            
            'identitySourceIpAddress': 'identitySourceIpAddress'
            
        }       

        
        #description
        
        self.description = None # str
        
        #name
        
        self.name = None # str
        
        #id
        
        self.id = None # str
        
        #state
        
        self.state = None # str
        
        #createTime
        
        self.createTime = None # int
        
        #lastUpdateTime
        
        self.lastUpdateTime = None # int
        
        #scalableGroupExternalHandle
        
        self.scalableGroupExternalHandle = None # str
        
        #applicationGroups that belong to the scalable group.
        
        self.applicationGroups = None # list[ApplicationGroupDTOBrief]
        
        #parentScalableGroup from which user, user groups are inherited.
        
        self.parentScalableGroup = None # ScalableGroupBriefDTO
        
        #applications that belong to the scalable group.
        
        self.applications = None # list[ApplicationV2DTOBrief]
        
        #identitySourceId
        
        self.identitySourceId = None # str
        
        #identitySourceType
        
        self.identitySourceType = None # str
        
        #identitySourceIpAddress
        
        self.identitySourceIpAddress = None # str
        
