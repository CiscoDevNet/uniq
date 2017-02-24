#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class BandwidthProfileAssociatedPolicyScopeDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'policyScope': 'str',
            
            
            'stale': 'bool'
            
        }

        self.attributeMap = {
            
            'policyScope': 'policyScope',
            
            'stale': 'stale'
            
        }       

        
        #Policy scope using this BandwidthProfile
        
        self.policyScope = None # str
        
        #Flag indicating whether the BandwidthProfile has been updated since the last time its associated policies were provisioned
        
        self.stale = None # bool
        
