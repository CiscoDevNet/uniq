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

class InstanceImpl(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'displayName': 'str',


            'entityClass': 'Class«InstanceImpl»',


            'instanceId': 'int',


            'classId': 'int',


            'authEntityId': 'int',


            'authEntityClass': 'int',


            'instanceUuid': 'str',


            'instanceVersion': 'int',


            'businessKey': 'str',


            '_orderedListOEIndex': 'int',


            '_orderedListOEAssocName': 'str',


            '_creationOrderIndex': 'int',


            '_isBeingChanged': 'bool',


            'internalKey': 'IdRef',


            'businessKeyAttributes': 'list[AttributeMetadata]',


            'displayNameAttributes': 'list[AttributeMetadata]',


            'alternateKeyAttributes': 'list[Entry«string,List«AttributeMetadata»»]',


            'entityMetadata': 'EntityMetadata',


            'propertyMetadataMap': 'list[Entry«string,PropertyMetadata»]',


            'componentName': 'str',


            'entityClassName': 'str',


            'entityClassSimpleName': 'str',


            'alternateKey': 'object',


            'businessKeyAttributeMap': 'list[Entry«AttributeMetadata,object»]'

        }

        self.attributeMap = {

            'displayName': 'displayName',

            'entityClass': 'entityClass',

            'instanceId': 'instanceId',

            'classId': 'classId',

            'authEntityId': 'authEntityId',

            'authEntityClass': 'authEntityClass',

            'instanceUuid': 'instanceUuid',

            'instanceVersion': 'instanceVersion',

            'businessKey': 'businessKey',

            '_orderedListOEIndex': '_orderedListOEIndex',

            '_orderedListOEAssocName': '_orderedListOEAssocName',

            '_creationOrderIndex': '_creationOrderIndex',

            '_isBeingChanged': '_isBeingChanged',

            'internalKey': 'internalKey',

            'businessKeyAttributes': 'businessKeyAttributes',

            'displayNameAttributes': 'displayNameAttributes',

            'alternateKeyAttributes': 'alternateKeyAttributes',

            'entityMetadata': 'entityMetadata',

            'propertyMetadataMap': 'propertyMetadataMap',

            'componentName': 'componentName',

            'entityClassName': 'entityClassName',

            'entityClassSimpleName': 'entityClassSimpleName',

            'alternateKey': 'alternateKey',

            'businessKeyAttributeMap': 'businessKeyAttributeMap'

        }



        self.displayName = None # str


        self.entityClass = None # Class«InstanceImpl»


        self.instanceId = None # int


        self.classId = None # int


        self.authEntityId = None # int


        self.authEntityClass = None # int


        self.instanceUuid = None # str


        self.instanceVersion = None # int


        self.businessKey = None # str


        self._orderedListOEIndex = None # int


        self._orderedListOEAssocName = None # str


        self._creationOrderIndex = None # int


        self._isBeingChanged = None # bool


        self.internalKey = None # IdRef


        self.businessKeyAttributes = None # list[AttributeMetadata]


        self.displayNameAttributes = None # list[AttributeMetadata]


        self.alternateKeyAttributes = None # list[Entry«string,List«AttributeMetadata»»]


        self.entityMetadata = None # EntityMetadata


        self.propertyMetadataMap = None # list[Entry«string,PropertyMetadata»]


        self.componentName = None # str


        self.entityClassName = None # str


        self.entityClassSimpleName = None # str


        self.alternateKey = None # object


        self.businessKeyAttributeMap = None # list[Entry«AttributeMetadata,object»]

