#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ZtdRequestHeader(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'xForwardedFor': 'str',
            
            
            'attributeInfo': 'dict',
            
            
            'id': 'str'
            
        }

        self.attributeMap = {
            
            'xForwardedFor': 'xForwardedFor',
            
            'attributeInfo': 'attributeInfo',
            
            'id': 'id'
            
        }       

        
        
        self.xForwardedFor = None # str
        
        
        self.attributeInfo = None # dict
        
        
        self.id = None # str
        
