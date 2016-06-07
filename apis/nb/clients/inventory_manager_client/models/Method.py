#!/usr/bin/env python
#pylint: skip-file
"""
Copyright 2016 Cisco Systems

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

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


            'defaultValue': 'object',


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


        self.defaultValue = None # object


        self.parameterAnnotations = None # list[Array]


        self.annotations = None # list[Annotation]


        self.accessible = None # bool

