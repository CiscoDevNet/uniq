#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class SiteDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'location': 'str',
            
            
            'id': 'str',
            
            
            'taskId': 'str',
            
            
            'siteType': 'str',
            
            
            'lanRoutingProtocol': 'str',
            
            
            'lanRoutingQualifier': 'str',
            
            
            'brownFieldSite': 'bool',
            
            
            'layer2Site': 'bool',
            
            
            'devices': 'list[SiteDeviceDTO]',
            
            
            'vlans': 'list[SiteVLANDTO]',
            
            
            'preferredPopName': 'str',
            
            
            'apicSiteIdentifier': 'str',
            
            
            'siteConfigurationType': 'str',
            
            
            'errorHandleCondition': 'str',
            
            
            'name': 'str'
            
        }

        self.attributeMap = {
            
            'location': 'location',
            
            'id': 'id',
            
            'taskId': 'taskId',
            
            'siteType': 'siteType',
            
            'lanRoutingProtocol': 'lanRoutingProtocol',
            
            'lanRoutingQualifier': 'lanRoutingQualifier',
            
            'brownFieldSite': 'brownFieldSite',
            
            'layer2Site': 'layer2Site',
            
            'devices': 'devices',
            
            'vlans': 'vlans',
            
            'preferredPopName': 'preferredPopName',
            
            'apicSiteIdentifier': 'apicSiteIdentifier',
            
            'siteConfigurationType': 'siteConfigurationType',
            
            'errorHandleCondition': 'errorHandleCondition',
            
            'name': 'name'
            
        }       

        
        
        self.location = None # str
        
        
        self.id = None # str
        
        
        self.taskId = None # str
        
        
        self.siteType = None # str
        
        
        self.lanRoutingProtocol = None # str
        
        
        self.lanRoutingQualifier = None # str
        
        
        self.brownFieldSite = None # bool
        
        
        self.layer2Site = None # bool
        
        
        self.devices = None # list[SiteDeviceDTO]
        
        
        self.vlans = None # list[SiteVLANDTO]
        
        
        self.preferredPopName = None # str
        
        
        self.apicSiteIdentifier = None # str
        
        
        self.siteConfigurationType = None # str
        
        
        self.errorHandleCondition = None # str
        
        
        self.name = None # str
        
