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
            
            
            'lastContact': 'str',
            
            
            'deviceId': 'str',
            
            
            'lastStateTransitionTime': 'str',
            
            
            'stateDisplay': 'str',
            
            
            'state': 'str',
            
            
            'serialNumber': 'str',
            
            
            'tag': 'str',
            
            
            'aliases': 'list[str]',
            
            
            'id': 'str',
            
            
            'platformId': 'str',
            
            
            'site': 'str',
            
            
            'imageId': 'str',
            
            
            'eulaAccepted': 'bool',
            
            
            'memberCount': 'int',
            
            
            'templateConfigId': 'str',
            
            
            'licenseLevel': 'str',
            
            
            'bootStrapId': 'str',
            
            
            'licenseString': 'str',
            
            
            'apCount': 'str',
            
            
            'isMobilityController': 'str',
            
            
            'sudiRequired': 'bool',
            
            
            'deviceDiscoveryInfo': 'ZtdDeviceDiscoveryInfo',
            
            
            'configId': 'str',
            
            
            'pkiEnabled': 'bool',
            
            
            'memberDetail': 'list[ZtdMemberDetail]',
            
            
            'connectedToDeviceId': 'str',
            
            
            'connectedToPortId': 'str',
            
            
            'imagePreference': 'str',
            
            
            'connectedToDeviceHostName': 'str',
            
            
            'connectedToPortName': 'str',
            
            
            'connetedToLocationCivicAddr': 'str',
            
            
            'connetedToLocationGeoAddr': 'str',
            
            
            'configPreference': 'str',
            
            
            'hostName': 'str'
            
        }

        self.attributeMap = {
            
            'authStatus': 'authStatus',
            
            'lastContact': 'lastContact',
            
            'deviceId': 'deviceId',
            
            'lastStateTransitionTime': 'lastStateTransitionTime',
            
            'stateDisplay': 'stateDisplay',
            
            'state': 'state',
            
            'serialNumber': 'serialNumber',
            
            'tag': 'tag',
            
            'aliases': 'aliases',
            
            'id': 'id',
            
            'platformId': 'platformId',
            
            'site': 'site',
            
            'imageId': 'imageId',
            
            'eulaAccepted': 'eulaAccepted',
            
            'memberCount': 'memberCount',
            
            'templateConfigId': 'templateConfigId',
            
            'licenseLevel': 'licenseLevel',
            
            'bootStrapId': 'bootStrapId',
            
            'licenseString': 'licenseString',
            
            'apCount': 'apCount',
            
            'isMobilityController': 'isMobilityController',
            
            'sudiRequired': 'sudiRequired',
            
            'deviceDiscoveryInfo': 'deviceDiscoveryInfo',
            
            'configId': 'configId',
            
            'pkiEnabled': 'pkiEnabled',
            
            'memberDetail': 'memberDetail',
            
            'connectedToDeviceId': 'connectedToDeviceId',
            
            'connectedToPortId': 'connectedToPortId',
            
            'imagePreference': 'imagePreference',
            
            'connectedToDeviceHostName': 'connectedToDeviceHostName',
            
            'connectedToPortName': 'connectedToPortName',
            
            'connetedToLocationCivicAddr': 'connetedToLocationCivicAddr',
            
            'connetedToLocationGeoAddr': 'connetedToLocationGeoAddr',
            
            'configPreference': 'configPreference',
            
            'hostName': 'hostName'
            
        }       

        
        
        self.authStatus = None # DeviceAuthState
        
        
        self.lastContact = None # str
        
        
        self.deviceId = None # str
        
        
        self.lastStateTransitionTime = None # str
        
        
        self.stateDisplay = None # str
        
        
        self.state = None # str
        
        #Serial number
        
        self.serialNumber = None # str
        
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
        
        #CLI execution EULA accepted or not
        
        self.eulaAccepted = None # bool
        
        #Count of members in a stack switch excluding master
        
        self.memberCount = None # int
        
        #Template config ID
        
        self.templateConfigId = None # str
        
        #CLI execution license level
        
        self.licenseLevel = None # str
        
        #Bootstrap file id
        
        self.bootStrapId = None # str
        
        #License string
        
        self.licenseString = None # str
        
        #Wireless AP count
        
        self.apCount = None # str
        
        #Specify if device is a wireless mobility controller
        
        self.isMobilityController = None # str
        
        
        self.sudiRequired = None # bool
        
        #Device discovery info
        
        self.deviceDiscoveryInfo = None # ZtdDeviceDiscoveryInfo
        
        #Configuration file id
        
        self.configId = None # str
        
        #Configure PKCS#12 trust point during PNP workflow if true
        
        self.pkiEnabled = None # bool
        
        
        self.memberDetail = None # list[ZtdMemberDetail]
        
        
        self.connectedToDeviceId = None # str
        
        
        self.connectedToPortId = None # str
        
        
        self.imagePreference = None # str
        
        
        self.connectedToDeviceHostName = None # str
        
        
        self.connectedToPortName = None # str
        
        
        self.connetedToLocationCivicAddr = None # str
        
        
        self.connetedToLocationGeoAddr = None # str
        
        
        self.configPreference = None # str
        
        #Host name
        
        self.hostName = None # str
        
