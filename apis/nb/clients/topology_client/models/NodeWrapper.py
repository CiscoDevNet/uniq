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

class NodeWrapper(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'role': 'str',


            'order': 'int',


            'id': 'str',


            'label': 'str',


            'roleSource': 'str',


            'customParam': 'NodeWrapperCustom',


            'greyOut': 'bool',


            'deviceType': 'str',


            'ip': 'str',


            'softwareVersion': 'str',


            'nodeType': 'str',


            'family': 'str',


            'platformId': 'str',


            'tags': 'list[str]',


            'aclApplied': 'bool',


            'dataPathId': 'str',


            'upperNode': 'str',


            'fixed': 'bool',


            'osType': 'str',


            'vlanId': 'str',


            'x': 'int',


            'y': 'int',


            'userId': 'str',


            'networkType': 'str'

        }

        self.attributeMap = {

            'role': 'role',

            'order': 'order',

            'id': 'id',

            'label': 'label',

            'roleSource': 'roleSource',

            'customParam': 'customParam',

            'greyOut': 'greyOut',

            'deviceType': 'deviceType',

            'ip': 'ip',

            'softwareVersion': 'softwareVersion',

            'nodeType': 'nodeType',

            'family': 'family',

            'platformId': 'platformId',

            'tags': 'tags',

            'aclApplied': 'aclApplied',

            'dataPathId': 'dataPathId',

            'upperNode': 'upperNode',

            'fixed': 'fixed',

            'osType': 'osType',

            'vlanId': 'vlanId',

            'x': 'x',

            'y': 'y',

            'userId': 'userId',

            'networkType': 'networkType'

        }


        #Role of the device

        self.role = None # str

        #Device order by link number

        self.order = None # int

        #Unique identifier for device

        self.id = None # str

        #Hostname of the device

        self.label = None # str

        #Indicates whether role is assigned manually or automatically

        self.roleSource = None # str

        #Device custom parameters

        self.customParam = None # NodeWrapperCustom

        #Indicates if the device is active for this topology view

        self.greyOut = None # bool

        #Type of the device

        self.deviceType = None # str

        #IP address of the device

        self.ip = None # str

        #Device OS version

        self.softwareVersion = None # str

        #Host or device

        self.nodeType = None # str

        #Product family which is part of the product identifier

        self.family = None # str

        #Device platform description

        self.platformId = None # str

        #List of tags applied on this device

        self.tags = None # list[str]

        #Indicates if the ACL that is applied on the device

        self.aclApplied = None # bool

        #ID of the path between devices

        self.dataPathId = None # str

        #Start node ID

        self.upperNode = None # str

        #Indication of whether the position is fixed or will use auto layout

        self.fixed = None # bool

        #OS type of the device

        self.osType = None # str

        #VLan id

        self.vlanId = None # str

        #X position of the device on the displayed topology view

        self.x = None # int

        #Y position of the device on the displayed topology view

        self.y = None # int

        #ID of the host

        self.userId = None # str

        #Type of network

        self.networkType = None # str

