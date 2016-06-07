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

class PerfMonitorStatistics(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'destIpAddress': 'str',


            'sourcePort': 'str',


            'destPort': 'str',


            'sourceIpAddress': 'str',


            'byteRate': 'int',


            'inputInterface': 'str',


            'ipv4DSCP': 'str',


            'ipv4TTL': 'int',


            'outputInterface': 'str',


            'packetCount': 'int',


            'packetLoss': 'int',


            'packetLossPercentage': 'float',


            'refreshedAt': 'int',


            'rtpJitterMax': 'int',


            'rtpJitterMean': 'int',


            'rtpJitterMin': 'int',


            'protocol': 'str'

        }

        self.attributeMap = {

            'destIpAddress': 'destIpAddress',

            'sourcePort': 'sourcePort',

            'destPort': 'destPort',

            'sourceIpAddress': 'sourceIpAddress',

            'byteRate': 'byteRate',

            'inputInterface': 'inputInterface',

            'ipv4DSCP': 'ipv4DSCP',

            'ipv4TTL': 'ipv4TTL',

            'outputInterface': 'outputInterface',

            'packetCount': 'packetCount',

            'packetLoss': 'packetLoss',

            'packetLossPercentage': 'packetLossPercentage',

            'refreshedAt': 'refreshedAt',

            'rtpJitterMax': 'rtpJitterMax',

            'rtpJitterMean': 'rtpJitterMean',

            'rtpJitterMin': 'rtpJitterMin',

            'protocol': 'protocol'

        }



        self.destIpAddress = None # str


        self.sourcePort = None # str


        self.destPort = None # str


        self.sourceIpAddress = None # str


        self.byteRate = None # int


        self.inputInterface = None # str


        self.ipv4DSCP = None # str


        self.ipv4TTL = None # int


        self.outputInterface = None # str


        self.packetCount = None # int


        self.packetLoss = None # int


        self.packetLossPercentage = None # float


        self.refreshedAt = None # int


        self.rtpJitterMax = None # int


        self.rtpJitterMean = None # int


        self.rtpJitterMin = None # int


        self.protocol = None # str

