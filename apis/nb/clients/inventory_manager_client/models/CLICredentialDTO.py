#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class CLICredentialDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'username': 'str',
            
            
            'enablePassword': 'str',
            
            
            'password': 'str',
            
            
            'description': 'str',
            
            
            'comments': 'str',
            
            
            'credentialType': 'str',
            
            
            'instanceUuid': 'str',
            
            
            'id': 'str'
            
        }

        self.attributeMap = {
            
            'username': 'username',
            
            'enablePassword': 'enablePassword',
            
            'password': 'password',
            
            'description': 'description',
            
            'comments': 'comments',
            
            'credentialType': 'credentialType',
            
            'instanceUuid': 'instanceUuid',
            
            'id': 'id'
            
        }       

        
        #CLI username
        
        self.username = None # str
        
        #CLI enable password
        
        self.enablePassword = None # str
        
        #CLI password
        
        self.password = None # str
        
        #Description of the credential
        
        self.description = None # str
        
        #Comments to identify the credential
        
        self.comments = None # str
        
        #Credential type to identify the application that uses the credential
        
        self.credentialType = None # str
        
        
        self.instanceUuid = None # str
        
        
        self.id = None # str
        
