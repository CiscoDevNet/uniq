#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class DNSSettingsDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'ipAddress': 'str',
            
            
            'secondaryIpAddress': 'str',
            
            
            'name': 'str'
            
        }

        self.attributeMap = {
            
            'ipAddress': 'ipAddress',
            
            'secondaryIpAddress': 'secondaryIpAddress',
            
            'name': 'name'
            
        }       

        
        
        self.ipAddress = None # str
        
        
        self.secondaryIpAddress = None # str
        
        
        self.name = None # str
        
