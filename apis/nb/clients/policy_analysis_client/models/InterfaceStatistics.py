#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class InterfaceStatistics(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'refreshedAt': 'int',
            
            
            'inputPackets': 'int',
            
            
            'inputQueueCount': 'int',
            
            
            'inputQueueDrops': 'int',
            
            
            'inputQueueFlushes': 'int',
            
            
            'inputQueueMaxDepth': 'int',
            
            
            'inputRatebps': 'int',
            
            
            'outputDrop': 'int',
            
            
            'outputPackets': 'int',
            
            
            'outputQueueCount': 'int',
            
            
            'outputQueueDepth': 'int',
            
            
            'outputRatebps': 'int',
            
            
            'adminStatus': 'str',
            
            
            'operationalStatus': 'str'
            
        }

        self.attributeMap = {
            
            'refreshedAt': 'refreshedAt',
            
            'inputPackets': 'inputPackets',
            
            'inputQueueCount': 'inputQueueCount',
            
            'inputQueueDrops': 'inputQueueDrops',
            
            'inputQueueFlushes': 'inputQueueFlushes',
            
            'inputQueueMaxDepth': 'inputQueueMaxDepth',
            
            'inputRatebps': 'inputRatebps',
            
            'outputDrop': 'outputDrop',
            
            'outputPackets': 'outputPackets',
            
            'outputQueueCount': 'outputQueueCount',
            
            'outputQueueDepth': 'outputQueueDepth',
            
            'outputRatebps': 'outputRatebps',
            
            'adminStatus': 'adminStatus',
            
            'operationalStatus': 'operationalStatus'
            
        }       

        
        
        self.refreshedAt = None # int
        
        
        self.inputPackets = None # int
        
        
        self.inputQueueCount = None # int
        
        
        self.inputQueueDrops = None # int
        
        
        self.inputQueueFlushes = None # int
        
        
        self.inputQueueMaxDepth = None # int
        
        
        self.inputRatebps = None # int
        
        
        self.outputDrop = None # int
        
        
        self.outputPackets = None # int
        
        
        self.outputQueueCount = None # int
        
        
        self.outputQueueDepth = None # int
        
        
        self.outputRatebps = None # int
        
        
        self.adminStatus = None # str
        
        
        self.operationalStatus = None # str
        
