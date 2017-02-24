#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ZtdSiteDevice(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'authStatus': 'DeviceAuthState',
            
            
            'deviceId': 'str',
            
            
            'lastStateTransitionTime': 'str',
            
            
            'lastContact': 'str',
            
            
            'stateDisplay': 'str',
            
            
            'state': 'str',
            
            
            'serialNumber': 'str',
            
            
            'source': 'str',
            
            
            'tag': 'str',
            
            
            'aliases': 'list[str]',
            
            
            'id': 'str',
            
            
            'platformId': 'str',
            
            
            'site': 'str',
            
            
            'imageId': 'str',
            
            
            'configId': 'str',
            
            
            'pkiEnabled': 'bool',
            
            
            'memberCount': 'int',
            
            
            'eulaAccepted': 'bool',
            
            
            'licenseLevel': 'str',
            
            
            'templateConfigId': 'str',
            
            
            'bootStrapId': 'str',
            
            
            'licenseString': 'str',
            
            
            'apCount': 'str',
            
            
            'isMobilityController': 'str',
            
            
            'deviceDiscoveryInfo': 'ZtdDeviceDiscoveryInfo',
            
            
            'sudiRequired': 'bool',
            
            
            'memberDetail': 'list[ZtdMemberDetail]',
            
            
            'connectedToDeviceId': 'str',
            
            
            'connectedToPortId': 'str',
            
            
            'connectedToDeviceHostName': 'str',
            
            
            'connectedToPortName': 'str',
            
            
            'configPreference': 'str',
            
            
            'imagePreference': 'str',
            
            
            'connetedToLocationGeoAddr': 'str',
            
            
            'connetedToLocationCivicAddr': 'str',
            
            
            'hostName': 'str'
            
        }

        self.attributeMap = {
            
            'authStatus': 'authStatus',
            
            'deviceId': 'deviceId',
            
            'lastStateTransitionTime': 'lastStateTransitionTime',
            
            'lastContact': 'lastContact',
            
            'stateDisplay': 'stateDisplay',
            
            'state': 'state',
            
            'serialNumber': 'serialNumber',
            
            'source': 'source',
            
            'tag': 'tag',
            
            'aliases': 'aliases',
            
            'id': 'id',
            
            'platformId': 'platformId',
            
            'site': 'site',
            
            'imageId': 'imageId',
            
            'configId': 'configId',
            
            'pkiEnabled': 'pkiEnabled',
            
            'memberCount': 'memberCount',
            
            'eulaAccepted': 'eulaAccepted',
            
            'licenseLevel': 'licenseLevel',
            
            'templateConfigId': 'templateConfigId',
            
            'bootStrapId': 'bootStrapId',
            
            'licenseString': 'licenseString',
            
            'apCount': 'apCount',
            
            'isMobilityController': 'isMobilityController',
            
            'deviceDiscoveryInfo': 'deviceDiscoveryInfo',
            
            'sudiRequired': 'sudiRequired',
            
            'memberDetail': 'memberDetail',
            
            'connectedToDeviceId': 'connectedToDeviceId',
            
            'connectedToPortId': 'connectedToPortId',
            
            'connectedToDeviceHostName': 'connectedToDeviceHostName',
            
            'connectedToPortName': 'connectedToPortName',
            
            'configPreference': 'configPreference',
            
            'imagePreference': 'imagePreference',
            
            'connetedToLocationGeoAddr': 'connetedToLocationGeoAddr',
            
            'connetedToLocationCivicAddr': 'connetedToLocationCivicAddr',
            
            'hostName': 'hostName'
            
        }       

        
        
        self.authStatus = None # DeviceAuthState
        
        
        self.deviceId = None # str
        
        
        self.lastStateTransitionTime = None # str
        
        
        self.lastContact = None # str
        
        
        self.stateDisplay = None # str
        
        
        self.state = None # str
        
        #Serial number
        
        self.serialNumber = None # str
        
        #Source of rule,set to CLOUD if rule matches synced cloud device
        
        self.source = None # str
        
        #Tag of device
        
        self.tag = None # str
        
        
        self.aliases = None # list[str]
        
        #ID of device
        
        self.id = None # str
        
        #Platform ID
        
        self.platformId = None # str
        
        #Site to which device belongs if auto-provisioned
        
        self.site = None # str
        
        #Image file ID
        
        self.imageId = None # str
        
        #Configuration file id
        
        self.configId = None # str
        
        #Configure PKCS#12 trust point during PNP workflow if true
        
        self.pkiEnabled = None # bool
        
        #Count of members in a stack switch excluding master
        
        self.memberCount = None # int
        
        #CLI execution EULA accepted or not
        
        self.eulaAccepted = None # bool
        
        #CLI execution license level
        
        self.licenseLevel = None # str
        
        #Template config ID
        
        self.templateConfigId = None # str
        
        #Bootstrap file id
        
        self.bootStrapId = None # str
        
        #License string
        
        self.licenseString = None # str
        
        #Wireless AP count
        
        self.apCount = None # str
        
        #Specify if device is a wireless mobility controller
        
        self.isMobilityController = None # str
        
        #Device discovery info
        
        self.deviceDiscoveryInfo = None # ZtdDeviceDiscoveryInfo
        
        
        self.sudiRequired = None # bool
        
        
        self.memberDetail = None # list[ZtdMemberDetail]
        
        
        self.connectedToDeviceId = None # str
        
        
        self.connectedToPortId = None # str
        
        
        self.connectedToDeviceHostName = None # str
        
        
        self.connectedToPortName = None # str
        
        
        self.configPreference = None # str
        
        
        self.imagePreference = None # str
        
        
        self.connetedToLocationGeoAddr = None # str
        
        
        self.connetedToLocationCivicAddr = None # str
        
        #Host name
        
        self.hostName = None # str
        
