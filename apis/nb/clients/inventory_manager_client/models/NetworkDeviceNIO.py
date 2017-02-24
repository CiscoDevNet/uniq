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
            
            'pingStatus': 'str',
            
            
            'snmpStatus': 'str',
            
            
            'cliStatus': 'str',
            
            
            'ingressQueueConfig': 'str',
            
            
            'authModelId': 'str',
            
            
            'duplicateDeviceId': 'str',
            
            
            'anchorWlcForAp': 'str',
            
            
            'wlcApDeviceStatus': 'str',
            
            
            'inventoryReachabilityStatus': 'str',
            
            
            'errorDescription': 'str',
            
            
            'imageName': 'str',
            
            
            'avgUpdateFrequency': 'int',
            
            
            'numUpdates': 'int',
            
            
            'upTime': 'str',
            
            
            'serialNumber': 'str',
            
            
            'type': 'str',
            
            
            'location': 'str',
            
            
            'portRange': 'str',
            
            
            'macAddress': 'str',
            
            
            'vendor': 'str',
            
            
            'softwareVersion': 'str',
            
            
            'role': 'str',
            
            
            'lastUpdated': 'str',
            
            
            'inventoryCollectionStatus': 'str',
            
            
            'errorCode': 'str',
            
            
            'tagCount': 'int',
            
            
            'hostname': 'str',
            
            
            'locationName': 'str',
            
            
            'id': 'str',
            
            
            'tag': 'str',
            
            
            'qosStatus': 'str',
            
            
            'managementIpAddress': 'str',
            
            
            'memorySize': 'str',
            
            
            'platformId': 'str',
            
            
            'reachabilityFailureReason': 'str',
            
            
            'reachabilityStatus': 'str',
            
            
            'snmpContact': 'str',
            
            
            'snmpLocation': 'str',
            
            
            'bootDateTime': 'DateTime',
            
            
            'family': 'str',
            
            
            'interfaceCount': 'str',
            
            
            'lineCardCount': 'str',
            
            
            'lineCardId': 'str',
            
            
            'roleSource': 'str'
            
        }

        self.attributeMap = {
            
            'pingStatus': 'pingStatus',
            
            'snmpStatus': 'snmpStatus',
            
            'cliStatus': 'cliStatus',
            
            'ingressQueueConfig': 'ingressQueueConfig',
            
            'authModelId': 'authModelId',
            
            'duplicateDeviceId': 'duplicateDeviceId',
            
            'anchorWlcForAp': 'anchorWlcForAp',
            
            'wlcApDeviceStatus': 'wlcApDeviceStatus',
            
            'inventoryReachabilityStatus': 'inventoryReachabilityStatus',
            
            'errorDescription': 'errorDescription',
            
            'imageName': 'imageName',
            
            'avgUpdateFrequency': 'avgUpdateFrequency',
            
            'numUpdates': 'numUpdates',
            
            'upTime': 'upTime',
            
            'serialNumber': 'serialNumber',
            
            'type': 'type',
            
            'location': 'location',
            
            'portRange': 'portRange',
            
            'macAddress': 'macAddress',
            
            'vendor': 'vendor',
            
            'softwareVersion': 'softwareVersion',
            
            'role': 'role',
            
            'lastUpdated': 'lastUpdated',
            
            'inventoryCollectionStatus': 'inventoryCollectionStatus',
            
            'errorCode': 'errorCode',
            
            'tagCount': 'tagCount',
            
            'hostname': 'hostname',
            
            'locationName': 'locationName',
            
            'id': 'id',
            
            'tag': 'tag',
            
            'qosStatus': 'qosStatus',
            
            'managementIpAddress': 'managementIpAddress',
            
            'memorySize': 'memorySize',
            
            'platformId': 'platformId',
            
            'reachabilityFailureReason': 'reachabilityFailureReason',
            
            'reachabilityStatus': 'reachabilityStatus',
            
            'snmpContact': 'snmpContact',
            
            'snmpLocation': 'snmpLocation',
            
            'bootDateTime': 'bootDateTime',
            
            'family': 'family',
            
            'interfaceCount': 'interfaceCount',
            
            'lineCardCount': 'lineCardCount',
            
            'lineCardId': 'lineCardId',
            
            'roleSource': 'roleSource'
            
        }       

        
        #Ping status at the time of discovery
        
        self.pingStatus = None # str
        
        #SNMP status at the time of discovery
        
        self.snmpStatus = None # str
        
        #CLI status at the time of discovery
        
        self.cliStatus = None # str
        
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
        
        #Last known reachabilty status of the device
        
        self.inventoryReachabilityStatus = None # str
        
        #Error description when inventory collection fails
        
        self.errorDescription = None # str
        
        #Image details on the device
        
        self.imageName = None # str
        
        #Frequency in which interface info gets updated
        
        self.avgUpdateFrequency = None # int
        
        #Number of time network-device info got updated
        
        self.numUpdates = None # int
        
        #Time that shows for how long the device has been up
        
        self.upTime = None # str
        
        #Serial number of device
        
        self.serialNumber = None # str
        
        #Type of device as switch, router, wireless lan controller, accesspoints
        
        self.type = None # str
        
        #Location ID that is associated with the device
        
        self.location = None # str
        
        #Range of ports on device
        
        self.portRange = None # str
        
        #MAC address of device
        
        self.macAddress = None # str
        
        #Vendor information of the device
        
        self.vendor = None # str
        
        #Software version on the device
        
        self.softwareVersion = None # str
        
        #Role of device as access, distribution, border router, core
        
        self.role = None # str
        
        #Time when the network device info last got updated
        
        self.lastUpdated = None # str
        
        #Last known collection status of the device
        
        self.inventoryCollectionStatus = None # str
        
        #Error code when inventory collection fails
        
        self.errorCode = None # str
        
        #Number of tags associated with the device
        
        self.tagCount = None # int
        
        #Device name
        
        self.hostname = None # str
        
        #Name of the associated location
        
        self.locationName = None # str
        
        #Unique identifier of network device
        
        self.id = None # str
        
        #Tag ID that is associated with the device
        
        self.tag = None # str
        
        #Qos status on device
        
        self.qosStatus = None # str
        
        #IP address of the device
        
        self.managementIpAddress = None # str
        
        #Processor memory size
        
        self.memorySize = None # str
        
        #Platform ID of device
        
        self.platformId = None # str
        
        #Failure reason for unreachable devices
        
        self.reachabilityFailureReason = None # str
        
        #Reachability status of a device as Success/Failure/Discarded
        
        self.reachabilityStatus = None # str
        
        #SNMP contact on device
        
        self.snmpContact = None # str
        
        #SNMP location on device
        
        self.snmpLocation = None # str
        
        #Device boot time
        
        self.bootDateTime = None # DateTime
        
        #Family of device as switch, router, wireless lan controller, accesspoints
        
        self.family = None # str
        
        #Number of interfaces on the device
        
        self.interfaceCount = None # str
        
        #Number of linecards on the device
        
        self.lineCardCount = None # str
        
        #IDs of linecards of the device
        
        self.lineCardId = None # str
        
        #Role source as manual / auto
        
        self.roleSource = None # str
        
