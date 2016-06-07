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

class LinkWrapper(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'source': 'str',


            'id': 'str',


            'endPortID': 'str',


            'startPortID': 'str',


            'greyOut': 'bool',


            'linkStatus': 'str',


            'startPortIpv4Address': 'str',


            'startPortIpv4Mask': 'str',


            'endPortIpv4Address': 'str',


            'endPortIpv4Mask': 'str',


            'endPortName': 'str',


            'endPortSpeed': 'str',


            'startPortName': 'str',


            'startPortSpeed': 'str',


            'tag': 'str',


            'target': 'str'

        }

        self.attributeMap = {

            'source': 'source',

            'id': 'id',

            'endPortID': 'endPortID',

            'startPortID': 'startPortID',

            'greyOut': 'greyOut',

            'linkStatus': 'linkStatus',

            'startPortIpv4Address': 'startPortIpv4Address',

            'startPortIpv4Mask': 'startPortIpv4Mask',

            'endPortIpv4Address': 'endPortIpv4Address',

            'endPortIpv4Mask': 'endPortIpv4Mask',

            'endPortName': 'endPortName',

            'endPortSpeed': 'endPortSpeed',

            'startPortName': 'startPortName',

            'startPortSpeed': 'startPortSpeed',

            'tag': 'tag',

            'target': 'target'

        }


        #Device ID correspondng to the source device

        self.source = None # str

        #Unified identifier for device

        self.id = None # str

        #Device port ID corresponding to end devices

        self.endPortID = None # str

        #Device port ID corresponding to start devices

        self.startPortID = None # str

        #Device greyout

        self.greyOut = None # bool

        #Indicates whether link is working

        self.linkStatus = None # str

        #Interface port IPv4 address corresponding to start devices

        self.startPortIpv4Address = None # str

        #Interface port IPv4 mask corresponding to start devices

        self.startPortIpv4Mask = None # str

        #Interface port IPv4 address corresponding to end devices

        self.endPortIpv4Address = None # str

        #Interface port IPv4 mask corresponding to end devices

        self.endPortIpv4Mask = None # str

        #Interface port name corresponding to end devices

        self.endPortName = None # str

        #Interface port speed corresponding to end devices

        self.endPortSpeed = None # str

        #Interface port name corresponding to start devices

        self.startPortName = None # str

        #Interface port speed corresponding to start devices

        self.startPortSpeed = None # str

        #Tag for the devices

        self.tag = None # str

        #Device ID corresponding to the target device

        self.target = None # str

