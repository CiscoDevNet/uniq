#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class Constructor(object):


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
            
            
            'typeParameters': 'list[TypeVariable]',
            
            
            'declaringClass': 'Class«object»',
            
            
            'declaredAnnotations': 'list[Annotation]',
            
            
            'parameterTypes': 'list[Class]',
            
            
            'genericParameterTypes': 'list[Type]',
            
            
            'exceptionTypes': 'list[Class]',
            
            
            'genericExceptionTypes': 'list[Type]',
            
            
            'varArgs': 'bool',
            
            
            'parameterAnnotations': 'list[Array]',
            
            
            'annotations': 'list[Annotation]',
            
            
            'accessible': 'bool'
            
        }

        self.attributeMap = {
            
            'modifiers': 'modifiers',
            
            'name': 'name',
            
            'synthetic': 'synthetic',
            
            'typeParameters': 'typeParameters',
            
            'declaringClass': 'declaringClass',
            
            'declaredAnnotations': 'declaredAnnotations',
            
            'parameterTypes': 'parameterTypes',
            
            'genericParameterTypes': 'genericParameterTypes',
            
            'exceptionTypes': 'exceptionTypes',
            
            'genericExceptionTypes': 'genericExceptionTypes',
            
            'varArgs': 'varArgs',
            
            'parameterAnnotations': 'parameterAnnotations',
            
            'annotations': 'annotations',
            
            'accessible': 'accessible'
            
        }       

        
        
        self.modifiers = None # int
        
        
        self.name = None # str
        
        
        self.synthetic = None # bool
        
        
        self.typeParameters = None # list[TypeVariable]
        
        
        self.declaringClass = None # Class«object»
        
        
        self.declaredAnnotations = None # list[Annotation]
        
        
        self.parameterTypes = None # list[Class]
        
        
        self.genericParameterTypes = None # list[Type]
        
        
        self.exceptionTypes = None # list[Class]
        
        
        self.genericExceptionTypes = None # list[Type]
        
        
        self.varArgs = None # bool
        
        
        self.parameterAnnotations = None # list[Array]
        
        
        self.annotations = None # list[Annotation]
        
        
        self.accessible = None # bool
        
