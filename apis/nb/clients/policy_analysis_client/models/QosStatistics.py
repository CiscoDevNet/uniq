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

class QosStatistics(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'timeStamp': 'int',


            'classMap': 'str',


            'dropRate': 'int',


            'numBytes': 'int',


            'numPackets': 'int',


            'offeredRate': 'int',


            'queueBandwidthbps': 'int',


            'queueDepth': 'int',


            'queueNoBufferDrops': 'int',


            'queueTotalDrops': 'int'

        }

        self.attributeMap = {

            'timeStamp': 'timeStamp',

            'classMap': 'classMap',

            'dropRate': 'dropRate',

            'numBytes': 'numBytes',

            'numPackets': 'numPackets',

            'offeredRate': 'offeredRate',

            'queueBandwidthbps': 'queueBandwidthbps',

            'queueDepth': 'queueDepth',

            'queueNoBufferDrops': 'queueNoBufferDrops',

            'queueTotalDrops': 'queueTotalDrops'

        }



        self.timeStamp = None  # int


        self.classMap = None  # str


        self.dropRate = None  # int


        self.numBytes = None  # int


        self.numPackets = None  # int


        self.offeredRate = None  # int


        self.queueBandwidthbps = None  # int


        self.queueDepth = None  # int


        self.queueNoBufferDrops = None  # int


        self.queueTotalDrops = None  # int

