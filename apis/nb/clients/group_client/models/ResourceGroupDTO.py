#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ResourceGroupDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'groupTypeList': 'list[str]',
            
            
            'name': 'str',
            
            
            'id': 'str'
            
        }

        self.attributeMap = {
            
            'groupTypeList': 'groupTypeList',
            
            'name': 'name',
            
            'id': 'id'
            
        }       

        
        
        self.groupTypeList = None # list[str]
        
        
        self.name = None # str
        
        
        self.id = None # str
        
