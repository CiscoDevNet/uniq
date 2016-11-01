#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class AclPortInfo(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'destPorts': 'list[str]',
            
            
            'sourcePorts': 'list[str]'
            
        }

        self.attributeMap = {
            
            'destPorts': 'destPorts',
            
            'sourcePorts': 'sourcePorts'
            
        }       

        
        
        self.destPorts = None # list[str]
        
        
        self.sourcePorts = None # list[str]
        
