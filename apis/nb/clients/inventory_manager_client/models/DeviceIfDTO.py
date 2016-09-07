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
            
            'description': 'str',
            
            
            'className': 'str',
            
            
            'deviceId': 'str',
            
            
            'status': 'str',
            
            
            'interfaceType': 'str',
            
            
            'duplex': 'str',
            
            
            'portMode': 'str',
            
            
            'portType': 'str',
            
            
            'lastUpdated': 'str',
            
            
            'vlanId': 'str',
            
            
            'portName': 'str',
            
            
            'series': 'str',
            
            
            'ipv4Address': 'str',
            
            
            'ipv4Mask': 'str',
            
            
            'isisSupport': 'str',
            
            
            'mappedPhysicalInterfaceId': 'str',
            
            
            'mappedPhysicalInterfaceName': 'str',
            
            
            'nativeVlanId': 'str',
            
            
            'ospfSupport': 'str',
            
            
            'pid': 'str',
            
            
            'serialNo': 'str',
            
            
            'ifIndex': 'str',
            
            
            'macAddress': 'str',
            
            
            'speed': 'str',
            
            
            'id': 'str',
            
            
            'instanceUuid': 'str'
            
        }

        self.attributeMap = {
            
            'description': 'description',
            
            'className': 'className',
            
            'deviceId': 'deviceId',
            
            'status': 'status',
            
            'interfaceType': 'interfaceType',
            
            'duplex': 'duplex',
            
            'portMode': 'portMode',
            
            'portType': 'portType',
            
            'lastUpdated': 'lastUpdated',
            
            'vlanId': 'vlanId',
            
            'portName': 'portName',
            
            'series': 'series',
            
            'ipv4Address': 'ipv4Address',
            
            'ipv4Mask': 'ipv4Mask',
            
            'isisSupport': 'isisSupport',
            
            'mappedPhysicalInterfaceId': 'mappedPhysicalInterfaceId',
            
            'mappedPhysicalInterfaceName': 'mappedPhysicalInterfaceName',
            
            'nativeVlanId': 'nativeVlanId',
            
            'ospfSupport': 'ospfSupport',
            
            'pid': 'pid',
            
            'serialNo': 'serialNo',
            
            'ifIndex': 'ifIndex',
            
            'macAddress': 'macAddress',
            
            'speed': 'speed',
            
            'id': 'id',
            
            'instanceUuid': 'instanceUuid'
            
        }       

        
        #interface description
        
        self.description = None # str
        
        
        self.className = None # str
        
        #ID of the device
        
        self.deviceId = None # str
        
        #Interface status as Down / Up
        
        self.status = None # str
        
        #Interface type as Physical or Virtual
        
        self.interfaceType = None # str
        
        #Interface duplex as AutoNegotiate or FullDuplex
        
        self.duplex = None # str
        
        #Port mode as access, trunk, routed
        
        self.portMode = None # str
        
        #Port type as Ethernet Port / Ethernet SVI / Ethernet Sub Interface
        
        self.portType = None # str
        
        #Time when the device interface info last got updated
        
        self.lastUpdated = None # str
        
        #Vlan ID of interface
        
        self.vlanId = None # str
        
        #Interface name
        
        self.portName = None # str
        
        #Series of the device
        
        self.series = None # str
        
        #IPv4 address assigned for interface
        
        self.ipv4Address = None # str
        
        #Subnet mask for IPv4 address assigned for interface
        
        self.ipv4Mask = None # str
        
        #Flag for ISIS enabled / disabled
        
        self.isisSupport = None # str
        
        #ID of physical interface mapped with the virtual interface of WLC
        
        self.mappedPhysicalInterfaceId = None # str
        
        #Physical interface name mapped with the virtual interface of WLC
        
        self.mappedPhysicalInterfaceName = None # str
        
        #Vlan to receive untagged frames on trunk port
        
        self.nativeVlanId = None # str
        
        #Flag for OSPF enabled / disabled
        
        self.ospfSupport = None # str
        
        #Platform ID of the device
        
        self.pid = None # str
        
        #Serial number of the device
        
        self.serialNo = None # str
        
        #Interface index
        
        self.ifIndex = None # str
        
        #MAC address of interface
        
        self.macAddress = None # str
        
        #Speed of the interface
        
        self.speed = None # str
        
        
        self.id = None # str
        
        
        self.instanceUuid = None # str
