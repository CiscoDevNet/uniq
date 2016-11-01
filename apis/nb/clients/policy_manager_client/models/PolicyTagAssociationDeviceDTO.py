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
            
            'restricted': 'bool',
            
            
            'unAssigned': 'bool',
            
            
            'deviceRole': 'str',
            
            
            'restrictedReason': 'str',
            
            
            'deviceId': 'str',
            
            
            'deviceType': 'str',
            
            
            'deviceName': 'str',
            
            
            'deviceIp': 'str'
            
        }

        self.attributeMap = {
            
            'restricted': 'restricted',
            
            'unAssigned': 'unAssigned',
            
            'deviceRole': 'deviceRole',
            
            'restrictedReason': 'restrictedReason',
            
            'deviceId': 'deviceId',
            
            'deviceType': 'deviceType',
            
            'deviceName': 'deviceName',
            
            'deviceIp': 'deviceIp'
            
        }       

        
        
        self.restricted = None # bool
        
        
        self.unAssigned = None # bool
        
        
        self.deviceRole = None # str
        
        
        self.restrictedReason = None # str
        
        
        self.deviceId = None # str
        
        
        self.deviceType = None # str
        
        
        self.deviceName = None # str
        
        
        self.deviceIp = None # str
        
