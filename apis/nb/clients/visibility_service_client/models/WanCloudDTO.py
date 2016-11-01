#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class WanCloudDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'id': 'str',
            
            
            'wanType': 'str',
            
            
            'meterType': 'str',
            
            
            'label': 'str'
            
        }

        self.attributeMap = {
            
            'id': 'id',
            
            'wanType': 'wanType',
            
            'meterType': 'meterType',
            
            'label': 'label'
            
        }       

        
        
        self.id = None # str
        
        
        self.wanType = None # str
        
        
        self.meterType = None # str
        
        
        self.label = None # str
        
