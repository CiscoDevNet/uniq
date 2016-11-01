#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PathResponse(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'detailedStatus': 'DetailedStatus',
            
            
            'networkElements': 'list[NetworkElement]',
            
            
            'networkElementsInfo': 'list[NetworkElementInfo]',
            
            
            'properties': 'list[str]',
            
            
            'lastUpdate': 'str',
            
            
            'request': 'FlowAnalysis'
            
        }

        self.attributeMap = {
            
            'detailedStatus': 'detailedStatus',
            
            'networkElements': 'networkElements',
            
            'networkElementsInfo': 'networkElementsInfo',
            
            'properties': 'properties',
            
            'lastUpdate': 'lastUpdate',
            
            'request': 'request'
            
        }       

        
        #Detailed Status of the calculation of Path Trace with its inclusions
        
        self.detailedStatus = None # DetailedStatus
        
        
        self.networkElements = None # list[NetworkElement]
        
        #Nodes travesed along a path, including source and destination
        
        self.networkElementsInfo = None # list[NetworkElementInfo]
        
        #Properties for path trace
        
        self.properties = None # list[str]
        
        #Last updated time
        
        self.lastUpdate = None # str
        
        #Describes the source and destination for a path trace
        
        self.request = None # FlowAnalysis
        
