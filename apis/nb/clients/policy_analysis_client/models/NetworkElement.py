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

class NetworkElement(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'role': 'str',


            'ip': 'str',


            'ingressVirtualInterface': 'Interface',


            'egressVirtualInterface': 'Interface',


            'ingressPhysicalInterface': 'Interface',


            'egressPhysicalInterface': 'Interface',


            'linkInformationSource': 'str',


            'tunnels': 'list[str]',


            'accuracyList': 'list[Accuracy]',


            'deviceStatsCollectionFailureReason': 'str',


            'detailedStatus': 'DetailedStatus',


            'deviceStatistics': 'DeviceStatistics',


            'perfMonStatistics': 'PerfMonitorStatistics',


            'perfMonCollection': 'str',


            'perfMonCollectionFailureReason': 'str',


            'deviceStatsCollection': 'str',


            'name': 'str',


            'id': 'str',


            'type': 'str'

        }

        self.attributeMap = {

            'role': 'role',

            'ip': 'ip',

            'ingressVirtualInterface': 'ingressVirtualInterface',

            'egressVirtualInterface': 'egressVirtualInterface',

            'ingressPhysicalInterface': 'ingressPhysicalInterface',

            'egressPhysicalInterface': 'egressPhysicalInterface',

            'linkInformationSource': 'linkInformationSource',

            'tunnels': 'tunnels',

            'accuracyList': 'accuracyList',

            'deviceStatsCollectionFailureReason': 'deviceStatsCollectionFailureReason',

            'detailedStatus': 'detailedStatus',

            'deviceStatistics': 'deviceStatistics',

            'perfMonStatistics': 'perfMonStatistics',

            'perfMonCollection': 'perfMonCollection',

            'perfMonCollectionFailureReason': 'perfMonCollectionFailureReason',

            'deviceStatsCollection': 'deviceStatsCollection',

            'name': 'name',

            'id': 'id',

            'type': 'type'

        }


        #Role of device in network(can be access,core,distribution or border router)

        self.role = None # str

        #Network Device IP

        self.ip = None # str

        #Ingress virtual interface of the network device

        self.ingressVirtualInterface = None # Interface

        #Egress virtual interface of the network device

        self.egressVirtualInterface = None # Interface

        #Igress physical interface of the network device

        self.ingressPhysicalInterface = None # Interface

        #Egress physical interface of the network device

        self.egressPhysicalInterface = None # Interface

        #The source of the link information to the next hop

        self.linkInformationSource = None # str

        #Tunnels this network element is in

        self.tunnels = None # list[str]


        self.accuracyList = None # list[Accuracy]


        self.deviceStatsCollectionFailureReason = None # str


        self.detailedStatus = None # DetailedStatus


        self.deviceStatistics = None # DeviceStatistics


        self.perfMonStatistics = None # PerfMonitorStatistics

        #A status value from [ INPROGRESS, SUCCESS, FAILED ]

        self.perfMonCollection = None # str


        self.perfMonCollectionFailureReason = None # str

        #A status value from [ INPROGRESS, SUCCESS, FAILED ]

        self.deviceStatsCollection = None # str

        #Network Device name

        self.name = None # str

        #Network Device ID

        self.id = None # str

        #Network Device Type(can be switch,router,wired host or wireless host)

        self.type = None # str

