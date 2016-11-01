#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class AclAce(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'result': 'str',
            
            
            'matchingPorts': 'list[AclMatchingPorts]',
            
            
            'ace': 'str'
            
        }

        self.attributeMap = {
            
            'result': 'result',
            
            'matchingPorts': 'matchingPorts',
            
            'ace': 'ace'
            
        }       

        
        
        self.result = None # str
        
        
        self.matchingPorts = None # list[AclMatchingPorts]
        
        
        self.ace = None # str
        
