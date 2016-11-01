#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class UnclaimedDeviceDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'siteName': 'str',
            
            
            'latitude': 'str',
            
            
            'longitude': 'str',
            
            
            'siteLocation': 'str',
            
            
            'siteDevice': 'SiteDeviceDTO'
            
        }

        self.attributeMap = {
            
            'siteName': 'siteName',
            
            'latitude': 'latitude',
            
            'longitude': 'longitude',
            
            'siteLocation': 'siteLocation',
            
            'siteDevice': 'siteDevice'
            
        }       

        
        
        self.siteName = None # str
        
        
        self.latitude = None # str
        
        
        self.longitude = None # str
        
        
        self.siteLocation = None # str
        
        
        self.siteDevice = None # SiteDeviceDTO
        
