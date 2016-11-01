#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class SiteIPAddressPoolDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'ipAddress': 'str',
            
            
            'vlanType': 'str',
            
            
            'vlanId': 'str',
            
            
            'ipAddressType': 'str',
            
            
            'deviceSerialNumber': 'list[str]',
            
            
            'siteName': 'str',
            
            
            'isBrownFieldSite': 'bool',
            
            
            'layer3Site': 'bool',
            
            
            'id': 'str',
            
            
            'prefix': 'str'
            
        }

        self.attributeMap = {
            
            'ipAddress': 'ipAddress',
            
            'vlanType': 'vlanType',
            
            'vlanId': 'vlanId',
            
            'ipAddressType': 'ipAddressType',
            
            'deviceSerialNumber': 'deviceSerialNumber',
            
            'siteName': 'siteName',
            
            'isBrownFieldSite': 'isBrownFieldSite',
            
            'layer3Site': 'layer3Site',
            
            'id': 'id',
            
            'prefix': 'prefix'
            
        }       

        
        
        self.ipAddress = None # str
        
        
        self.vlanType = None # str
        
        
        self.vlanId = None # str
        
        
        self.ipAddressType = None # str
        
        
        self.deviceSerialNumber = None # list[str]
        
        
        self.siteName = None # str
        
        
        self.isBrownFieldSite = None # bool
        
        
        self.layer3Site = None # bool
        
        
        self.id = None # str
        
        
        self.prefix = None # str
        
