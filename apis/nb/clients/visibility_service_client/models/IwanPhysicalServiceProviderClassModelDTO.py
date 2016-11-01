#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class IwanPhysicalServiceProviderClassModelDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'sla': 'int',
            
            
            'dscp': 'str',
            
            
            'priority': 'str',
            
            
            'className': 'str'
            
        }

        self.attributeMap = {
            
            'sla': 'sla',
            
            'dscp': 'dscp',
            
            'priority': 'priority',
            
            'className': 'className'
            
        }       

        
        
        self.sla = None # int
        
        
        self.dscp = None # str
        
        
        self.priority = None # str
        
        
        self.className = None # str
        
