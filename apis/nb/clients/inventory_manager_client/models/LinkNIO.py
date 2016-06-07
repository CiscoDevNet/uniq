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

class LinkNIO(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'id': 'str',


            'lastUpdated': 'str',


            'linkStatus': 'str',


            'numUpdates': 'int',


            'avgUpdateFrequency': 'int',


            'endDeviceHostName': 'str',


            'endDeviceId': 'str',


            'endPortId': 'str',


            'endDeviceIpAddress': 'str',


            'startDeviceId': 'str',


            'startPortId': 'str',


            'attributeInfo': 'object'

        }

        self.attributeMap = {

            'id': 'id',

            'lastUpdated': 'lastUpdated',

            'linkStatus': 'linkStatus',

            'numUpdates': 'numUpdates',

            'avgUpdateFrequency': 'avgUpdateFrequency',

            'endDeviceHostName': 'endDeviceHostName',

            'endDeviceId': 'endDeviceId',

            'endPortId': 'endPortId',

            'endDeviceIpAddress': 'endDeviceIpAddress',

            'startDeviceId': 'startDeviceId',

            'startPortId': 'startPortId',

            'attributeInfo': 'attributeInfo'

        }



        self.id = None # str


        self.lastUpdated = None # str


        self.linkStatus = None # str


        self.numUpdates = None # int


        self.avgUpdateFrequency = None # int


        self.endDeviceHostName = None # str


        self.endDeviceId = None # str


        self.endPortId = None # str


        self.endDeviceIpAddress = None # str


        self.startDeviceId = None # str


        self.startPortId = None # str


        self.attributeInfo = None # object

