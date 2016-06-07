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

class DiscoveryNIO(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'protocolOrder': 'str',


            'cdpLevel': 'int',


            'discoveryCondition': 'str',


            'userNameList': 'str',


            'passwordList': 'str',


            'parentDiscoveryId': 'str',


            'snmpRoCommunity': 'str',


            'snmpRwCommunity': 'str',


            'isAutoCdp': 'bool',


            'enablePasswordList': 'str',


            'numDevices': 'int',


            'name': 'str',


            'id': 'str',


            'timeOut': 'int',


            'discoveryType': 'str',


            'retryCount': 'int',


            'ipAddressList': 'str',


            'deviceIds': 'str',


            'discoveryStatus': 'str',


            'attributeInfo': 'object'

        }

        self.attributeMap = {

            'protocolOrder': 'protocolOrder',

            'cdpLevel': 'cdpLevel',

            'discoveryCondition': 'discoveryCondition',

            'userNameList': 'userNameList',

            'passwordList': 'passwordList',

            'parentDiscoveryId': 'parentDiscoveryId',

            'snmpRoCommunity': 'snmpRoCommunity',

            'snmpRwCommunity': 'snmpRwCommunity',

            'isAutoCdp': 'isAutoCdp',

            'enablePasswordList': 'enablePasswordList',

            'numDevices': 'numDevices',

            'name': 'name',

            'id': 'id',

            'timeOut': 'timeOut',

            'discoveryType': 'discoveryType',

            'retryCount': 'retryCount',

            'ipAddressList': 'ipAddressList',

            'deviceIds': 'deviceIds',

            'discoveryStatus': 'discoveryStatus',

            'attributeInfo': 'attributeInfo'

        }



        self.protocolOrder = None # str


        self.cdpLevel = None # int

        #Complete or In Progress

        self.discoveryCondition = None # str


        self.userNameList = None # str


        self.passwordList = None # str


        self.parentDiscoveryId = None # str


        self.snmpRoCommunity = None # str


        self.snmpRwCommunity = None # str


        self.isAutoCdp = None # bool


        self.enablePasswordList = None # str


        self.numDevices = None # int


        self.name = None # str


        self.id = None # str


        self.timeOut = None # int

        #Available types are: single, auto cdp discovery, range, multi range

        self.discoveryType = None # str


        self.retryCount = None # int


        self.ipAddressList = None # str


        self.deviceIds = None # str

        #Available options are: active, inactive

        self.discoveryStatus = None # str


        self.attributeInfo = None # object

