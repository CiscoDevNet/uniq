#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ZtdPlatform(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'platformName': 'str',
            
            
            'productId': 'list[str]'
            
        }

        self.attributeMap = {
            
            'platformName': 'platformName',
            
            'productId': 'productId'
            
        }       

        
        #Platform name
        
        self.platformName = None # str
        
        #Product IDs under a platform
        
        self.productId = None # list[str]
        
