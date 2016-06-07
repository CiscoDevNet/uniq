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

class InventoryRequest(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'enablePasswordList': 'list[str]',


            'passwordList': 'list[str]',


            'userNameList': 'list[str]',


            'protocolOrder': 'str',


            'cdpLevel': 'int',


            'retry': 'int',


            'reDiscovery': 'bool',


            'snmpAuthProtocol': 'str',


            'snmpAuthPassphrase': 'str',


            'snmpPrivProtocol': 'str',


            'snmpPrivPassphrase': 'str',


            'snmpROCommunity': 'str',


            'snmpRWCommunity': 'str',


            'snmpUserName': 'str',


            'name': 'str',


            'timeout': 'int',


            'snmpVersion': 'str',


            'discoveryType': 'str',


            'ipAddressList': 'str',


            'snmpMode': 'str'

        }

        self.attributeMap = {

            'enablePasswordList': 'enablePasswordList',

            'passwordList': 'passwordList',

            'userNameList': 'userNameList',

            'protocolOrder': 'protocolOrder',

            'cdpLevel': 'cdpLevel',

            'retry': 'retry',

            'reDiscovery': 'reDiscovery',

            'snmpAuthProtocol': 'snmpAuthProtocol',

            'snmpAuthPassphrase': 'snmpAuthPassphrase',

            'snmpPrivProtocol': 'snmpPrivProtocol',

            'snmpPrivPassphrase': 'snmpPrivPassphrase',

            'snmpROCommunity': 'snmpROCommunity',

            'snmpRWCommunity': 'snmpRWCommunity',

            'snmpUserName': 'snmpUserName',

            'name': 'name',

            'timeout': 'timeout',

            'snmpVersion': 'snmpVersion',

            'discoveryType': 'discoveryType',

            'ipAddressList': 'ipAddressList',

            'snmpMode': 'snmpMode'

        }



        self.enablePasswordList = None # list[str]


        self.passwordList = None # list[str]


        self.userNameList = None # list[str]


        self.protocolOrder = None # str


        self.cdpLevel = None # int


        self.retry = None # int


        self.reDiscovery = None # bool


        self.snmpAuthProtocol = None # str


        self.snmpAuthPassphrase = None # str


        self.snmpPrivProtocol = None # str


        self.snmpPrivPassphrase = None # str


        self.snmpROCommunity = None # str


        self.snmpRWCommunity = None # str


        self.snmpUserName = None # str


        self.name = None # str


        self.timeout = None # int


        self.snmpVersion = None # str

        #Available types are: single, auto cdp discovery, range, multi range

        self.discoveryType = None # str

        #

        self.ipAddressList = None # str


        self.snmpMode = None # str

