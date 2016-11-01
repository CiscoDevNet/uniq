#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class SNMPv3CredentialDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'privacyPassword': 'str',
            
            
            'privacyType': 'str',
            
            
            'snmpMode': 'str',
            
            
            'username': 'str',
            
            
            'authType': 'str',
            
            
            'authPassword': 'str',
            
            
            'description': 'str',
            
            
            'credentialType': 'str',
            
            
            'comments': 'str',
            
            
            'instanceUuid': 'str',
            
            
            'id': 'str'
            
        }

        self.attributeMap = {
            
            'privacyPassword': 'privacyPassword',
            
            'privacyType': 'privacyType',
            
            'snmpMode': 'snmpMode',
            
            'username': 'username',
            
            'authType': 'authType',
            
            'authPassword': 'authPassword',
            
            'description': 'description',
            
            'credentialType': 'credentialType',
            
            'comments': 'comments',
            
            'instanceUuid': 'instanceUuid',
            
            'id': 'id'
            
        }       

        
        #Privacy password is required if SNMP mode is AuthPriv
        
        self.privacyPassword = None # str
        
        #Privacy type is required if SNMP mode is AuthPriv
        
        self.privacyType = None # str
        
        #SNMP mode
        
        self.snmpMode = None # str
        
        #SNMP user name
        
        self.username = None # str
        
        #Authentication type is required if SNMP mode is AuthPriv / AuthNoPriv
        
        self.authType = None # str
        
        #AuthPassword is required if SNMP mode is AuthPriv / AuthNoPriv
        
        self.authPassword = None # str
        
        #Description of the credential
        
        self.description = None # str
        
        #Credential type to identify the application that uses the credential
        
        self.credentialType = None # str
        
        #Comments to identify the credential
        
        self.comments = None # str
        
        
        self.instanceUuid = None # str
        
        
        self.id = None # str
        
