#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class QosClassMapStatistics(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'queueNoBufferDrops': 'int',
            
            
            'refreshedAt': 'int',
            
            
            'queueTotalDrops': 'int',
            
            
            'classMapName': 'str',
            
            
            'dropRate': 'int',
            
            
            'numBytes': 'int',
            
            
            'numPackets': 'int',
            
            
            'queueBandwidthbps': 'str',
            
            
            'queueDepth': 'int',
            
            
            'offeredRate': 'int'
            
        }

        self.attributeMap = {
            
            'queueNoBufferDrops': 'queueNoBufferDrops',
            
            'refreshedAt': 'refreshedAt',
            
            'queueTotalDrops': 'queueTotalDrops',
            
            'classMapName': 'classMapName',
            
            'dropRate': 'dropRate',
            
            'numBytes': 'numBytes',
            
            'numPackets': 'numPackets',
            
            'queueBandwidthbps': 'queueBandwidthbps',
            
            'queueDepth': 'queueDepth',
            
            'offeredRate': 'offeredRate'
            
        }       

        
        
        self.queueNoBufferDrops = None # int
        
        
        self.refreshedAt = None # int
        
        
        self.queueTotalDrops = None # int
        
        
        self.classMapName = None # str
        
        
        self.dropRate = None # int
        
        
        self.numBytes = None # int
        
        
        self.numPackets = None # int
        
        
        self.queueBandwidthbps = None # str
        
        
        self.queueDepth = None # int
        
        
        self.offeredRate = None # int
        
