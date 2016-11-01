#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class VlanDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'numberOfIPs': 'int',
            
            
            'mask': 'int',
            
            
            'prefix': 'str',
            
            
            'vlanType': 'str',
            
            
            'vlanNumber': 'int',
            
            
            'networkAddress': 'str',
            
            
            'ipAddress': 'str',
            
            
            'interfaceName': 'str'
            
        }

        self.attributeMap = {
            
            'numberOfIPs': 'numberOfIPs',
            
            'mask': 'mask',
            
            'prefix': 'prefix',
            
            'vlanType': 'vlanType',
            
            'vlanNumber': 'vlanNumber',
            
            'networkAddress': 'networkAddress',
            
            'ipAddress': 'ipAddress',
            
            'interfaceName': 'interfaceName'
            
        }       

        
        
        self.numberOfIPs = None # int
        
        
        self.mask = None # int
        
        
        self.prefix = None # str
        
        
        self.vlanType = None # str
        
        
        self.vlanNumber = None # int
        
        
        self.networkAddress = None # str
        
        
        self.ipAddress = None # str
        
        
        self.interfaceName = None # str
        
