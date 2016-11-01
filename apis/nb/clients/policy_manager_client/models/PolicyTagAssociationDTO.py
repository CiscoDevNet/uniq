#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PolicyTagAssociationDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'networkDevices': 'list[PolicyTagAssociationDeviceDTO]',
            
            
            'policyTag': 'str',
            
            
            'unModifiable': 'bool',
            
            
            'unModifiableReason': 'str'
            
        }

        self.attributeMap = {
            
            'networkDevices': 'networkDevices',
            
            'policyTag': 'policyTag',
            
            'unModifiable': 'unModifiable',
            
            'unModifiableReason': 'unModifiableReason'
            
        }       

        
        
        self.networkDevices = None # list[PolicyTagAssociationDeviceDTO]
        
        
        self.policyTag = None # str
        
        
        self.unModifiable = None # bool
        
        
        self.unModifiableReason = None # str
        
