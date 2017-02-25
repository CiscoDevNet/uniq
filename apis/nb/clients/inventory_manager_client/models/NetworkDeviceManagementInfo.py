#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class NetworkDeviceManagementInfo(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'family': 'str',
            
            
            'id': 'str',
            
            
            'type': 'str',
            
            
            'series': 'str',
            
            
            'hostname': 'str',
            
            
            'credentials': 'dict',
            
            
            'managementIpAddress': 'str'
            
        }

        self.attributeMap = {
            
            'family': 'family',
            
            'id': 'id',
            
            'type': 'type',
            
            'series': 'series',
            
            'hostname': 'hostname',
            
            'credentials': 'credentials',
            
            'managementIpAddress': 'managementIpAddress'
            
        }       

        
        #Family of device as switch, router, wireless lan controller, accesspoints
        
        self.family = None # str
        
        #Unique identifier of device
        
        self.id = None # str
        
        #Type of device as switch, router, wireless lan controller, accesspoints
        
        self.type = None # str
        
        #Device series
        
        self.series = None # str
        
        #Device name
        
        self.hostname = None # str
        
        #Credential info
        
        self.credentials = None # dict
        
        #IP address of the device
        
        self.managementIpAddress = None # str
        
