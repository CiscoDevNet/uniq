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

class NetworkElementInfo(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'role': 'str',


            'ip': 'str',


            'linkInformationSource': 'str',


            'tunnels': 'list[str]',


            'accuracyList': 'list[Accuracy]',


            'egressInterface': 'InterfaceContainer',


            'ingressInterface': 'InterfaceContainer',


            'deviceStatsCollectionFailureReason': 'str',


            'detailedStatus': 'DetailedStatus',


            'deviceStatistics': 'DeviceStatistics',


            'perfMonCollection': 'str',


            'perfMonCollectionFailureReason': 'str',


            'deviceStatsCollection': 'str',


            'perfMonitorStatistics': 'PerfMonitorStatistics',


            'name': 'str',


            'id': 'str',


            'type': 'str'

        }

        self.attributeMap = {

            'role': 'role',

            'ip': 'ip',

            'linkInformationSource': 'linkInformationSource',

            'tunnels': 'tunnels',

            'accuracyList': 'accuracyList',

            'egressInterface': 'egressInterface',

            'ingressInterface': 'ingressInterface',

            'deviceStatsCollectionFailureReason': 'deviceStatsCollectionFailureReason',

            'detailedStatus': 'detailedStatus',

            'deviceStatistics': 'deviceStatistics',

            'perfMonCollection': 'perfMonCollection',

            'perfMonCollectionFailureReason': 'perfMonCollectionFailureReason',

            'deviceStatsCollection': 'deviceStatsCollection',

            'perfMonitorStatistics': 'perfMonitorStatistics',

            'name': 'name',

            'id': 'id',

            'type': 'type'

        }


        #Role of device in network(can be access,core,distribution or border router)

        self.role = None # str

        #Network Device IP

        self.ip = None # str

        #The source of the link information to the next hop

        self.linkInformationSource = None # str

        #Tunnels this network element is in

        self.tunnels = None # list[str]


        self.accuracyList = None # list[Accuracy]

        #Egress interface of the network device

        self.egressInterface = None # InterfaceContainer

        #Ingress interface of the network device

        self.ingressInterface = None # InterfaceContainer


        self.deviceStatsCollectionFailureReason = None # str


        self.detailedStatus = None # DetailedStatus

        #Device statistics

        self.deviceStatistics = None # DeviceStatistics

        #A status value from [ INPROGRESS, SUCCESS, FAILED ]

        self.perfMonCollection = None # str


        self.perfMonCollectionFailureReason = None # str

        #A status value from [ INPROGRESS, SUCCESS, FAILED ]

        self.deviceStatsCollection = None # str

        #perf mon statistics on the device for give flow

        self.perfMonitorStatistics = None # PerfMonitorStatistics

        #Network Device name

        self.name = None # str

        #Network Device ID

        self.id = None # str

        #Network Device Type(can be switch,router,wired host or wireless host)

        self.type = None # str

