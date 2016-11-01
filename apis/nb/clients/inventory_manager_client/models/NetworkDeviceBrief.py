#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class NetworkDeviceBrief(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'id': 'str',
            
            
            'hostName': 'str'
            
        }

        self.attributeMap = {
            
            'id': 'id',
            
            'hostName': 'hostName'
            
        }       

        
        
        self.id = None # str
        
        
        self.hostName = None # str
        
