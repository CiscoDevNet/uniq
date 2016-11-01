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
            
            'id': 'str',
            
            
            'type': 'str',
            
            
            'family': 'str',
            
            
            'managementIpAddress': 'str',
            
            
            'credentials': 'dict',
            
            
            'series': 'str',
            
            
            'hostname': 'str'
            
        }

        self.attributeMap = {
            
            'id': 'id',
            
            'type': 'type',
            
            'family': 'family',
            
            'managementIpAddress': 'managementIpAddress',
            
            'credentials': 'credentials',
            
            'series': 'series',
            
            'hostname': 'hostname'
            
        }       

        
        #Unique identifier of device
        
        self.id = None # str
        
        #Type of device as switch, router, wireless lan controller, accesspoints
        
        self.type = None # str
        
        #Family of device as switch, router, wireless lan controller, accesspoints
        
        self.family = None # str
        
        #IP address of the device
        
        self.managementIpAddress = None # str
        
        #Credential info
        
        self.credentials = None # dict
        
        #Device series
        
        self.series = None # str
        
        #Device name
        
        self.hostname = None # str
        
