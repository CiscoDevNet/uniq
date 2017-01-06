#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ZtdTemplateConfig(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'description': 'str',
            
            
            'id': 'str',
            
            
            'templateId': 'str',
            
            
            'configId': 'str',
            
            
            'configProperty': 'dict',
            
            
            'generate': 'bool',
            
            
            'name': 'str'
            
        }

        self.attributeMap = {
            
            'description': 'description',
            
            'id': 'id',
            
            'templateId': 'templateId',
            
            'configId': 'configId',
            
            'configProperty': 'configProperty',
            
            'generate': 'generate',
            
            'name': 'name'
            
        }       

        
        #Template config description
        
        self.description = None # str
        
        #Template config ID
        
        self.id = None # str
        
        #Template ID
        
        self.templateId = None # str
        
        
        self.configId = None # str
        
        #Template varialble key-value pairs
        
        self.configProperty = None # dict
        
        #True to generate template
        
        self.generate = None # bool
        
        #Template config name
        
        self.name = None # str
        
