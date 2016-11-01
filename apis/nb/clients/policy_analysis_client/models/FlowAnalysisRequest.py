#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class FlowAnalysisRequest(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'protocol': 'str',
            
            
            'sourcePort': 'str',
            
            
            'destIP': 'str',
            
            
            'destPort': 'str',
            
            
            'sourceIP': 'str',
            
            
            'periodicRefresh': 'bool',
            
            
            'inclusions': 'list[str]'
            
        }

        self.attributeMap = {
            
            'protocol': 'protocol',
            
            'sourcePort': 'sourcePort',
            
            'destIP': 'destIP',
            
            'destPort': 'destPort',
            
            'sourceIP': 'sourceIP',
            
            'periodicRefresh': 'periodicRefresh',
            
            'inclusions': 'inclusions'
            
        }       

        
        #Protocol
        
        self.protocol = None # str
        
        #Source Port
        
        self.sourcePort = None # str
        
        #Destination IP address
        
        self.destIP = None # str
        
        #Destination Port
        
        self.destPort = None # str
        
        #Source IP address
        
        self.sourceIP = None # str
        
        #periodicRefresh of path for every 30 sec
        
        self.periodicRefresh = None # bool
        
        #Subset of {INTERFACE-STATS, QOS-STATS, DEVICE-STATS, PERFORMANCE-STATS, ACL-TRACE}
        
        self.inclusions = None # list[str]
        
