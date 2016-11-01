#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PolicyInterruptDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'createTime': 'int',
            
            
            'lastUpdateTime': 'int',
            
            
            'action': 'str',
            
            
            'policyScope': 'str',
            
            
            'scopeWirelessSegment': 'str'
            
        }

        self.attributeMap = {
            
            'createTime': 'createTime',
            
            'lastUpdateTime': 'lastUpdateTime',
            
            'action': 'action',
            
            'policyScope': 'policyScope',
            
            'scopeWirelessSegment': 'scopeWirelessSegment'
            
        }       

        
        
        self.createTime = None # int
        
        
        self.lastUpdateTime = None # int
        
        #One of {ABORT, ABORT-RESTORE-TO-ORIGINAL}
        
        self.action = None # str
        
        #Policy scope
        
        self.policyScope = None # str
        
        #Scope wireless segment
        
        self.scopeWirelessSegment = None # str
        
