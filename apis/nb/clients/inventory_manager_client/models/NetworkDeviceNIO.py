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

class NetworkDeviceNIO(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'ingressQueueConfig': 'str',


            'authModelId': 'str',


            'duplicateDeviceId': 'str',


            'anchorWlcForAp': 'str',


            'wlcApDeviceStatus': 'str',


            'vendor': 'str',


            'imageName': 'str',


            'type': 'str',


            'id': 'str',


            'location': 'str',


            'hostname': 'str',


            'tag': 'str',


            'serialNumber': 'str',


            'macAddress': 'str',


            'locationName': 'str',


            'lastUpdated': 'str',


            'upTime': 'str',


            'role': 'str',


            'tagCount': 'int',


            'portRange': 'str',


            'softwareVersion': 'str',


            'numUpdates': 'int',


            'avgUpdateFrequency': 'int',


            'bootDateTime': 'DateTime',


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


            'family': 'str',


            'qosStatus': 'str'

        }

        self.attributeMap = {

            'ingressQueueConfig': 'ingressQueueConfig',

            'authModelId': 'authModelId',

            'duplicateDeviceId': 'duplicateDeviceId',

            'anchorWlcForAp': 'anchorWlcForAp',

            'wlcApDeviceStatus': 'wlcApDeviceStatus',

            'vendor': 'vendor',

            'imageName': 'imageName',

            'type': 'type',

            'id': 'id',

            'location': 'location',

            'hostname': 'hostname',

            'tag': 'tag',

            'serialNumber': 'serialNumber',

            'macAddress': 'macAddress',

            'locationName': 'locationName',

            'lastUpdated': 'lastUpdated',

            'upTime': 'upTime',

            'role': 'role',

            'tagCount': 'tagCount',

            'portRange': 'portRange',

            'softwareVersion': 'softwareVersion',

            'numUpdates': 'numUpdates',

            'avgUpdateFrequency': 'avgUpdateFrequency',

            'bootDateTime': 'bootDateTime',

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

            'family': 'family',

            'qosStatus': 'qosStatus'

        }


        #Ingress queue config on device

        self.ingressQueueConfig = None # str

        #Authentication model Id on device

        self.authModelId = None # str

        #Identifier of the duplicate ip of the same device discovered

        self.duplicateDeviceId = None # str

        #Connected WLC device for AP

        self.anchorWlcForAp = None # str

        #Collection status of AP devices

        self.wlcApDeviceStatus = None # str

        #Vendor information of the device

        self.vendor = None # str

        #Image details on the device

        self.imageName = None # str

        #Type of device as switch, router, wireless lan controller, accesspoints

        self.type = None # str

        #Unique identifier of network device

        self.id = None # str

        #Location ID that is associated with the device

        self.location = None # str

        #Device name

        self.hostname = None # str

        #Tag ID that is associated with the device

        self.tag = None # str

        #Serial number of device

        self.serialNumber = None # str

        #MAC address of device

        self.macAddress = None # str

        #Name of the associated location

        self.locationName = None # str

        #Time when the network device info last got updated

        self.lastUpdated = None # str

        #Time that shows for how long the device has been up

        self.upTime = None # str

        #Role of device as access, distribution, border router, core

        self.role = None # str

        #Number of tags associated with the device

        self.tagCount = None # int

        #Range of ports on device

        self.portRange = None # str

        #Software version on the device

        self.softwareVersion = None # str

        #Number of time network-device info got updated

        self.numUpdates = None # int

        #Frequency in which interface info gets updated

        self.avgUpdateFrequency = None # int

        #Device boot time

        self.bootDateTime = None # DateTime

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

        #Family of device as switch, router, wireless lan controller, accesspoints

        self.family = None # str

        #Qos status on device

        self.qosStatus = None # str

