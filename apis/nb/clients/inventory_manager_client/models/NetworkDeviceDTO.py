#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class NetworkDeviceDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'location': 'str',
            
            
            'type': 'str',
            
            
            'serialNumber': 'str',
            
            
            'errorCode': 'str',
            
            
            'family': 'str',
            
            
            'role': 'str',
            
            
            'roleSource': 'str',
            
            
            'apManagerInterfaceIp': 'str',
            
            
            'bootDateTime': 'str',
            
            
            'collectionStatus': 'str',
            
            
            'interfaceCount': 'str',
            
            
            'lineCardCount': 'str',
            
            
            'lineCardId': 'str',
            
            
            'managementIpAddress': 'str',
            
            
            'memorySize': 'str',
            
            
            'platformId': 'str',
            
            
            'reachabilityFailureReason': 'str',
            
            
            'reachabilityStatus': 'str',
            
            
            'snmpContact': 'str',
            
            
            'snmpLocation': 'str',
            
            
            'tunnelUdpPort': 'str',
            
            
            'inventoryStatusDetail': 'str',
            
            
            'upTime': 'str',
            
            
            'series': 'str',
            
            
            'lastUpdateTime': 'date-time',
            
            
            'locationName': 'str',
            
            
            'tagCount': 'str',
            
            
            'hostname': 'str',
            
            
            'errorDescription': 'str',
            
            
            'lastUpdated': 'str',
            
            
            'macAddress': 'str',
            
            
            'softwareVersion': 'str',
            
            
            'instanceUuid': 'str',
            
            
            'id': 'str'
            
        }

        self.attributeMap = {
            
            'location': 'location',
            
            'type': 'type',
            
            'serialNumber': 'serialNumber',
            
            'errorCode': 'errorCode',
            
            'family': 'family',
            
            'role': 'role',
            
            'roleSource': 'roleSource',
            
            'apManagerInterfaceIp': 'apManagerInterfaceIp',
            
            'bootDateTime': 'bootDateTime',
            
            'collectionStatus': 'collectionStatus',
            
            'interfaceCount': 'interfaceCount',
            
            'lineCardCount': 'lineCardCount',
            
            'lineCardId': 'lineCardId',
            
            'managementIpAddress': 'managementIpAddress',
            
            'memorySize': 'memorySize',
            
            'platformId': 'platformId',
            
            'reachabilityFailureReason': 'reachabilityFailureReason',
            
            'reachabilityStatus': 'reachabilityStatus',
            
            'snmpContact': 'snmpContact',
            
            'snmpLocation': 'snmpLocation',
            
            'tunnelUdpPort': 'tunnelUdpPort',
            
            'inventoryStatusDetail': 'inventoryStatusDetail',
            
            'upTime': 'upTime',
            
            'series': 'series',
            
            'lastUpdateTime': 'lastUpdateTime',
            
            'locationName': 'locationName',
            
            'tagCount': 'tagCount',
            
            'hostname': 'hostname',
            
            'errorDescription': 'errorDescription',
            
            'lastUpdated': 'lastUpdated',
            
            'macAddress': 'macAddress',
            
            'softwareVersion': 'softwareVersion',
            
            'instanceUuid': 'instanceUuid',
            
            'id': 'id'
            
        }       

        
        #Location ID that is associated with the device
        
        self.location = None # str
        
        #Type of device as switch, router, wireless lan controller, accesspoints
        
        self.type = None # str
        
        #Serial number of device
        
        self.serialNumber = None # str
        
        #Inventory status error code
        
        self.errorCode = None # str
        
        #Family of device as switch, router, wireless lan controller, accesspoints
        
        self.family = None # str
        
        #Role of device as access, distribution, border router, core
        
        self.role = None # str
        
        #Role source as manual / auto
        
        self.roleSource = None # str
        
        #IP address of WLC on AP manager interface
        
        self.apManagerInterfaceIp = None # str
        
        #Device boot time
        
        self.bootDateTime = None # str
        
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
        
        #SNMP contact on device
        
        self.snmpContact = None # str
        
        #SNMP location on device
        
        self.snmpLocation = None # str
        
        #Mobility protocol port is stored as tunneludpport for WLC
        
        self.tunnelUdpPort = None # str
        
        #Status detail of inventory sync
        
        self.inventoryStatusDetail = None # str
        
        #Time that shows for how long the device has been up
        
        self.upTime = None # str
        
        #Device series
        
        self.series = None # str
        
        
        self.lastUpdateTime = None # date-time
        
        #Name of the associated location
        
        self.locationName = None # str
        
        #Number of tags associated with the device
        
        self.tagCount = None # str
        
        #Device name
        
        self.hostname = None # str
        
        #Inventory status description
        
        self.errorDescription = None # str
        
        #Time when the network device info last got updated
        
        self.lastUpdated = None # str
        
        #MAC address of device
        
        self.macAddress = None # str
        
        #Software version on the device
        
        self.softwareVersion = None # str
        
        
        self.instanceUuid = None # str
        
        
        self.id = None # str
        
