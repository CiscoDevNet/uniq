#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ClassModelDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'name': 'str',
            
            
            'dscp': 'str',
            
            
            'bandwidthPercentage': 'int',
            
            
            'admittedTrafficClasses': 'list[str]',
            
            
            'priority': 'bool'
            
        }

        self.attributeMap = {
            
            'name': 'name',
            
            'dscp': 'dscp',
            
            'bandwidthPercentage': 'bandwidthPercentage',
            
            'admittedTrafficClasses': 'admittedTrafficClasses',
            
            'priority': 'priority'
            
        }       

        
        #
        
        self.name = None # str
        
        #Valid values are from 0 to 63 inclusive
        
        self.dscp = None # str
        
        #Valid values are from 1 to 100 inclusive
        
        self.bandwidthPercentage = None # int
        
        #Valid values are broadcast-video, bulk-data, multimedia-conferencing, multimedia-streaming, network-control, ops-admin-mgmt, real-time-interactive, signaling, transactional-data, voip-telephony, best-effort, scavenger
        
        self.admittedTrafficClasses = None # list[str]
        
        #1 and Only 1 classModel in a given ServiceProviderProfile should have priority value as &#39;true&#39;
        
        self.priority = None # bool
        
