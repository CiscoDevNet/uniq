#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ZtdHistory(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'serialNumber': 'str',
            
            
            'log': 'str',
            
            
            'id': 'str',
            
            
            'platformId': 'str',
            
            
            'transactionTime': 'str'
            
        }

        self.attributeMap = {
            
            'serialNumber': 'serialNumber',
            
            'log': 'log',
            
            'id': 'id',
            
            'platformId': 'platformId',
            
            'transactionTime': 'transactionTime'
            
        }       

        
        #Serial number
        
        self.serialNumber = None # str
        
        #Log message from device
        
        self.log = None # str
        
        
        self.id = None # str
        
        #Platform ID
        
        self.platformId = None # str
        
        #Last contact time of device
        
        self.transactionTime = None # str
        
