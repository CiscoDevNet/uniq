#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PolicyInterruptInput(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'action': 'str',
            
            
            'policyScope': 'str',
            
            
            'scopeWirelessSegment': 'str'
            
        }

        self.attributeMap = {
            
            'action': 'action',
            
            'policyScope': 'policyScope',
            
            'scopeWirelessSegment': 'scopeWirelessSegment'
            
        }       

        
        #One of {ABORT, ABORT-RESTORE-TO-ORIGINAL}
        
        self.action = None # str
        
        #Policy scope
        
        self.policyScope = None # str
        
        #Scope wireless segment
        
        self.scopeWirelessSegment = None # str
        
