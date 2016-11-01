#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ScopeRole(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'scope': 'str',
            
            
            'role': 'str'
            
        }

        self.attributeMap = {
            
            'scope': 'scope',
            
            'role': 'role'
            
        }       

        
        #Scope of Authorization. Added to support future implementations, supported value is only ALL
        
        self.scope = None # str
        
        #Authorization Role. Supported values are ROLE_ADMIN, ROLE_OBSERVER and ROLE_INSTALLER
        
        self.role = None # str
        
