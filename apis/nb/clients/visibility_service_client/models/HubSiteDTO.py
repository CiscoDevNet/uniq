#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class HubSiteDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'lanRoutingQualifier': 'str',
            
            
            'lanRoutingProtocol': 'str',
            
            
            'siteType': 'str',
            
            
            'popId': 'int',
            
            
            'taskId': 'str',
            
            
            'dcPrefixDTOs': 'list[DCPrefixDTO]',
            
            
            'errorHandleCondition': 'str',
            
            
            'hubSiteWanDTOs': 'list[HubSiteWanDTO]',
            
            
            'apicSiteId': 'str',
            
            
            'name': 'str',
            
            
            'id': 'str'
            
        }

        self.attributeMap = {
            
            'lanRoutingQualifier': 'lanRoutingQualifier',
            
            'lanRoutingProtocol': 'lanRoutingProtocol',
            
            'siteType': 'siteType',
            
            'popId': 'popId',
            
            'taskId': 'taskId',
            
            'dcPrefixDTOs': 'dcPrefixDTOs',
            
            'errorHandleCondition': 'errorHandleCondition',
            
            'hubSiteWanDTOs': 'hubSiteWanDTOs',
            
            'apicSiteId': 'apicSiteId',
            
            'name': 'name',
            
            'id': 'id'
            
        }       

        
        
        self.lanRoutingQualifier = None # str
        
        
        self.lanRoutingProtocol = None # str
        
        
        self.siteType = None # str
        
        
        self.popId = None # int
        
        
        self.taskId = None # str
        
        
        self.dcPrefixDTOs = None # list[DCPrefixDTO]
        
        
        self.errorHandleCondition = None # str
        
        
        self.hubSiteWanDTOs = None # list[HubSiteWanDTO]
        
        
        self.apicSiteId = None # str
        
        
        self.name = None # str
        
        
        self.id = None # str
        
