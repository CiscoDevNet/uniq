#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class SiteVLANDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'ipAddress': 'str',
            
            
            'numberOfIPs': 'int',
            
            
            'vlanType': 'str',
            
            
            'vlanId': 'int',
            
            
            'dhcpEnabled': 'bool',
            
            
            'dhcpIp': 'str',
            
            
            'dhcpMask': 'int',
            
            
            'prefix': 'str'
            
        }

        self.attributeMap = {
            
            'ipAddress': 'ipAddress',
            
            'numberOfIPs': 'numberOfIPs',
            
            'vlanType': 'vlanType',
            
            'vlanId': 'vlanId',
            
            'dhcpEnabled': 'dhcpEnabled',
            
            'dhcpIp': 'dhcpIp',
            
            'dhcpMask': 'dhcpMask',
            
            'prefix': 'prefix'
            
        }       

        
        
        self.ipAddress = None # str
        
        
        self.numberOfIPs = None # int
        
        
        self.vlanType = None # str
        
        
        self.vlanId = None # int
        
        
        self.dhcpEnabled = None # bool
        
        
        self.dhcpIp = None # str
        
        
        self.dhcpMask = None # int
        
        
        self.prefix = None # str
        
