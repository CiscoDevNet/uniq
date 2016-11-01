#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class Certificate(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'type': 'str',
            
            
            'encoded': 'list[byte]',
            
            
            'publicKey': 'PublicKey'
            
        }

        self.attributeMap = {
            
            'type': 'type',
            
            'encoded': 'encoded',
            
            'publicKey': 'publicKey'
            
        }       

        
        
        self.type = None # str
        
        
        self.encoded = None # list[byte]
        
        
        self.publicKey = None # PublicKey
        
