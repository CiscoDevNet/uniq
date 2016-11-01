#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class InterfaceInfoDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'ipAddress': 'str',
            
            
            'subnetMask': 'str',
            
            
            'networkAddress': 'str',
            
            
            'switchPort': 'bool',
            
            
            'interfaceName': 'str',
            
            
            'nextHop': 'str',
            
            
            'trunkPort': 'bool'
            
        }

        self.attributeMap = {
            
            'ipAddress': 'ipAddress',
            
            'subnetMask': 'subnetMask',
            
            'networkAddress': 'networkAddress',
            
            'switchPort': 'switchPort',
            
            'interfaceName': 'interfaceName',
            
            'nextHop': 'nextHop',
            
            'trunkPort': 'trunkPort'
            
        }       

        
        
        self.ipAddress = None # str
        
        
        self.subnetMask = None # str
        
        
        self.networkAddress = None # str
        
        
        self.switchPort = None # bool
        
        
        self.interfaceName = None # str
        
        
        self.nextHop = None # str
        
        
        self.trunkPort = None # bool
        
