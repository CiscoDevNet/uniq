#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class CiscoIseDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'description': 'str',
            
            
            'id': 'str',
            
            
            'password': 'str',
            
            
            'ipAddress': 'str',
            
            
            'username': 'str',
            
            
            'keystoreFileId': 'str',
            
            
            'keystoreFilePassPhrase': 'str',
            
            
            'subscriberName': 'str',
            
            
            'truststoreFileId': 'str',
            
            
            'truststoreFilePassPhrase': 'str',
            
            
            'serverState': 'str'
            
        }

        self.attributeMap = {
            
            'description': 'description',
            
            'id': 'id',
            
            'password': 'password',
            
            'ipAddress': 'ipAddress',
            
            'username': 'username',
            
            'keystoreFileId': 'keystoreFileId',
            
            'keystoreFilePassPhrase': 'keystoreFilePassPhrase',
            
            'subscriberName': 'subscriberName',
            
            'truststoreFileId': 'truststoreFileId',
            
            'truststoreFilePassPhrase': 'truststoreFilePassPhrase',
            
            'serverState': 'serverState'
            
        }       

        
        #description
        
        self.description = None # str
        
        #id
        
        self.id = None # str
        
        #password
        
        self.password = None # str
        
        #ipAddress
        
        self.ipAddress = None # str
        
        #username
        
        self.username = None # str
        
        #keystoreFileId
        
        self.keystoreFileId = None # str
        
        #keystoreFilePassPhrase
        
        self.keystoreFilePassPhrase = None # str
        
        #subscriberName
        
        self.subscriberName = None # str
        
        #truststoreFileId
        
        self.truststoreFileId = None # str
        
        #truststoreFilePassPhrase
        
        self.truststoreFilePassPhrase = None # str
        
        #serverState
        
        self.serverState = None # str
        
