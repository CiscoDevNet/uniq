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

class InterfaceStatistics(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'adminStatus': 'str',


            'inputPackets': 'int',


            'inputQueueCount': 'int',


            'inputQueueDrops': 'int',


            'inputQueueFlushes': 'int',


            'inputQueueMaxDepth': 'int',


            'inputRatebps': 'int',


            'operationalStatus': 'str',


            'outputDrop': 'int',


            'outputPackets': 'int',


            'outputQueueCount': 'int',


            'outputQueueDepth': 'int',


            'outputRatebps': 'int',


            'refreshedAt': 'int'

        }

        self.attributeMap = {

            'adminStatus': 'adminStatus',

            'inputPackets': 'inputPackets',

            'inputQueueCount': 'inputQueueCount',

            'inputQueueDrops': 'inputQueueDrops',

            'inputQueueFlushes': 'inputQueueFlushes',

            'inputQueueMaxDepth': 'inputQueueMaxDepth',

            'inputRatebps': 'inputRatebps',

            'operationalStatus': 'operationalStatus',

            'outputDrop': 'outputDrop',

            'outputPackets': 'outputPackets',

            'outputQueueCount': 'outputQueueCount',

            'outputQueueDepth': 'outputQueueDepth',

            'outputRatebps': 'outputRatebps',

            'refreshedAt': 'refreshedAt'

        }



        self.adminStatus = None # str


        self.inputPackets = None # int


        self.inputQueueCount = None # int


        self.inputQueueDrops = None # int


        self.inputQueueFlushes = None # int


        self.inputQueueMaxDepth = None # int


        self.inputRatebps = None # int


        self.operationalStatus = None # str


        self.outputDrop = None # int


        self.outputPackets = None # int


        self.outputQueueCount = None # int


        self.outputQueueDepth = None # int


        self.outputRatebps = None # int


        self.refreshedAt = None # int

