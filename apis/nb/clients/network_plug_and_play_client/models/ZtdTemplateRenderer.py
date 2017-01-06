#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ZtdTemplateRenderer(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'id': 'str',
            
            
            'fileId': 'str',
            
            
            'configProperty': 'dict',
            
            
            'generatedContent': 'str'
            
        }

        self.attributeMap = {
            
            'id': 'id',
            
            'fileId': 'fileId',
            
            'configProperty': 'configProperty',
            
            'generatedContent': 'generatedContent'
            
        }       

        
        #Template Renderer ID
        
        self.id = None # str
        
        
        self.fileId = None # str
        
        
        self.configProperty = None # dict
        
        
        self.generatedContent = None # str
        
