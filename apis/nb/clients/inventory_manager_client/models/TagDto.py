#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class TagDto(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'id': 'str',
            
            
            'resourceId': 'str',
            
            
            'tag': 'str',
            
            
            'resourceType': 'str'
            
        }

        self.attributeMap = {
            
            'id': 'id',
            
            'resourceId': 'resourceId',
            
            'tag': 'tag',
            
            'resourceType': 'resourceType'
            
        }       

        
        #Unique identifier for tag
        
        self.id = None # str
        
        #Id of the resource to which the tag to be associated
        
        self.resourceId = None # str
        
        #Name of the tag
        
        self.tag = None # str
        
        #Type of the resource to which the tag to be associated
        
        self.resourceType = None # str
        
