#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ScalableGroupDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'name': 'str',
            
            
            'id': 'str',
            
            
            'state': 'str'
            
        }

        self.attributeMap = {
            
            'name': 'name',
            
            'id': 'id',
            
            'state': 'state'
            
        }       

        
        #name
        
        self.name = None # str
        
        #id
        
        self.id = None # str
        
        #state
        
        self.state = None # str
        
