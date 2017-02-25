#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class LocationNIO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'civicAddress': 'str',
            
            
            'description': 'str',
            
            
            'geographicalAddress': 'str',
            
            
            'locationName': 'str',
            
            
            'id': 'str',
            
            
            'tag': 'str'
            
        }

        self.attributeMap = {
            
            'civicAddress': 'civicAddress',
            
            'description': 'description',
            
            'geographicalAddress': 'geographicalAddress',
            
            'locationName': 'locationName',
            
            'id': 'id',
            
            'tag': 'tag'
            
        }       

        
        #Civic address of the location
        
        self.civicAddress = None # str
        
        #Description of the location
        
        self.description = None # str
        
        #Geographic address of the location
        
        self.geographicalAddress = None # str
        
        #Name of the location
        
        self.locationName = None # str
        
        #Unique identifier for location
        
        self.id = None # str
        
        #Tag associated with the location
        
        self.tag = None # str
        
