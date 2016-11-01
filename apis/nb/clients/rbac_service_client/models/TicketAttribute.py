#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class TicketAttribute(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'attribute': 'str',
            
            
            'value': 'int'
            
        }

        self.attributeMap = {
            
            'attribute': 'attribute',
            
            'value': 'value'
            
        }       

        
        #Service Ticket Attribute Name
        
        self.attribute = None # str
        
        #Service Ticket Attribute Value
        
        self.value = None # int
        
