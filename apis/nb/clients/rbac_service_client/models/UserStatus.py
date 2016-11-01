#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class UserStatus(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'lockedAt': 'str',
            
            
            'lockExpiration': 'int',
            
            
            'accountLocked': 'bool',
            
            
            'username': 'str'
            
        }

        self.attributeMap = {
            
            'lockedAt': 'lockedAt',
            
            'lockExpiration': 'lockExpiration',
            
            'accountLocked': 'accountLocked',
            
            'username': 'username'
            
        }       

        
        
        self.lockedAt = None # str
        
        
        self.lockExpiration = None # int
        
        
        self.accountLocked = None # bool
        
        
        self.username = None # str
        
