#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PublicKey(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'format': 'str',
            
            
            'algorithm': 'str',
            
            
            'encoded': 'list[byte]'
            
        }

        self.attributeMap = {
            
            'format': 'format',
            
            'algorithm': 'algorithm',
            
            'encoded': 'encoded'
            
        }       

        
        
        self.format = None # str
        
        
        self.algorithm = None # str
        
        
        self.encoded = None # list[byte]
        
