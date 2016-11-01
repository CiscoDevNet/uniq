#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class IwanPhysicalServiceProviderDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'classModelType': 'str',
            
            
            'classModels': 'list[IwanPhysicalServiceProviderClassModelDTO]',
            
            
            'wanType': 'str',
            
            
            'vendor': 'str',
            
            
            'defaultModel': 'str',
            
            
            'name': 'str'
            
        }

        self.attributeMap = {
            
            'classModelType': 'classModelType',
            
            'classModels': 'classModels',
            
            'wanType': 'wanType',
            
            'vendor': 'vendor',
            
            'defaultModel': 'defaultModel',
            
            'name': 'name'
            
        }       

        
        
        self.classModelType = None # str
        
        
        self.classModels = None # list[IwanPhysicalServiceProviderClassModelDTO]
        
        
        self.wanType = None # str
        
        
        self.vendor = None # str
        
        
        self.defaultModel = None # str
        
        
        self.name = None # str
        
