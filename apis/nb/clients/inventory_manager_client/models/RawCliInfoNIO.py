#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class RawCliInfoNIO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'version': 'str',
            
            
            'inventory': 'str',
            
            
            'ipIntfBrief': 'str',
            
            
            'intfDescription': 'str',
            
            
            'macAddressTable': 'str',
            
            
            'healthMonitor': 'str',
            
            
            'snmp': 'str',
            
            
            'id': 'str',
            
            
            'runningConfig': 'str',
            
            
            'cdpNeighbors': 'str',
            
            
            'attributeInfo': 'dict'
            
        }

        self.attributeMap = {
            
            'version': 'version',
            
            'inventory': 'inventory',
            
            'ipIntfBrief': 'ipIntfBrief',
            
            'intfDescription': 'intfDescription',
            
            'macAddressTable': 'macAddressTable',
            
            'healthMonitor': 'healthMonitor',
            
            'snmp': 'snmp',
            
            'id': 'id',
            
            'runningConfig': 'runningConfig',
            
            'cdpNeighbors': 'cdpNeighbors',
            
            'attributeInfo': 'attributeInfo'
            
        }       

        
        #Version configuration info of the device
        
        self.version = None # str
        
        #Inventory configuration info of the device
        
        self.inventory = None # str
        
        #IP interface brief configuration info of the device
        
        self.ipIntfBrief = None # str
        
        #Interface configuration info of the device
        
        self.intfDescription = None # str
        
        #MAC address configuration info of the device
        
        self.macAddressTable = None # str
        
        #Health monitor configuration info of the device
        
        self.healthMonitor = None # str
        
        #SNMP configuration info of the device
        
        self.snmp = None # str
        
        #Unique identifier for config
        
        self.id = None # str
        
        #Running-config of the device
        
        self.runningConfig = None # str
        
        #CDP configuration info of the device
        
        self.cdpNeighbors = None # str
        
        
        self.attributeInfo = None # dict
        
