#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ZtdSmartAccountControllerAttribute(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'primaryFqdn': 'str',
            
            
            'primaryIpv4': 'str',
            
            
            'secondaryIpv4': 'str',
            
            
            'primaryProtocol': 'str',
            
            
            'primaryPort': 'str',
            
            
            'secondaryProtocol': 'str',
            
            
            'secondaryPort': 'str'
            
        }

        self.attributeMap = {
            
            'primaryFqdn': 'primaryFqdn',
            
            'primaryIpv4': 'primaryIpv4',
            
            'secondaryIpv4': 'secondaryIpv4',
            
            'primaryProtocol': 'primaryProtocol',
            
            'primaryPort': 'primaryPort',
            
            'secondaryProtocol': 'secondaryProtocol',
            
            'secondaryPort': 'secondaryPort'
            
        }       

        
        
        self.primaryFqdn = None # str
        
        
        self.primaryIpv4 = None # str
        
        
        self.secondaryIpv4 = None # str
        
        
        self.primaryProtocol = None # str
        
        
        self.primaryPort = None # str
        
        
        self.secondaryProtocol = None # str
        
        
        self.secondaryPort = None # str
        
