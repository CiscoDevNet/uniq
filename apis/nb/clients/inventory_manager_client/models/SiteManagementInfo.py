#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class SiteManagementInfo(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'deviceIds': 'list[str]',
            
            
            'name': 'str',
            
            
            'location': 'str',
            
            
            'properties': 'dict',
            
            
            'id': 'str',
            
            
            'description': 'str'
            
        }

        self.attributeMap = {
            
            'deviceIds': 'deviceIds',
            
            'name': 'name',
            
            'location': 'location',
            
            'properties': 'properties',
            
            'id': 'id',
            
            'description': 'description'
            
        }       

        
        #Unique identifier of devices that are associated with site
        
        self.deviceIds = None # list[str]
        
        #Name of site
        
        self.name = None # str
        
        #Location of site
        
        self.location = None # str
        
        #Properties of site
        
        self.properties = None # dict
        
        #Unique identifier of site
        
        self.id = None # str
        
        #Description of site
        
        self.description = None # str
        
