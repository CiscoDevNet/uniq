#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class IPPoolAllocationDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'status': 'str',
            
            
            'deviceId': 'str',
            
            
            'siteId': 'str',
            
            
            'ipSubnet': 'str',
            
            
            'networkFeature': 'str',
            
            
            'siteName': 'str',
            
            
            'deviceName': 'str'
            
        }

        self.attributeMap = {
            
            'status': 'status',
            
            'deviceId': 'deviceId',
            
            'siteId': 'siteId',
            
            'ipSubnet': 'ipSubnet',
            
            'networkFeature': 'networkFeature',
            
            'siteName': 'siteName',
            
            'deviceName': 'deviceName'
            
        }       

        
        
        self.status = None # str
        
        
        self.deviceId = None # str
        
        
        self.siteId = None # str
        
        
        self.ipSubnet = None # str
        
        
        self.networkFeature = None # str
        
        
        self.siteName = None # str
        
        
        self.deviceName = None # str
        
