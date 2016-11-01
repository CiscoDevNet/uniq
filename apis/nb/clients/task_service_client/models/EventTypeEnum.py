#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class EventTypeEnum(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'ordinal': 'int',
            
            
            'value': 'str'
            
        }

        self.attributeMap = {
            
            'ordinal': 'ordinal',
            
            'value': 'value'
            
        }       

        
        
        self.ordinal = None # int
        
        
        self.value = None # str
        
