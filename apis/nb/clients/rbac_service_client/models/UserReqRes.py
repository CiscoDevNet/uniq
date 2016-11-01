#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class UserReqRes(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'authSource': 'str',
            
            
            'password': 'str',
            
            
            'authorization': 'list[ScopeRole]',
            
            
            'username': 'str',
            
            
            'oldPassword': 'str'
            
        }

        self.attributeMap = {
            
            'authSource': 'authSource',
            
            'password': 'password',
            
            'authorization': 'authorization',
            
            'username': 'username',
            
            'oldPassword': 'oldPassword'
            
        }       

        
        #User Authentication Source
        
        self.authSource = None # str
        
        
        self.password = None # str
        
        #User Authorization Scope
        
        self.authorization = None # list[ScopeRole]
        
        #Username
        
        self.username = None # str
        
        
        self.oldPassword = None # str
        
