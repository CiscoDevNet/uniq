#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class NetworkUser(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'userIdentifiers': 'list[str]',
            
            
            'deviceTypes': 'list[str]',
            
            
            'locations': 'list[str]',
            
            
            'applications': 'list[PolicyApplication]',
            
            
            'applicationDiffs': 'list[PolicyApplicationDiffDTO]',
            
            
            'categories': 'list[CategoryDTO]'
            
        }

        self.attributeMap = {
            
            'userIdentifiers': 'userIdentifiers',
            
            'deviceTypes': 'deviceTypes',
            
            'locations': 'locations',
            
            'applications': 'applications',
            
            'applicationDiffs': 'applicationDiffs',
            
            'categories': 'categories'
            
        }       

        
        
        self.userIdentifiers = None # list[str]
        
        
        self.deviceTypes = None # list[str]
        
        
        self.locations = None # list[str]
        
        
        self.applications = None # list[PolicyApplication]
        
        
        self.applicationDiffs = None # list[PolicyApplicationDiffDTO]
        
        
        self.categories = None # list[CategoryDTO]
        
