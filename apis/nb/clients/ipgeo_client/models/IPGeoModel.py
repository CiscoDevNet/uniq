#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class IPGeoModel(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'latitude': 'str',
            
            
            'longitude': 'str',
            
            
            'city': 'str',
            
            
            'continent': 'str',
            
            
            'continentCode': 'str',
            
            
            'subDivision': 'str',
            
            
            'subDivisionCode': 'str',
            
            
            'countryCode': 'str',
            
            
            'country': 'str'
            
        }

        self.attributeMap = {
            
            'latitude': 'latitude',
            
            'longitude': 'longitude',
            
            'city': 'city',
            
            'continent': 'continent',
            
            'continentCode': 'continentCode',
            
            'subDivision': 'subDivision',
            
            'subDivisionCode': 'subDivisionCode',
            
            'countryCode': 'countryCode',
            
            'country': 'country'
            
        }       

        
        
        self.latitude = None # str
        
        
        self.longitude = None # str
        
        
        self.city = None # str
        
        
        self.continent = None # str
        
        
        self.continentCode = None # str
        
        
        self.subDivision = None # str
        
        
        self.subDivisionCode = None # str
        
        
        self.countryCode = None # str
        
        
        self.country = None # str
        
