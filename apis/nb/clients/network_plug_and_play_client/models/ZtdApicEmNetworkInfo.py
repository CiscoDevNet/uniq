#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ZtdApicEmNetworkInfo(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'proxyCert': 'str',
            
            
            'controllerCert': 'str',
            
            
            'ipv4Addresses': 'list[str]',
            
            
            'ipv6Addresses': 'list[str]',
            
            
            'proxyEnabled': 'bool'
            
        }

        self.attributeMap = {
            
            'proxyCert': 'proxyCert',
            
            'controllerCert': 'controllerCert',
            
            'ipv4Addresses': 'ipv4Addresses',
            
            'ipv6Addresses': 'ipv6Addresses',
            
            'proxyEnabled': 'proxyEnabled'
            
        }       

        
        
        self.proxyCert = None # str
        
        
        self.controllerCert = None # str
        
        
        self.ipv4Addresses = None # list[str]
        
        
        self.ipv6Addresses = None # list[str]
        
        
        self.proxyEnabled = None # bool
        
