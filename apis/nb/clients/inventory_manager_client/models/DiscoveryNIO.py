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
            
            
            'deviceIds': 'str',
            
            
            'discoveryCondition': 'str',
            
            
            'globalCredentialIdList': 'list[str]',
            
            
            'numDevices': 'int',
            
            
            'isAutoCdp': 'bool',
            
            
            'parentDiscoveryId': 'str',
            
            
            'snmpRwCommunity': 'str',
            
            
            'snmpRoCommunity': 'str',
            
            
            'name': 'str',
            
            
            'ipAddressList': 'str',
            
            
            'discoveryType': 'str',
            
            
            'retryCount': 'int',
            
            
            'timeOut': 'int',
            
            
            'id': 'str',
            
            
            'discoveryStatus': 'str',
            
            
            'snmpMode': 'str',
            
            
            'snmpUserName': 'str',
            
            
            'attributeInfo': 'dict'
            
        }

        self.attributeMap = {
            
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
            
            'deviceIds': 'deviceIds',
            
            'discoveryCondition': 'discoveryCondition',
            
            'globalCredentialIdList': 'globalCredentialIdList',
            
            'numDevices': 'numDevices',
            
            'isAutoCdp': 'isAutoCdp',
            
            'parentDiscoveryId': 'parentDiscoveryId',
            
            'snmpRwCommunity': 'snmpRwCommunity',
            
            'snmpRoCommunity': 'snmpRoCommunity',
            
            'name': 'name',
            
            'ipAddressList': 'ipAddressList',
            
            'discoveryType': 'discoveryType',
            
            'retryCount': 'retryCount',
            
            'timeOut': 'timeOut',
            
            'id': 'id',
            
            'discoveryStatus': 'discoveryStatus',
            
            'snmpMode': 'snmpMode',
            
            'snmpUserName': 'snmpUserName',
            
            'attributeInfo': 'attributeInfo'
            
        }       

        
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
        
        #Ids of the devices discovered in a discovery
        
        self.deviceIds = None # str
        
        #To indicate the discovery status. Available options: Complete or In Progress
        
        self.discoveryCondition = None # str
        
        #To get the list of global credential of the discovery
        
        self.globalCredentialIdList = None # list[str]
        
        #Number of devices discovered in a discovery
        
        self.numDevices = None # int
        
        #Flag to mention if CDP discovery or not
        
        self.isAutoCdp = None # bool
        
        #Parent Discovery Id from which the discovery initiated
        
        self.parentDiscoveryId = None # str
        
        #Snmp RW community of the devices to be discovered
        
        self.snmpRwCommunity = None # str
        
        #Snmp RO community of the devices to be discovered
        
        self.snmpRoCommunity = None # str
        
        #Name for the discovery
        
        self.name = None # str
        
        #Ip address of the device to be discovered
        
        self.ipAddressList = None # str
        
        #Available types are: single, auto cdp discovery, range, multi range
        
        self.discoveryType = None # str
        
        #Number of times to try establishing connection to device
        
        self.retryCount = None # int
        
        #Time to wait for device response.
        
        self.timeOut = None # int
        
        #Unique identifier for discovery
        
        self.id = None # str
        
        #Available options are: active, inactive, edit
        
        self.discoveryStatus = None # str
        
        
        self.snmpMode = None # str
        
        
        self.snmpUserName = None # str
        
        
        self.attributeInfo = None # dict
        
