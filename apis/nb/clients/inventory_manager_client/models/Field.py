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

