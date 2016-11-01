#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class TypeVariable(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'bounds': 'list[Type]',
            
            
            'genericDeclaration': 'GenericDeclaration',
            
            
            'name': 'str'
            
        }

        self.attributeMap = {
            
            'bounds': 'bounds',
            
            'genericDeclaration': 'genericDeclaration',
            
            'name': 'name'
            
        }       

        
        
        self.bounds = None # list[Type]
        
        
        self.genericDeclaration = None # GenericDeclaration
        
        
        self.name = None # str
        
