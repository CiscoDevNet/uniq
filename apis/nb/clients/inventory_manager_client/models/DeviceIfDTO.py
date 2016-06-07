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

class DeviceIfDTO(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'status': 'str',


            'interfaceType': 'str',


            'deviceId': 'str',


            'macAddress': 'str',


            'ifIndex': 'str',


            'speed': 'str',


            'duplex': 'str',


            'vlanId': 'str',


            'portName': 'str',


            'lastUpdated': 'str',


            'portMode': 'str',


            'portType': 'str',


            'numUpdates': 'str',


            'series': 'str',


            'avgUpdateFrequency': 'str',


            'lineCardId': 'str',


            'ipv4Mask': 'str',


            'ipv4Address': 'str',


            'isisSupport': 'str',


            'mappedPhysicalInterfaceId': 'str',


            'mappedPhysicalInterfaceName': 'str',


            'nativeVlanId': 'str',


            'ospfSupport': 'str',


            'pid': 'str',


            'serialNo': 'str',


            'instanceUuid': 'str'

        }

        self.attributeMap = {

            'status': 'status',

            'interfaceType': 'interfaceType',

            'deviceId': 'deviceId',

            'macAddress': 'macAddress',

            'ifIndex': 'ifIndex',

            'speed': 'speed',

            'duplex': 'duplex',

            'vlanId': 'vlanId',

            'portName': 'portName',

            'lastUpdated': 'lastUpdated',

            'portMode': 'portMode',

            'portType': 'portType',

            'numUpdates': 'numUpdates',

            'series': 'series',

            'avgUpdateFrequency': 'avgUpdateFrequency',

            'lineCardId': 'lineCardId',

            'ipv4Mask': 'ipv4Mask',

            'ipv4Address': 'ipv4Address',

            'isisSupport': 'isisSupport',

            'mappedPhysicalInterfaceId': 'mappedPhysicalInterfaceId',

            'mappedPhysicalInterfaceName': 'mappedPhysicalInterfaceName',

            'nativeVlanId': 'nativeVlanId',

            'ospfSupport': 'ospfSupport',

            'pid': 'pid',

            'serialNo': 'serialNo',

            'instanceUuid': 'instanceUuid'

        }



        self.status = None # str


        self.interfaceType = None # str


        self.deviceId = None # str


        self.macAddress = None # str


        self.ifIndex = None # str


        self.speed = None # str


        self.duplex = None # str


        self.vlanId = None # str


        self.portName = None # str


        self.lastUpdated = None # str


        self.portMode = None # str


        self.portType = None # str


        self.numUpdates = None # str


        self.series = None # str


        self.avgUpdateFrequency = None # str


        self.lineCardId = None # str


        self.ipv4Mask = None # str


        self.ipv4Address = None # str


        self.isisSupport = None # str


        self.mappedPhysicalInterfaceId = None # str


        self.mappedPhysicalInterfaceName = None # str


        self.nativeVlanId = None # str


        self.ospfSupport = None # str


        self.pid = None # str


        self.serialNo = None # str


        self.instanceUuid = None # str

