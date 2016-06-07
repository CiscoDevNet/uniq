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

class NetworkDeviceDTO(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'serialNumber': 'str',


            'family': 'str',


            'inventoryStatusDetail': 'str',


            'hostname': 'str',


            'macAddress': 'str',


            'locationName': 'str',


            'lastUpdated': 'str',


            'upTime': 'str',


            'lastUpdateTime': 'date-time',


            'role': 'str',


            'tagCount': 'str',


            'softwareVersion': 'str',


            'apManagerInterfaceIp': 'str',


            'bootDateTime': 'str',


            'series': 'str',


            'collectionStatus': 'str',


            'interfaceCount': 'str',


            'lineCardCount': 'str',


            'lineCardId': 'str',


            'managementIpAddress': 'str',


            'memorySize': 'str',


            'platformId': 'str',


            'reachabilityFailureReason': 'str',


            'reachabilityStatus': 'str',


            'roleSource': 'str',


            'snmpContact': 'str',


            'snmpLocation': 'str',


            'tunnelUdpPort': 'str',


            'location': 'str',


            'type': 'str',


            'id': 'str',


            'instanceUuid': 'str'

        }

        self.attributeMap = {

            'serialNumber': 'serialNumber',

            'family': 'family',

            'inventoryStatusDetail': 'inventoryStatusDetail',

            'hostname': 'hostname',

            'macAddress': 'macAddress',

            'locationName': 'locationName',

            'lastUpdated': 'lastUpdated',

            'upTime': 'upTime',

            'lastUpdateTime': 'lastUpdateTime',

            'role': 'role',

            'tagCount': 'tagCount',

            'softwareVersion': 'softwareVersion',

            'apManagerInterfaceIp': 'apManagerInterfaceIp',

            'bootDateTime': 'bootDateTime',

            'series': 'series',

            'collectionStatus': 'collectionStatus',

            'interfaceCount': 'interfaceCount',

            'lineCardCount': 'lineCardCount',

            'lineCardId': 'lineCardId',

            'managementIpAddress': 'managementIpAddress',

            'memorySize': 'memorySize',

            'platformId': 'platformId',

            'reachabilityFailureReason': 'reachabilityFailureReason',

            'reachabilityStatus': 'reachabilityStatus',

            'roleSource': 'roleSource',

            'snmpContact': 'snmpContact',

            'snmpLocation': 'snmpLocation',

            'tunnelUdpPort': 'tunnelUdpPort',

            'location': 'location',

            'type': 'type',

            'id': 'id',

            'instanceUuid': 'instanceUuid'

        }


        #Serial number of device

        self.serialNumber = None # str

        #Family of device as switch, router, wireless lan controller, accesspoints

        self.family = None # str

        #Status detail of inventory sync

        self.inventoryStatusDetail = None # str

        #Device name

        self.hostname = None # str

        #MAC address of device

        self.macAddress = None # str

        #Name of the associated location

        self.locationName = None # str

        #Time when the network device info last got updated

        self.lastUpdated = None # str

        #Time that shows for how long the device has been up

        self.upTime = None # str


        self.lastUpdateTime = None # date-time

        #Role of device as access, distribution, border router, core

        self.role = None # str

        #Number of tags associated with the device

        self.tagCount = None # str

        #Software version on the device

        self.softwareVersion = None # str

        #IP address of WLC on AP manager interface

        self.apManagerInterfaceIp = None # str

        #Device boot time

        self.bootDateTime = None # str

        #Device series

        self.series = None # str

        #Collection status as Synchronizing, Could not synchronize, Not manageable, Managed, Partial Collection Failure, Incomplete, Unreachable, Wrong credential, Reachable, In Progress

        self.collectionStatus = None # str

        #Number of interfaces on the device

        self.interfaceCount = None # str

        #Number of linecards on the device

        self.lineCardCount = None # str

        #IDs of linecards of the device

        self.lineCardId = None # str

        #IP address of the device

        self.managementIpAddress = None # str

        #Processor memory size

        self.memorySize = None # str

        #Platform ID of device

        self.platformId = None # str

        #Failure reason for unreachable devices

        self.reachabilityFailureReason = None # str

        #Device reachability status as Reachable / Unreachable

        self.reachabilityStatus = None # str

        #Role source as manual / auto

        self.roleSource = None # str

        #SNMP contact on device

        self.snmpContact = None # str

        #SNMP location on device

        self.snmpLocation = None # str

        #Mobility protocol port is stored as tunneludpport for WLC

        self.tunnelUdpPort = None # str

        #Location ID that is associated with the device

        self.location = None # str

        #Type of device as switch, router, wireless lan controller, accesspoints

        self.type = None # str


        self.id = None # str


        self.instanceUuid = None # str

