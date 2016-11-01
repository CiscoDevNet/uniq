#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


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
            
            
            'pingStatus': 'str',
            
            
            'snmpStatus': 'str',
            
            
            'cliStatus': 'str',
            
            
            'inventoryReachabilityStatus': 'str',
            
            
            'type': 'str',
            
            
            'location': 'str',
            
            
            'id': 'str',
            
            
            'role': 'str',
            
            
            'roleSource': 'str',
            
            
            'avgUpdateFrequency': 'int',
            
            
            'numUpdates': 'int',
            
            
            'bootDateTime': 'DateTime',
            
            
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
            
            
            'family': 'str',
            
            
            'qosStatus': 'str',
            
            
            'tag': 'str',
            
            
            'inventoryCollectionStatus': 'str',
            
            
            'upTime': 'str',
            
            
            'locationName': 'str',
            
            
            'tagCount': 'int',
            
            
            'hostname': 'str',
            
            
            'errorCode': 'str',
            
            
            'errorDescription': 'str',
            
            
            'imageName': 'str',
            
            
            'lastUpdated': 'str',
            
            
            'vendor': 'str',
            
            
            'macAddress': 'str',
            
            
            'softwareVersion': 'str',
            
            
            'serialNumber': 'str',
            
            
            'portRange': 'str'
            
        }

        self.attributeMap = {
            
            'ingressQueueConfig': 'ingressQueueConfig',
            
            'authModelId': 'authModelId',
            
            'duplicateDeviceId': 'duplicateDeviceId',
            
            'anchorWlcForAp': 'anchorWlcForAp',
            
            'wlcApDeviceStatus': 'wlcApDeviceStatus',
            
            'pingStatus': 'pingStatus',
            
            'snmpStatus': 'snmpStatus',
            
            'cliStatus': 'cliStatus',
            
            'inventoryReachabilityStatus': 'inventoryReachabilityStatus',
            
            'type': 'type',
            
            'location': 'location',
            
            'id': 'id',
            
            'role': 'role',
            
            'roleSource': 'roleSource',
            
            'avgUpdateFrequency': 'avgUpdateFrequency',
            
            'numUpdates': 'numUpdates',
            
            'bootDateTime': 'bootDateTime',
            
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
            
            'family': 'family',
            
            'qosStatus': 'qosStatus',
            
            'tag': 'tag',
            
            'inventoryCollectionStatus': 'inventoryCollectionStatus',
            
            'upTime': 'upTime',
            
            'locationName': 'locationName',
            
            'tagCount': 'tagCount',
            
            'hostname': 'hostname',
            
            'errorCode': 'errorCode',
            
            'errorDescription': 'errorDescription',
            
            'imageName': 'imageName',
            
            'lastUpdated': 'lastUpdated',
            
            'vendor': 'vendor',
            
            'macAddress': 'macAddress',
            
            'softwareVersion': 'softwareVersion',
            
            'serialNumber': 'serialNumber',
            
            'portRange': 'portRange'
            
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
        
        #Ping status at the time of discovery
        
        self.pingStatus = None # str
        
        #SNMP status at the time of discovery
        
        self.snmpStatus = None # str
        
        #CLI status at the time of discovery
        
        self.cliStatus = None # str
        
        #Inventory reachablity status
        
        self.inventoryReachabilityStatus = None # str
        
        #Type of device as switch, router, wireless lan controller, accesspoints
        
        self.type = None # str
        
        #Location ID that is associated with the device
        
        self.location = None # str
        
        #Unique identifier of network device
        
        self.id = None # str
        
        #Role of device as access, distribution, border router, core
        
        self.role = None # str
        
        #Role source as manual / auto
        
        self.roleSource = None # str
        
        #Frequency in which interface info gets updated
        
        self.avgUpdateFrequency = None # int
        
        #Number of time network-device info got updated
        
        self.numUpdates = None # int
        
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
        
        #SNMP contact on device
        
        self.snmpContact = None # str
        
        #SNMP location on device
        
        self.snmpLocation = None # str
        
        #Family of device as switch, router, wireless lan controller, accesspoints
        
        self.family = None # str
        
        #Qos status on device
        
        self.qosStatus = None # str
        
        #Tag ID that is associated with the device
        
        self.tag = None # str
        
        #Inventory status
        
        self.inventoryCollectionStatus = None # str
        
        #Time that shows for how long the device has been up
        
        self.upTime = None # str
        
        #Name of the associated location
        
        self.locationName = None # str
        
        #Number of tags associated with the device
        
        self.tagCount = None # int
        
        #Device name
        
        self.hostname = None # str
        
        #Inventory status error code
        
        self.errorCode = None # str
        
        #Inventory status description
        
        self.errorDescription = None # str
        
        #Image details on the device
        
        self.imageName = None # str
        
        #Time when the network device info last got updated
        
        self.lastUpdated = None # str
        
        #Vendor information of the device
        
        self.vendor = None # str
        
        #MAC address of device
        
        self.macAddress = None # str
        
        #Software version on the device
        
        self.softwareVersion = None # str
        
        #Serial number of device
        
        self.serialNumber = None # str
        
        #Range of ports on device
        
        self.portRange = None # str
        
