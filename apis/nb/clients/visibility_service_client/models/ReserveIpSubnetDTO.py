#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ReserveIpSubnetDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'id': 'str',
            
            
            'role': 'str',
            
            
            'siteName': 'str',
            
            
            'ipv4Subnet': 'str',
            
            
            'vlanType': 'str',
            
            
            'vlanId': 'str',
            
            
            'deviceSerialNumber': 'list[str]',
            
            
            'createSitePool': 'bool'
            
        }

        self.attributeMap = {
            
            'id': 'id',
            
            'role': 'role',
            
            'siteName': 'siteName',
            
            'ipv4Subnet': 'ipv4Subnet',
            
            'vlanType': 'vlanType',
            
            'vlanId': 'vlanId',
            
            'deviceSerialNumber': 'deviceSerialNumber',
            
            'createSitePool': 'createSitePool'
            
        }       

        
        
        self.id = None # str
        
        
        self.role = None # str
        
        
        self.siteName = None # str
        
        
        self.ipv4Subnet = None # str
        
        
        self.vlanType = None # str
        
        
        self.vlanId = None # str
        
        
        self.deviceSerialNumber = None # list[str]
        
        
        self.createSitePool = None # bool
        
