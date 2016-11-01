#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class LDAPSettingsDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'password': 'str',
            
            
            'username': 'str',
            
            
            'ldapServerUrl': 'str',
            
            
            'securityAuthentication': 'str',
            
            
            'groupAttribute': 'str',
            
            
            'securityPrincipal': 'str'
            
        }

        self.attributeMap = {
            
            'password': 'password',
            
            'username': 'username',
            
            'ldapServerUrl': 'ldapServerUrl',
            
            'securityAuthentication': 'securityAuthentication',
            
            'groupAttribute': 'groupAttribute',
            
            'securityPrincipal': 'securityPrincipal'
            
        }       

        
        
        self.password = None # str
        
        
        self.username = None # str
        
        
        self.ldapServerUrl = None # str
        
        
        self.securityAuthentication = None # str
        
        
        self.groupAttribute = None # str
        
        
        self.securityPrincipal = None # str
        
