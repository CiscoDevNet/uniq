#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ZtdSmartAccountUser(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'password': 'str',
            
            
            'username': 'str',
            
            
            'id': 'str',
            
            
            'state': 'str'
            
        }

        self.attributeMap = {
            
            'password': 'password',
            
            'username': 'username',
            
            'id': 'id',
            
            'state': 'state'
            
        }       

        
        #Smart Account Password
        
        self.password = None # str
        
        #Smart Account Username
        
        self.username = None # str
        
        #User ID
        
        self.id = None # str
        
        
        self.state = None # str
        
