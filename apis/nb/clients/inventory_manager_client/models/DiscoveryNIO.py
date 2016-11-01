#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class DiscoveryNIO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'name': 'str',
            
            
            'cdpLevel': 'int',
            
            
            'enablePasswordList': 'str',
            
            
            'ipFilterList': 'str',
            
            
            'passwordList': 'str',
            
            
            'protocolOrder': 'str',
            
            
            'snmpAuthPassphrase': 'str',
            
            
            'snmpAuthProtocol': 'str',
            
            
            'snmpPrivPassphrase': 'str',
            
            
            'snmpPrivProtocol': 'str',
            
            
            'userNameList': 'str',
            
            
            'snmpRoCommunity': 'str',
            
            
            'snmpRwCommunity': 'str',
            
            
            'discoveryCondition': 'str',
            
            
            'numDevices': 'int',
            
            
            'isAutoCdp': 'bool',
            
            
            'globalCredentialIdList': 'list[str]',
            
            
            'parentDiscoveryId': 'str',
            
            
            'id': 'str',
            
            
            'snmpMode': 'str',
            
            
            'discoveryStatus': 'str',
            
            
            'deviceIds': 'str',
            
            
            'snmpUserName': 'str',
            
            
            'timeOut': 'int',
            
            
            'ipAddressList': 'str',
            
            
            'retryCount': 'int',
            
            
            'discoveryType': 'str'
            
        }

        self.attributeMap = {
            
            'name': 'name',
            
            'cdpLevel': 'cdpLevel',
            
            'enablePasswordList': 'enablePasswordList',
            
            'ipFilterList': 'ipFilterList',
            
            'passwordList': 'passwordList',
            
            'protocolOrder': 'protocolOrder',
            
            'snmpAuthPassphrase': 'snmpAuthPassphrase',
            
            'snmpAuthProtocol': 'snmpAuthProtocol',
            
            'snmpPrivPassphrase': 'snmpPrivPassphrase',
            
            'snmpPrivProtocol': 'snmpPrivProtocol',
            
            'userNameList': 'userNameList',
            
            'snmpRoCommunity': 'snmpRoCommunity',
            
            'snmpRwCommunity': 'snmpRwCommunity',
            
            'discoveryCondition': 'discoveryCondition',
            
            'numDevices': 'numDevices',
            
            'isAutoCdp': 'isAutoCdp',
            
            'globalCredentialIdList': 'globalCredentialIdList',
            
            'parentDiscoveryId': 'parentDiscoveryId',
            
            'id': 'id',
            
            'snmpMode': 'snmpMode',
            
            'discoveryStatus': 'discoveryStatus',
            
            'deviceIds': 'deviceIds',
            
            'snmpUserName': 'snmpUserName',
            
            'timeOut': 'timeOut',
            
            'ipAddressList': 'ipAddressList',
            
            'retryCount': 'retryCount',
            
            'discoveryType': 'discoveryType'
            
        }       

        
        #Name for the discovery
        
        self.name = None # str
        
        #CDP level to which neighbor devices to be discovered
        
        self.cdpLevel = None # int
        
        #Enable Password of the devices to be discovered
        
        self.enablePasswordList = None # str
        
        #IP addresses of the devices to be filtered
        
        self.ipFilterList = None # str
        
        #Password of the devices to be discovered
        
        self.passwordList = None # str
        
        #Order of protocol in which device connection establishment to be tried
        
        self.protocolOrder = None # str
        
        
        self.snmpAuthPassphrase = None # str
        
        
        self.snmpAuthProtocol = None # str
        
        
        self.snmpPrivPassphrase = None # str
        
        
        self.snmpPrivProtocol = None # str
        
        #Username of the devices to be discovered
        
        self.userNameList = None # str
        
        #Snmp RO community of the devices to be discovered
        
        self.snmpRoCommunity = None # str
        
        #Snmp RW community of the devices to be discovered
        
        self.snmpRwCommunity = None # str
        
        #To indicate the discovery status. Available options: Complete or In Progress
        
        self.discoveryCondition = None # str
        
        #Number of devices discovered in a discovery
        
        self.numDevices = None # int
        
        #Flag to mention if CDP discovery or not
        
        self.isAutoCdp = None # bool
        
        #To get the list of global credential of the discovery
        
        self.globalCredentialIdList = None # list[str]
        
        #Parent Discovery Id from which the discovery initiated
        
        self.parentDiscoveryId = None # str
        
        #Unique identifier for discovery
        
        self.id = None # str
        
        
        self.snmpMode = None # str
        
        #Available options are: active, inactive, edit
        
        self.discoveryStatus = None # str
        
        #Ids of the devices discovered in a discovery
        
        self.deviceIds = None # str
        
        
        self.snmpUserName = None # str
        
        #Time to wait for device response.
        
        self.timeOut = None # int
        
        #Ip address of the device to be discovered
        
        self.ipAddressList = None # str
        
        #Number of times to try establishing connection to device
        
        self.retryCount = None # int
        
        #Available types are: single, auto cdp discovery, range, multi range
        
        self.discoveryType = None # str
        
