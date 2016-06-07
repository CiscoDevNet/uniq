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

class FlowAnalysis(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'status': 'str',


            'failureReason': 'str',


            'createTime': 'int',


            'lastUpdateTime': 'int',


            'id': 'str',


            'sourceIP': 'str',


            'destIP': 'str',


            'sourcePort': 'str',


            'destPort': 'str',


            'inclusions': 'list[str]',


            'periodicRefresh': 'bool',


            'protocol': 'str'

        }

        self.attributeMap = {

            'status': 'status',

            'failureReason': 'failureReason',

            'createTime': 'createTime',

            'lastUpdateTime': 'lastUpdateTime',

            'id': 'id',

            'sourceIP': 'sourceIP',

            'destIP': 'destIP',

            'sourcePort': 'sourcePort',

            'destPort': 'destPort',

            'inclusions': 'inclusions',

            'periodicRefresh': 'periodicRefresh',

            'protocol': 'protocol'

        }


        #Aggregated status of flow-analysis request. Value from a set of [INPROGRESS, COMPLETED, FAILED]

        self.status = None # str


        self.failureReason = None # str

        #Flow analysis request creation time

        self.createTime = None # int

        #Flow analysis request last update time

        self.lastUpdateTime = None # int

        #

        self.id = None # str

        #Source IP address

        self.sourceIP = None # str

        #Destination IP address

        self.destIP = None # str

        #Source Port

        self.sourcePort = None # str

        #Destination Port

        self.destPort = None # str

        #Subset of {INTERFACE-STATS, QOS-STATS, DEVICE-STATS, PERFORMANCE-STATS}

        self.inclusions = None # list[str]

        #periodicRefresh of path for every 30 sec

        self.periodicRefresh = None # bool

        #Protocol

        self.protocol = None # str

