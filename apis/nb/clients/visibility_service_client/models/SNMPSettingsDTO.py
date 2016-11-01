#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class SNMPSettingsDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'version': 'str',
            
            
            'mode': 'str',
            
            
            'timeout': 'str',
            
            
            'trapReflectionDestIp': 'str',
            
            
            'username': 'str',
            
            
            'authPwd': 'str',
            
            
            'privacyPwd': 'str',
            
            
            'readCommunity': 'str',
            
            
            'writeCommunity': 'str',
            
            
            'authType': 'str',
            
            
            'retry': 'str',
            
            
            'privacyType': 'str'
            
        }

        self.attributeMap = {
            
            'version': 'version',
            
            'mode': 'mode',
            
            'timeout': 'timeout',
            
            'trapReflectionDestIp': 'trapReflectionDestIp',
            
            'username': 'username',
            
            'authPwd': 'authPwd',
            
            'privacyPwd': 'privacyPwd',
            
            'readCommunity': 'readCommunity',
            
            'writeCommunity': 'writeCommunity',
            
            'authType': 'authType',
            
            'retry': 'retry',
            
            'privacyType': 'privacyType'
            
        }       

        
        
        self.version = None # str
        
        
        self.mode = None # str
        
        
        self.timeout = None # str
        
        
        self.trapReflectionDestIp = None # str
        
        
        self.username = None # str
        
        
        self.authPwd = None # str
        
        
        self.privacyPwd = None # str
        
        
        self.readCommunity = None # str
        
        
        self.writeCommunity = None # str
        
        
        self.authType = None # str
        
        
        self.retry = None # str
        
        
        self.privacyType = None # str
        
