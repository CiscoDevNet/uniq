#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class TopologyPageDto(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'applicationUuid': 'str',
            
            
            'name': 'str',
            
            
            'description': 'str',
            
            
            'id': 'str',
            
            
            'defaultViewId': 'str'
            
        }

        self.attributeMap = {
            
            'applicationUuid': 'applicationUuid',
            
            'name': 'name',
            
            'description': 'description',
            
            'id': 'id',
            
            'defaultViewId': 'defaultViewId'
            
        }       

        
        #Application unique identifier for this Page
        
        self.applicationUuid = None # str
        
        #Name for this Page
        
        self.name = None # str
        
        #Description for this Page
        
        self.description = None # str
        
        #Unique identifier for this Page
        
        self.id = None # str
        
        #Default View unique identifier for this Page
        
        self.defaultViewId = None # str
        
