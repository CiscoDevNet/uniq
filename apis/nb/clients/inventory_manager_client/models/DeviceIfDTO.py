#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class DeviceIfDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'className': 'str',
            
            
            'description': 'str',
            
            
            'interfaceType': 'str',
            
            
            'status': 'str',
            
            
            'voiceVlan': 'str',
            
            
            'ipv4Address': 'str',
            
            
            'ipv4Mask': 'str',
            
            
            'isisSupport': 'str',
            
            
            'mappedPhysicalInterfaceId': 'str',
            
            
            'mappedPhysicalInterfaceName': 'str',
            
            
            'mediaType': 'str',
            
            
            'nativeVlanId': 'str',
            
            
            'ospfSupport': 'str',
            
            
            'serialNo': 'str',
            
            
            'pid': 'str',
            
            
            'series': 'str',
            
            
            'vlanId': 'str',
            
            
            'deviceId': 'str',
            
            
            'duplex': 'str',
            
            
            'portMode': 'str',
            
            
            'portType': 'str',
            
            
            'lastUpdated': 'str',
            
            
            'macAddress': 'str',
            
            
            'ifIndex': 'str',
            
            
            'speed': 'str',
            
            
            'adminStatus': 'str',
            
            
            'portName': 'str',
            
            
            'instanceUuid': 'str',
            
            
            'id': 'str'
            
        }

        self.attributeMap = {
            
            'className': 'className',
            
            'description': 'description',
            
            'interfaceType': 'interfaceType',
            
            'status': 'status',
            
            'voiceVlan': 'voiceVlan',
            
            'ipv4Address': 'ipv4Address',
            
            'ipv4Mask': 'ipv4Mask',
            
            'isisSupport': 'isisSupport',
            
            'mappedPhysicalInterfaceId': 'mappedPhysicalInterfaceId',
            
            'mappedPhysicalInterfaceName': 'mappedPhysicalInterfaceName',
            
            'mediaType': 'mediaType',
            
            'nativeVlanId': 'nativeVlanId',
            
            'ospfSupport': 'ospfSupport',
            
            'serialNo': 'serialNo',
            
            'pid': 'pid',
            
            'series': 'series',
            
            'vlanId': 'vlanId',
            
            'deviceId': 'deviceId',
            
            'duplex': 'duplex',
            
            'portMode': 'portMode',
            
            'portType': 'portType',
            
            'lastUpdated': 'lastUpdated',
            
            'macAddress': 'macAddress',
            
            'ifIndex': 'ifIndex',
            
            'speed': 'speed',
            
            'adminStatus': 'adminStatus',
            
            'portName': 'portName',
            
            'instanceUuid': 'instanceUuid',
            
            'id': 'id'
            
        }       

        
        
        self.className = None # str
        
        #interface description
        
        self.description = None # str
        
        #Interface type as Physical or Virtual
        
        self.interfaceType = None # str
        
        #Interface status as Down / Up
        
        self.status = None # str
        
        #Vlan information of the interface
        
        self.voiceVlan = None # str
        
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
        
        #Media Type of the interface
        
        self.mediaType = None # str
        
        #Vlan to receive untagged frames on trunk port
        
        self.nativeVlanId = None # str
        
        #Flag for OSPF enabled / disabled
        
        self.ospfSupport = None # str
        
        #Serial number of the device
        
        self.serialNo = None # str
        
        #Platform ID of the device
        
        self.pid = None # str
        
        #Series of the device
        
        self.series = None # str
        
        #Vlan ID of interface
        
        self.vlanId = None # str
        
        #ID of the device
        
        self.deviceId = None # str
        
        #Interface duplex as AutoNegotiate or FullDuplex
        
        self.duplex = None # str
        
        #Port mode as access, trunk, routed
        
        self.portMode = None # str
        
        #Port type as Ethernet Port / Ethernet SVI / Ethernet Sub Interface
        
        self.portType = None # str
        
        #Time when the device interface info last got updated
        
        self.lastUpdated = None # str
        
        #MAC address of interface
        
        self.macAddress = None # str
        
        #Interface index
        
        self.ifIndex = None # str
        
        #Speed of the interface
        
        self.speed = None # str
        
        #Administrative status of the interface
        
        self.adminStatus = None # str
        
        #Interface name
        
        self.portName = None # str
        
        
        self.instanceUuid = None # str
        
        
        self.id = None # str
        
