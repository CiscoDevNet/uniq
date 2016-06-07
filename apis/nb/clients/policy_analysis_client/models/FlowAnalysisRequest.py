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

class FlowAnalysisRequest(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'protocol': 'str',


            'sourceIP': 'str',


            'sourcePort': 'str',


            'destIP': 'str',


            'destPort': 'str',


            'periodicRefresh': 'bool',


            'inclusions': 'list[str]'

        }

        self.attributeMap = {

            'protocol': 'protocol',

            'sourceIP': 'sourceIP',

            'sourcePort': 'sourcePort',

            'destIP': 'destIP',

            'destPort': 'destPort',

            'periodicRefresh': 'periodicRefresh',

            'inclusions': 'inclusions'

        }


        #Protocol

        self.protocol = None # str

        #Source IP address

        self.sourceIP = None # str

        #Source Port

        self.sourcePort = None # str

        #Destination IP address

        self.destIP = None # str

        #Destination Port

        self.destPort = None # str

        #periodicRefresh of path for every 30 sec

        self.periodicRefresh = None # bool

        #Subset of {INTERFACE-STATS, QOS-STATS, DEVICE-STATS, PERFORMANCE-STATS}

        self.inclusions = None # list[str]

