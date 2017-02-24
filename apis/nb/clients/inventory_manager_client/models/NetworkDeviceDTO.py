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
            
            'family': 'str',
            
            
            'location': 'str',
            
            
            'type': 'str',
            
            
            'serialNumber': 'str',
            
            
            'errorCode': 'str',
            
            
            'errorDescription': 'str',
            
            
            'lastUpdateTime': 'date-time',
            
            
            'series': 'str',
            
            
            'upTime': 'str',
            
            
            'inventoryStatusDetail': 'str',
            
            
            'role': 'str',
            
            
            'macAddress': 'str',
            
            
            'softwareVersion': 'str',
            
            
            'lastUpdated': 'str',
            
            
            'collectionInterval': 'str',
            
            
            'tagCount': 'str',
            
            
            'hostname': 'str',
            
            
            'locationName': 'str',
            
            
            'managementIpAddress': 'str',
            
            
            'memorySize': 'str',
            
            
            'platformId': 'str',
            
            
            'reachabilityFailureReason': 'str',
            
            
            'reachabilityStatus': 'str',
            
            
            'snmpContact': 'str',
            
            
            'snmpLocation': 'str',
            
            
            'tunnelUdpPort': 'str',
            
            
            'apManagerInterfaceIp': 'str',
            
            
            'bootDateTime': 'str',
            
            
            'collectionStatus': 'str',
            
            
            'interfaceCount': 'str',
            
            
            'lineCardCount': 'str',
            
            
            'lineCardId': 'str',
            
            
            'roleSource': 'str',
            
            
            'instanceUuid': 'str',
            
            
            'id': 'str'
            
        }

        self.attributeMap = {
            
            'family': 'family',
            
            'location': 'location',
            
            'type': 'type',
            
            'serialNumber': 'serialNumber',
            
            'errorCode': 'errorCode',
            
            'errorDescription': 'errorDescription',
            
            'lastUpdateTime': 'lastUpdateTime',
            
            'series': 'series',
            
            'upTime': 'upTime',
            
            'inventoryStatusDetail': 'inventoryStatusDetail',
            
            'role': 'role',
            
            'macAddress': 'macAddress',
            
            'softwareVersion': 'softwareVersion',
            
            'lastUpdated': 'lastUpdated',
            
            'collectionInterval': 'collectionInterval',
            
            'tagCount': 'tagCount',
            
            'hostname': 'hostname',
            
            'locationName': 'locationName',
            
            'managementIpAddress': 'managementIpAddress',
            
            'memorySize': 'memorySize',
            
            'platformId': 'platformId',
            
            'reachabilityFailureReason': 'reachabilityFailureReason',
            
            'reachabilityStatus': 'reachabilityStatus',
            
            'snmpContact': 'snmpContact',
            
            'snmpLocation': 'snmpLocation',
            
            'tunnelUdpPort': 'tunnelUdpPort',
            
            'apManagerInterfaceIp': 'apManagerInterfaceIp',
            
            'bootDateTime': 'bootDateTime',
            
            'collectionStatus': 'collectionStatus',
            
            'interfaceCount': 'interfaceCount',
            
            'lineCardCount': 'lineCardCount',
            
            'lineCardId': 'lineCardId',
            
            'roleSource': 'roleSource',
            
            'instanceUuid': 'instanceUuid',
            
            'id': 'id'
            
        }       

        
        #Family of device as switch, router, wireless lan controller, accesspoints
        
        self.family = None # str
        
        #Location ID that is associated with the device
        
        self.location = None # str
        
        #Type of device as switch, router, wireless lan controller, accesspoints
        
        self.type = None # str
        
        #Serial number of device
        
        self.serialNumber = None # str
        
        #Inventory status error code
        
        self.errorCode = None # str
        
        #Inventory status description
        
        self.errorDescription = None # str
        
        
        self.lastUpdateTime = None # date-time
        
        #Device series
        
        self.series = None # str
        
        #Time that shows for how long the device has been up
        
        self.upTime = None # str
        
        #Status detail of inventory sync
        
        self.inventoryStatusDetail = None # str
        
        #Role of device as access, distribution, border router, core
        
        self.role = None # str
        
        #MAC address of device
        
        self.macAddress = None # str
        
        #Software version on the device
        
        self.softwareVersion = None # str
        
        #Time when the network device info last got updated
        
        self.lastUpdated = None # str
        
        
        self.collectionInterval = None # str
        
        #Number of tags associated with the device
        
        self.tagCount = None # str
        
        #Device name
        
        self.hostname = None # str
        
        #Name of the associated location
        
        self.locationName = None # str
        
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
        
        #Role source as manual / auto
        
        self.roleSource = None # str
        
        
        self.instanceUuid = None # str
        
        
        self.id = None # str
        
