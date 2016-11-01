#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class NetworkDeviceBriefNIO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'id': 'str',
            
            
            'role': 'str',
            
            
            'roleSource': 'str'
            
        }

        self.attributeMap = {
            
            'id': 'id',
            
            'role': 'role',
            
            'roleSource': 'roleSource'
            
        }       

        
        #Unique identifier of the network device
        
        self.id = None # str
        
        #Role of device as access, distribution, border router, core
        
        self.role = None # str
        
        #Role source as manual / auto
        
        self.roleSource = None # str
        
