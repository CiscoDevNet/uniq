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

class HostDTO(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'hostName': 'str',


            'source': 'str',


            'vlanId': 'str',


            'lastUpdated': 'str',


            'avgUpdateFrequency': 'str',


            'connectedAPMacAddress': 'str',


            'connectedAPName': 'str',


            'connectedInterfaceId': 'str',


            'connectedInterfaceName': 'str',


            'connectedNetworkDeviceId': 'str',


            'connectedNetworkDeviceIpAddress': 'str',


            'hostIp': 'str',


            'hostMac': 'str',


            'hostType': 'str',


            'pointOfAttachment': 'str',


            'pointOfPresence': 'str',


            'attributeInfo': 'object',

            'id': 'str'

        }

        self.attributeMap = {

            'hostName': 'hostName',

            'source': 'source',

            'vlanId': 'vlanId',

            'lastUpdated': 'lastUpdated',

            'avgUpdateFrequency': 'avgUpdateFrequency',

            'connectedAPMacAddress': 'connectedAPMacAddress',

            'connectedAPName': 'connectedAPName',

            'connectedInterfaceId': 'connectedInterfaceId',

            'connectedInterfaceName': 'connectedInterfaceName',

            'connectedNetworkDeviceId': 'connectedNetworkDeviceId',

            'connectedNetworkDeviceIpAddress': 'connectedNetworkDeviceIpAddress',

            'hostIp': 'hostIp',

            'hostMac': 'hostMac',

            'hostType': 'hostType',

            'pointOfAttachment': 'pointOfAttachment',

            'pointOfPresence': 'pointOfPresence',

            'attributeInfo': 'attributeInfo',

            'id': 'id'

        }


        #Name of the host

        self.hostName = None # str

        #Source from which the host gets collected. Available option:200 for inventory collection and 300 for trap based data collection

        self.source = None # str

        #Vlan Id of the host

        self.vlanId = None # str

        #Time when the host info last got updated

        self.lastUpdated = None # str

        #Frequency in which host info gets updated

        self.avgUpdateFrequency = None # str

        #Mac address of the AP to which wireless host gets connected

        self.connectedAPMacAddress = None # str

        #Name of the AP to which wireless host gets connected

        self.connectedAPName = None # str

        #Id of the interface to which host gets connected

        self.connectedInterfaceId = None # str

        #Name of the interface to which host gets connected

        self.connectedInterfaceName = None # str

        #Id of the network device to which host gets connected

        self.connectedNetworkDeviceId = None # str

        #Ip address of the network device to which host gets connected

        self.connectedNetworkDeviceIpAddress = None # str

        #Ip address of the host

        self.hostIp = None # str

        #Mac address of the host

        self.hostMac = None # str

        #Type of the host. Available options are: Wired, Wireless

        self.hostType = None # str

        #Id of the Host&#39;s Point of attachment network device (wlc). Based on mobility

        self.pointOfAttachment = None # str

        #Id of the Host&#39;s Point of presence network device (wlc). Based on mobility

        self.pointOfPresence = None # str


        self.attributeInfo = None # object


        self.id = None # str

