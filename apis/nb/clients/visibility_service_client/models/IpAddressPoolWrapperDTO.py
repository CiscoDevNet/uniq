#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class IpAddressPoolWrapperDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'genericPools': 'list[GenericIpAddressPoolDTO]',
            
            
            'skipOverlapCheck': 'bool',
            
            
            'siteSpecificPools': 'list[SiteIPAddressPoolDTO]'
            
        }

        self.attributeMap = {
            
            'genericPools': 'genericPools',
            
            'skipOverlapCheck': 'skipOverlapCheck',
            
            'siteSpecificPools': 'siteSpecificPools'
            
        }       

        
        
        self.genericPools = None # list[GenericIpAddressPoolDTO]
        
        
        self.skipOverlapCheck = None # bool
        
        
        self.siteSpecificPools = None # list[SiteIPAddressPoolDTO]
        
