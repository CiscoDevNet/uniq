#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ZtdSmartAccountDevice(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'serialNumber': 'str',
            
            
            'id': 'str',
            
            
            'platformId': 'str',
            
            
            'macAddress': 'str',
            
            
            'stateDisplay': 'str',
            
            
            'reDirectState': 'str',
            
            
            'reDirectStateDisplay': 'str',
            
            
            'projectName': 'str',
            
            
            'syncedAccountId': 'str',
            
            
            'state': 'str',
            
            
            'attributeInfo': 'dict'
            
        }

        self.attributeMap = {
            
            'serialNumber': 'serialNumber',
            
            'id': 'id',
            
            'platformId': 'platformId',
            
            'macAddress': 'macAddress',
            
            'stateDisplay': 'stateDisplay',
            
            'reDirectState': 'reDirectState',
            
            'reDirectStateDisplay': 'reDirectStateDisplay',
            
            'projectName': 'projectName',
            
            'syncedAccountId': 'syncedAccountId',
            
            'state': 'state',
            
            'attributeInfo': 'attributeInfo'
            
        }       

        
        #serial number
        
        self.serialNumber = None # str
        
        #Smart Account Device Id
        
        self.id = None # str
        
        #platform id
        
        self.platformId = None # str
        
        #mac address
        
        self.macAddress = None # str
        
        
        self.stateDisplay = None # str
        
        
        self.reDirectState = None # str
        
        
        self.reDirectStateDisplay = None # str
        
        
        self.projectName = None # str
        
        #synced account id
        
        self.syncedAccountId = None # str
        
        #state
        
        self.state = None # str
        
        
        self.attributeInfo = None # dict
        
