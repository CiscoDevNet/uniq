#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class Method(object):


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
            
            
            'returnType': 'Class«object»',
            
            
            'parameterTypes': 'list[Class]',
            
            
            'genericReturnType': 'Type',
            
            
            'genericParameterTypes': 'list[Type]',
            
            
            'exceptionTypes': 'list[Class]',
            
            
            'genericExceptionTypes': 'list[Type]',
            
            
            'bridge': 'bool',
            
            
            'varArgs': 'bool',
            
            
            'defaultValue': 'dict',
            
            
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
            
            'returnType': 'returnType',
            
            'parameterTypes': 'parameterTypes',
            
            'genericReturnType': 'genericReturnType',
            
            'genericParameterTypes': 'genericParameterTypes',
            
            'exceptionTypes': 'exceptionTypes',
            
            'genericExceptionTypes': 'genericExceptionTypes',
            
            'bridge': 'bridge',
            
            'varArgs': 'varArgs',
            
            'defaultValue': 'defaultValue',
            
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
        
        
        self.returnType = None # Class«object»
        
        
        self.parameterTypes = None # list[Class]
        
        
        self.genericReturnType = None # Type
        
        
        self.genericParameterTypes = None # list[Type]
        
        
        self.exceptionTypes = None # list[Class]
        
        
        self.genericExceptionTypes = None # list[Type]
        
        
        self.bridge = None # bool
        
        
        self.varArgs = None # bool
        
        
        self.defaultValue = None # dict
        
        
        self.parameterAnnotations = None # list[Array]
        
        
        self.annotations = None # list[Annotation]
        
        
        self.accessible = None # bool
        
