#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PerfMonitorStatistics(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'destIpAddress': 'str',
            
            
            'packetBytes': 'int',
            
            
            'protocol': 'str',
            
            
            'byteRate': 'int',
            
            
            'inputInterface': 'str',
            
            
            'ipv4DSCP': 'str',
            
            
            'ipv4TTL': 'int',
            
            
            'outputInterface': 'str',
            
            
            'packetCount': 'int',
            
            
            'packetLoss': 'int',
            
            
            'packetLossPercentage': 'float',
            
            
            'refreshedAt': 'int',
            
            
            'rtpJitterMax': 'int',
            
            
            'rtpJitterMean': 'int',
            
            
            'rtpJitterMin': 'int',
            
            
            'sourcePort': 'str',
            
            
            'sourceIpAddress': 'str',
            
            
            'destPort': 'str'
            
        }

        self.attributeMap = {
            
            'destIpAddress': 'destIpAddress',
            
            'packetBytes': 'packetBytes',
            
            'protocol': 'protocol',
            
            'byteRate': 'byteRate',
            
            'inputInterface': 'inputInterface',
            
            'ipv4DSCP': 'ipv4DSCP',
            
            'ipv4TTL': 'ipv4TTL',
            
            'outputInterface': 'outputInterface',
            
            'packetCount': 'packetCount',
            
            'packetLoss': 'packetLoss',
            
            'packetLossPercentage': 'packetLossPercentage',
            
            'refreshedAt': 'refreshedAt',
            
            'rtpJitterMax': 'rtpJitterMax',
            
            'rtpJitterMean': 'rtpJitterMean',
            
            'rtpJitterMin': 'rtpJitterMin',
            
            'sourcePort': 'sourcePort',
            
            'sourceIpAddress': 'sourceIpAddress',
            
            'destPort': 'destPort'
            
        }       

        
        
        self.destIpAddress = None # str
        
        
        self.packetBytes = None # int
        
        
        self.protocol = None # str
        
        
        self.byteRate = None # int
        
        
        self.inputInterface = None # str
        
        
        self.ipv4DSCP = None # str
        
        
        self.ipv4TTL = None # int
        
        
        self.outputInterface = None # str
        
        
        self.packetCount = None # int
        
        
        self.packetLoss = None # int
        
        
        self.packetLossPercentage = None # float
        
        
        self.refreshedAt = None # int
        
        
        self.rtpJitterMax = None # int
        
        
        self.rtpJitterMean = None # int
        
        
        self.rtpJitterMin = None # int
        
        
        self.sourcePort = None # str
        
        
        self.sourceIpAddress = None # str
        
        
        self.destPort = None # str
        
