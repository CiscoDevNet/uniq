#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ZtdRule(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'serialNumber': 'str',
            
            
            'id': 'str',
            
            
            'site': 'str',
            
            
            'imageId': 'str',
            
            
            'platformId': 'str',
            
            
            'templateConfigId': 'str',
            
            
            'licenseString': 'str',
            
            
            'apCount': 'str',
            
            
            'isMobilityController': 'str',
            
            
            'pkiEnabled': 'bool',
            
            
            'configId': 'str',
            
            
            'hostName': 'str',
            
            
            'bootStrapId': 'str',
            
            
            'sudiRequired': 'bool',
            
            
            'deviceDiscoveryInfo': 'ZtdDeviceDiscoveryInfo',
            
            
            'licenseLevel': 'str',
            
            
            'memberCount': 'int',
            
            
            'eulaAccepted': 'bool',
            
            
            'memberDetail': 'list[ZtdMemberDetail]',
            
            
            'aliases': 'list[str]',
            
            
            'connectedToDeviceId': 'str',
            
            
            'connectedToPortId': 'str',
            
            
            'tag': 'str',
            
            
            'connetedToLocationGeoAddr': 'str',
            
            
            'configPreference': 'str',
            
            
            'imagePreference': 'str',
            
            
            'connectedToDeviceHostName': 'str',
            
            
            'connectedToPortName': 'str',
            
            
            'connetedToLocationCivicAddr': 'str'
            
        }

        self.attributeMap = {
            
            'serialNumber': 'serialNumber',
            
            'id': 'id',
            
            'site': 'site',
            
            'imageId': 'imageId',
            
            'platformId': 'platformId',
            
            'templateConfigId': 'templateConfigId',
            
            'licenseString': 'licenseString',
            
            'apCount': 'apCount',
            
            'isMobilityController': 'isMobilityController',
            
            'pkiEnabled': 'pkiEnabled',
            
            'configId': 'configId',
            
            'hostName': 'hostName',
            
            'bootStrapId': 'bootStrapId',
            
            'sudiRequired': 'sudiRequired',
            
            'deviceDiscoveryInfo': 'deviceDiscoveryInfo',
            
            'licenseLevel': 'licenseLevel',
            
            'memberCount': 'memberCount',
            
            'eulaAccepted': 'eulaAccepted',
            
            'memberDetail': 'memberDetail',
            
            'aliases': 'aliases',
            
            'connectedToDeviceId': 'connectedToDeviceId',
            
            'connectedToPortId': 'connectedToPortId',
            
            'tag': 'tag',
            
            'connetedToLocationGeoAddr': 'connetedToLocationGeoAddr',
            
            'configPreference': 'configPreference',
            
            'imagePreference': 'imagePreference',
            
            'connectedToDeviceHostName': 'connectedToDeviceHostName',
            
            'connectedToPortName': 'connectedToPortName',
            
            'connetedToLocationCivicAddr': 'connetedToLocationCivicAddr'
            
        }       

        
        #Serial number
        
        self.serialNumber = None # str
        
        #ID of device
        
        self.id = None # str
        
        #Site to which device belongs if auto-provisioned
        
        self.site = None # str
        
        #Image file ID
        
        self.imageId = None # str
        
        #Platform ID
        
        self.platformId = None # str
        
        #Template config ID
        
        self.templateConfigId = None # str
        
        #License string
        
        self.licenseString = None # str
        
        #Wireless AP count
        
        self.apCount = None # str
        
        #Specify if device is a wireless mobility controller
        
        self.isMobilityController = None # str
        
        #Configure PKCS#12 trust point during PNP workflow if true
        
        self.pkiEnabled = None # bool
        
        #Configuration file id
        
        self.configId = None # str
        
        #Host name
        
        self.hostName = None # str
        
        #Bootstrap file id
        
        self.bootStrapId = None # str
        
        
        self.sudiRequired = None # bool
        
        #Device discovery info
        
        self.deviceDiscoveryInfo = None # ZtdDeviceDiscoveryInfo
        
        #CLI execution license level
        
        self.licenseLevel = None # str
        
        #Count of members in a stack switch excluding master
        
        self.memberCount = None # int
        
        #CLI execution EULA accepted or not
        
        self.eulaAccepted = None # bool
        
        
        self.memberDetail = None # list[ZtdMemberDetail]
        
        
        self.aliases = None # list[str]
        
        
        self.connectedToDeviceId = None # str
        
        
        self.connectedToPortId = None # str
        
        #Tag of device
        
        self.tag = None # str
        
        
        self.connetedToLocationGeoAddr = None # str
        
        
        self.configPreference = None # str
        
        
        self.imagePreference = None # str
        
        
        self.connectedToDeviceHostName = None # str
        
        
        self.connectedToPortName = None # str
        
        
        self.connetedToLocationCivicAddr = None # str
        
