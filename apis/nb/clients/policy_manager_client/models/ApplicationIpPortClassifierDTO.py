#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ApplicationIpPortClassifierDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'protocol': 'str',
            
            
            'ipAddress': 'str',
            
            
            'ports': 'list[int]',
            
            
            'ipPorts': 'list[int]',
            
            
            'lowerPort': 'int',
            
            
            'upperPort': 'int',
            
            
            'subnetMask': 'int'
            
        }

        self.attributeMap = {
            
            'protocol': 'protocol',
            
            'ipAddress': 'ipAddress',
            
            'ports': 'ports',
            
            'ipPorts': 'ipPorts',
            
            'lowerPort': 'lowerPort',
            
            'upperPort': 'upperPort',
            
            'subnetMask': 'subnetMask'
            
        }       

        
        #Protocol of the application. Allowed values are tcp, udp, tcp/udp, ip or it could be empty. Values are case sensitive.
        
        self.protocol = None # str
        
        #IP address of the application.
        
        self.ipAddress = None # str
        
        #L4 Port numbers of the application.
        
        self.ports = None # list[int]
        
        #L3 Protocol numbers of the application
        
        self.ipPorts = None # list[int]
        
        #Lower Port of the Port range.
        
        self.lowerPort = None # int
        
        #Upper Port of the Port range.
        
        self.upperPort = None # int
        
        #Subnet mask. Defaults to 32
        
        self.subnetMask = None # int
        
