#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class UUID(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'leastSignificantBits': 'int',
            
            
            'mostSignificantBits': 'int'
            
        }

        self.attributeMap = {
            
            'leastSignificantBits': 'leastSignificantBits',
            
            'mostSignificantBits': 'mostSignificantBits'
            
        }       

        
        
        self.leastSignificantBits = None # int
        
        
        self.mostSignificantBits = None # int
        
