#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class NeighborhoodDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'type': 'str',
            
            
            'name': 'str',
            
            
            'description': 'str',
            
            
            'id': 'str',
            
            
            'listofScalableGroups': 'list[str]'
            
        }

        self.attributeMap = {
            
            'type': 'type',
            
            'name': 'name',
            
            'description': 'description',
            
            'id': 'id',
            
            'listofScalableGroups': 'listofScalableGroups'
            
        }       

        
        #Isolation Property
        
        self.type = None # str
        
        #Neighborhood Name
        
        self.name = None # str
        
        #Description of the group
        
        self.description = None # str
        
        #UUID of the Neighborhood
        
        self.id = None # str
        
        #List of Scalable Groups
        
        self.listofScalableGroups = None # list[str]
        
