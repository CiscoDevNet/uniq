#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PolicyTagAssociationDeviceDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'restrictedReason': 'str',
            
            
            'deviceRole': 'str',
            
            
            'restricted': 'bool',
            
            
            'deviceId': 'str',
            
            
            'deviceType': 'str',
            
            
            'deviceName': 'str',
            
            
            'deviceIp': 'str',
            
            
            'unAssigned': 'bool'
            
        }

        self.attributeMap = {
            
            'restrictedReason': 'restrictedReason',
            
            'deviceRole': 'deviceRole',
            
            'restricted': 'restricted',
            
            'deviceId': 'deviceId',
            
            'deviceType': 'deviceType',
            
            'deviceName': 'deviceName',
            
            'deviceIp': 'deviceIp',
            
            'unAssigned': 'unAssigned'
            
        }       

        
        
        self.restrictedReason = None # str
        
        
        self.deviceRole = None # str
        
        
        self.restricted = None # bool
        
        
        self.deviceId = None # str
        
        
        self.deviceType = None # str
        
        
        self.deviceName = None # str
        
        
        self.deviceIp = None # str
        
        
        self.unAssigned = None # bool
        
