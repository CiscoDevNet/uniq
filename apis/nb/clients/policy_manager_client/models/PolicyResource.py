#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PolicyResource(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'trafficClasses': 'str',
            
            
            'categories': 'list[CategoryDTO]',
            
            
            'applications': 'list[PolicyApplication]',
            
            
            'userIdentifiers': 'list[str]',
            
            
            'deviceTypes': 'list[str]',
            
            
            'locations': 'list[str]',
            
            
            'applicationDiffs': 'list[PolicyApplicationDiffDTO]'
            
        }

        self.attributeMap = {
            
            'trafficClasses': 'trafficClasses',
            
            'categories': 'categories',
            
            'applications': 'applications',
            
            'userIdentifiers': 'userIdentifiers',
            
            'deviceTypes': 'deviceTypes',
            
            'locations': 'locations',
            
            'applicationDiffs': 'applicationDiffs'
            
        }       

        
        #Traffic classes to set the bandwidth profile for. If the ActionProperty is BandwidthProfileId, this resource should be &#39;ALL_TRAFFIC_CLASSES&#39;. Otherwise, it should be null.
        
        self.trafficClasses = None # str
        
        
        self.categories = None # list[CategoryDTO]
        
        
        self.applications = None # list[PolicyApplication]
        
        
        self.userIdentifiers = None # list[str]
        
        
        self.deviceTypes = None # list[str]
        
        
        self.locations = None # list[str]
        
        
        self.applicationDiffs = None # list[PolicyApplicationDiffDTO]
        
