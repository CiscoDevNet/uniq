#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ZtdSyncedAccount(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'id': 'str',
            
            
            'userId': 'str',
            
            
            'profileId': 'str',
            
            
            'smartAccountId': 'str',
            
            
            'companyName': 'str',
            
            
            'virtualAccountId': 'str',
            
            
            'state': 'str'
            
        }

        self.attributeMap = {
            
            'id': 'id',
            
            'userId': 'userId',
            
            'profileId': 'profileId',
            
            'smartAccountId': 'smartAccountId',
            
            'companyName': 'companyName',
            
            'virtualAccountId': 'virtualAccountId',
            
            'state': 'state'
            
        }       

        
        #Synced Account ID
        
        self.id = None # str
        
        #Ztd Smart Account User Id
        
        self.userId = None # str
        
        #Profile ID
        
        self.profileId = None # str
        
        #Smart Account ID
        
        self.smartAccountId = None # str
        
        #Company Name
        
        self.companyName = None # str
        
        #Virtual Account ID
        
        self.virtualAccountId = None # str
        
        #State
        
        self.state = None # str
        
