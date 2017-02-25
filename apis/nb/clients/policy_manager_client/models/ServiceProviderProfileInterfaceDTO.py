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
            
            'deviceId': 'str',
            
            
            'interfaceName': 'str',
            
            
            'deviceName': 'str',
            
            
            'policyScope': 'str',
            
            
            'interfaceId': 'str',
            
            
            'serviceProviderProfileVersion': 'int',
            
            
            'stale': 'bool',
            
            
            'id': 'str',
            
            
            'createTime': 'int',
            
            
            'lastUpdateTime': 'int'
            
        }

        self.attributeMap = {
            
            'deviceId': 'deviceId',
            
            'interfaceName': 'interfaceName',
            
            'deviceName': 'deviceName',
            
            'policyScope': 'policyScope',
            
            'interfaceId': 'interfaceId',
            
            'serviceProviderProfileVersion': 'serviceProviderProfileVersion',
            
            'stale': 'stale',
            
            'id': 'id',
            
            'createTime': 'createTime',
            
            'lastUpdateTime': 'lastUpdateTime'
            
        }       

        
        
        self.deviceId = None # str
        
        
        self.interfaceName = None # str
        
        
        self.deviceName = None # str
        
        
        self.policyScope = None # str
        
        
        self.interfaceId = None # str
        
        
        self.serviceProviderProfileVersion = None # int
        
        #Indicates whether the ServiceProviderProfile has been updated since the last time this interface was provisioned
        
        self.stale = None # bool
        
        #id
        
        self.id = None # str
        
        #createTime
        
        self.createTime = None # int
        
        #lastUpdateTime
        
        self.lastUpdateTime = None # int
        
