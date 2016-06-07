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

class RawCliInfoNIO(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'snmp': 'str',


            'macAddressTable': 'str',


            'inventory': 'str',


            'intfDescription': 'str',


            'healthMonitor': 'str',


            'ipIntfBrief': 'str',


            'version': 'str',


            'id': 'str',


            'cdpNeighbors': 'str',


            'runningConfig': 'str',


            'attributeInfo': 'object'

        }

        self.attributeMap = {

            'snmp': 'snmp',

            'macAddressTable': 'macAddressTable',

            'inventory': 'inventory',

            'intfDescription': 'intfDescription',

            'healthMonitor': 'healthMonitor',

            'ipIntfBrief': 'ipIntfBrief',

            'version': 'version',

            'id': 'id',

            'cdpNeighbors': 'cdpNeighbors',

            'runningConfig': 'runningConfig',

            'attributeInfo': 'attributeInfo'

        }


        #SNMP configuration info of the device

        self.snmp = None # str

        #MAC address configuration info of the device

        self.macAddressTable = None # str

        #Inventory configuration info of the device

        self.inventory = None # str

        #Interface configuration info of the device

        self.intfDescription = None # str

        #Health monitor configuration info of the device

        self.healthMonitor = None # str

        #IP interface brief configuration info of the device

        self.ipIntfBrief = None # str

        #Version configuration info of the device

        self.version = None # str

        #Unique identifier for config

        self.id = None # str

        #CDP configuration info of the device

        self.cdpNeighbors = None # str

        #Running-config of the device

        self.runningConfig = None # str


        self.attributeInfo = None # object

