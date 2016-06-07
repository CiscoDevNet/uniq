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

class Interface(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'interfaceStatsCollectionFailureReason': 'str',


            'qosStatsCollectionFailureReason': 'str',


            'vrfName': 'str',


            'aclAnalysis': 'AclAnalysisResponse',


            'interfaceStatistics': 'InterfaceStatistics',


            'qosStatistics': 'list[QosClassMapStatistics]',


            'interfaceStatsCollection': 'str',


            'qosStatsCollection': 'str',


            'name': 'str',


            'id': 'str'

        }

        self.attributeMap = {

            'interfaceStatsCollectionFailureReason': 'interfaceStatsCollectionFailureReason',

            'qosStatsCollectionFailureReason': 'qosStatsCollectionFailureReason',

            'vrfName': 'vrfName',

            'aclAnalysis': 'aclAnalysis',

            'interfaceStatistics': 'interfaceStatistics',

            'qosStatistics': 'qosStatistics',

            'interfaceStatsCollection': 'interfaceStatsCollection',

            'qosStatsCollection': 'qosStatsCollection',

            'name': 'name',

            'id': 'id'

        }



        self.interfaceStatsCollectionFailureReason = None # str


        self.qosStatsCollectionFailureReason = None # str

        #Name of VRF that the interface on a device belongs to

        self.vrfName = None # str

        #Analysis of ACLs on an interface of a device

        self.aclAnalysis = None # AclAnalysisResponse


        self.interfaceStatistics = None # InterfaceStatistics


        self.qosStatistics = None # list[QosClassMapStatistics]

        #A status value from [ INPROGRESS, SUCCESS, FAILED ]

        self.interfaceStatsCollection = None # str

        #A status value from [ INPROGRESS, SUCCESS, FAILED ]

        self.qosStatsCollection = None # str

        #Name of interface on a device

        self.name = None # str

        #ID of interface on a device

        self.id = None # str

