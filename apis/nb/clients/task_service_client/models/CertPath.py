#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class CertPath(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'encodings': 'Iterator«string»',
            
            
            'certificates': 'list[Certificate]',
            
            
            'type': 'str',
            
            
            'encoded': 'list[byte]'
            
        }

        self.attributeMap = {
            
            'encodings': 'encodings',
            
            'certificates': 'certificates',
            
            'type': 'type',
            
            'encoded': 'encoded'
            
        }       

        
        
        self.encodings = None # Iterator«string»
        
        
        self.certificates = None # list[Certificate]
        
        
        self.type = None # str
        
        
        self.encoded = None # list[byte]
        
