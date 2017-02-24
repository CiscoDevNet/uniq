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
            
            
            'networkAddress': 'str',
            
            
            'ipAddress': 'str',
            
            
            'interfaceName': 'str',
            
            
            'vlanType': 'str',
            
            
            'vlanNumber': 'int'
            
        }

        self.attributeMap = {
            
            'numberOfIPs': 'numberOfIPs',
            
            'mask': 'mask',
            
            'prefix': 'prefix',
            
            'networkAddress': 'networkAddress',
            
            'ipAddress': 'ipAddress',
            
            'interfaceName': 'interfaceName',
            
            'vlanType': 'vlanType',
            
            'vlanNumber': 'vlanNumber'
            
        }       

        
        #Number of Ip addresses
        
        self.numberOfIPs = None # int
        
        #Mask ip
        
        self.mask = None # int
        
        #Prefix
        
        self.prefix = None # str
        
        #Network addresses
        
        self.networkAddress = None # str
        
        #Ip address
        
        self.ipAddress = None # str
        
        #Interface name
        
        self.interfaceName = None # str
        
        #Type of Vlan
        
        self.vlanType = None # str
        
        #Vlan Number
        
        self.vlanNumber = None # int
        
