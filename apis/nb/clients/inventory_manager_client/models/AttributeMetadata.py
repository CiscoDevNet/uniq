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

class AttributeMetadata(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'collectionImplType': 'Class«object»',


            'attribute': 'bool',


            'defaultValue': 'object',


            'required': 'bool',


            'collectionInterfaceType': 'Class«object»',


            'associationEnd': 'bool',


            'minCardinality': 'int',


            'maxCardinality': 'int',


            'unique': 'bool',


            'name': 'str',


            'collection': 'bool',


            'ordered': 'bool',


            'version': 'str',


            'description': 'str',


            'type': 'Class',


            'stereotypes': 'list[AbstractStereotype]'

        }

        self.attributeMap = {

            'collectionImplType': 'collectionImplType',

            'attribute': 'attribute',

            'defaultValue': 'defaultValue',

            'required': 'required',

            'collectionInterfaceType': 'collectionInterfaceType',

            'associationEnd': 'associationEnd',

            'minCardinality': 'minCardinality',

            'maxCardinality': 'maxCardinality',

            'unique': 'unique',

            'name': 'name',

            'collection': 'collection',

            'ordered': 'ordered',

            'version': 'version',

            'description': 'description',

            'type': 'type',

            'stereotypes': 'stereotypes'

        }



        self.collectionImplType = None # Class«object»


        self.attribute = None # bool


        self.defaultValue = None # object


        self.required = None # bool


        self.collectionInterfaceType = None # Class«object»


        self.associationEnd = None # bool


        self.minCardinality = None # int


        self.maxCardinality = None # int


        self.unique = None # bool


        self.name = None # str


        self.collection = None # bool


        self.ordered = None # bool


        self.version = None # str


        self.description = None # str


        self.type = None # Class


        self.stereotypes = None # list[AbstractStereotype]

