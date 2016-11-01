#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ProtectionDomain(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'classLoader': 'ClassLoader',
            
            
            'codeSource': 'CodeSource',
            
            
            'principals': 'list[Principal]',
            
            
            'permissions': 'PermissionCollection'
            
        }

        self.attributeMap = {
            
            'classLoader': 'classLoader',
            
            'codeSource': 'codeSource',
            
            'principals': 'principals',
            
            'permissions': 'permissions'
            
        }       

        
        
        self.classLoader = None # ClassLoader
        
        
        self.codeSource = None # CodeSource
        
        
        self.principals = None # list[Principal]
        
        
        self.permissions = None # PermissionCollection
        
