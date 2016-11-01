#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ServiceProviderProfileInterfaceDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'stale': 'bool',
            
            
            'interfaceName': 'str',
            
            
            'deviceId': 'str',
            
            
            'deviceName': 'str',
            
            
            'policyScope': 'str',
            
            
            'serviceProviderProfileVersion': 'int',
            
            
            'interfaceId': 'str',
            
            
            'id': 'str',
            
            
            'lastUpdateTime': 'int',
            
            
            'createTime': 'int'
            
        }

        self.attributeMap = {
            
            'stale': 'stale',
            
            'interfaceName': 'interfaceName',
            
            'deviceId': 'deviceId',
            
            'deviceName': 'deviceName',
            
            'policyScope': 'policyScope',
            
            'serviceProviderProfileVersion': 'serviceProviderProfileVersion',
            
            'interfaceId': 'interfaceId',
            
            'id': 'id',
            
            'lastUpdateTime': 'lastUpdateTime',
            
            'createTime': 'createTime'
            
        }       

        
        #Indicates whether the ServiceProviderProfile has been updated since the last time this interface was provisioned
        
        self.stale = None # bool
        
        
        self.interfaceName = None # str
        
        
        self.deviceId = None # str
        
        
        self.deviceName = None # str
        
        
        self.policyScope = None # str
        
        
        self.serviceProviderProfileVersion = None # int
        
        
        self.interfaceId = None # str
        
        #id
        
        self.id = None # str
        
        #lastUpdateTime
        
        self.lastUpdateTime = None # int
        
        #createTime
        
        self.createTime = None # int
        
