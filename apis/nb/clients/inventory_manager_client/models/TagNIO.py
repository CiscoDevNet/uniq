#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class TagNIO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'locationId': 'str',
            
            
            'lastUpdated': 'str',
            
            
            'linkId': 'str',
            
            
            'id': 'str',
            
            
            'tag': 'str',
            
            
            'interfaceId': 'str',
            
            
            'networkDeviceId': 'str'
            
        }

        self.attributeMap = {
            
            'locationId': 'locationId',
            
            'lastUpdated': 'lastUpdated',
            
            'linkId': 'linkId',
            
            'id': 'id',
            
            'tag': 'tag',
            
            'interfaceId': 'interfaceId',
            
            'networkDeviceId': 'networkDeviceId'
            
        }       

        
        #Unique identifier of location
        
        self.locationId = None # str
        
        #Time when the device interface info last got updated
        
        self.lastUpdated = None # str
        
        #Unique identifier of link
        
        self.linkId = None # str
        
        #Unique identifier of tag
        
        self.id = None # str
        
        #Tag Id
        
        self.tag = None # str
        
        #Unique identifier of the interface
        
        self.interfaceId = None # str
        
        #Unique identifier of device
        
        self.networkDeviceId = None # str
        
