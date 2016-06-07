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

class NetworkDeviceReachabilityInfoNIO(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'discoveryId': 'str',


            'protocolUsed': 'str',


            'discoveryStartTime': 'str',


            'mgmtIp': 'str',


            'protocolList': 'str',


            'snmpCommunity': 'str',


            'userName': 'str',


            'password': 'str',


            'id': 'str',


            'enablePassword': 'str',


            'reachabilityFailureReason': 'str',


            'reachabilityStatus': 'str',


            'attributeInfo': 'object'

        }

        self.attributeMap = {

            'discoveryId': 'discoveryId',

            'protocolUsed': 'protocolUsed',

            'discoveryStartTime': 'discoveryStartTime',

            'mgmtIp': 'mgmtIp',

            'protocolList': 'protocolList',

            'snmpCommunity': 'snmpCommunity',

            'userName': 'userName',

            'password': 'password',

            'id': 'id',

            'enablePassword': 'enablePassword',

            'reachabilityFailureReason': 'reachabilityFailureReason',

            'reachabilityStatus': 'reachabilityStatus',

            'attributeInfo': 'attributeInfo'

        }



        self.discoveryId = None # str


        self.protocolUsed = None # str


        self.discoveryStartTime = None # str


        self.mgmtIp = None # str


        self.protocolList = None # str


        self.snmpCommunity = None # str


        self.userName = None # str


        self.password = None # str


        self.id = None # str


        self.enablePassword = None # str


        self.reachabilityFailureReason = None # str


        self.reachabilityStatus = None # str


        self.attributeInfo = None # object

