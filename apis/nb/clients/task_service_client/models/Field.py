#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class Field(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'modifiers': 'int',
            
            
            'name': 'str',
            
            
            'synthetic': 'bool',
            
            
            'declaringClass': 'Class«object»',
            
            
            'declaredAnnotations': 'list[Annotation]',
            
            
            'enumConstant': 'bool',
            
            
            'type': 'Class«object»',
            
            
            'genericType': 'Type',
            
            
            'annotations': 'list[Annotation]',
            
            
            'accessible': 'bool'
            
        }

        self.attributeMap = {
            
            'modifiers': 'modifiers',
            
            'name': 'name',
            
            'synthetic': 'synthetic',
            
            'declaringClass': 'declaringClass',
            
            'declaredAnnotations': 'declaredAnnotations',
            
            'enumConstant': 'enumConstant',
            
            'type': 'type',
            
            'genericType': 'genericType',
            
            'annotations': 'annotations',
            
            'accessible': 'accessible'
            
        }       

        
        
        self.modifiers = None # int
        
        
        self.name = None # str
        
        
        self.synthetic = None # bool
        
        
        self.declaringClass = None # Class«object»
        
        
        self.declaredAnnotations = None # list[Annotation]
        
        
        self.enumConstant = None # bool
        
        
        self.type = None # Class«object»
        
        
        self.genericType = None # Type
        
        
        self.annotations = None # list[Annotation]
        
        
        self.accessible = None # bool
        
