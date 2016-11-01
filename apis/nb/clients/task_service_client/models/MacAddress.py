#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class MacAddress(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'allZeros': 'bool',
            
            
            'allOnes': 'bool',
            
            
            'octets': 'list[byte]'
            
        }

        self.attributeMap = {
            
            'allZeros': 'allZeros',
            
            'allOnes': 'allOnes',
            
            'octets': 'octets'
            
        }       

        
        
        self.allZeros = None # bool
        
        
        self.allOnes = None # bool
        
        
        self.octets = None # list[byte]
        
