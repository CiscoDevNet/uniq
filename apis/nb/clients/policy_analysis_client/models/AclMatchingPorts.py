#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class AclMatchingPorts(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'protocol': 'str',
            
            
            'ports': 'list[AclPortInfo]'
            
        }

        self.attributeMap = {
            
            'protocol': 'protocol',
            
            'ports': 'ports'
            
        }       

        
        
        self.protocol = None # str
        
        
        self.ports = None # list[AclPortInfo]
        
