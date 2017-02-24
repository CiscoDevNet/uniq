#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ZtdDeviceDiscoveryInfo(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'timeout': 'int',
            
            
            'userNameList': 'list[str]',
            
            
            'passwordList': 'list[str]',
            
            
            'enablePasswordList': 'list[str]',
            
            
            'snmpAuthPassphrase': 'str',
            
            
            'snmpPrivPassphrase': 'str',
            
            
            'ipAddressList': 'str',
            
            
            'snmpMode': 'str',
            
            
            'snmpVersion': 'str',
            
            
            'discoveryType': 'str',
            
            
            'cdpLevel': 'int',
            
            
            'ipFilterList': 'list[str]',
            
            
            'protocolOrder': 'str',
            
            
            'retry': 'int',
            
            
            'snmpAuthProtocol': 'str',
            
            
            'snmpPrivProtocol': 'str',
            
            
            'snmpROCommunity': 'str',
            
            
            'snmpRWCommunity': 'str',
            
            
            'snmpUserName': 'str',
            
            
            'globalCredentialIdList': 'list[str]',
            
            
            'name': 'str'
            
        }

        self.attributeMap = {
            
            'timeout': 'timeout',
            
            'userNameList': 'userNameList',
            
            'passwordList': 'passwordList',
            
            'enablePasswordList': 'enablePasswordList',
            
            'snmpAuthPassphrase': 'snmpAuthPassphrase',
            
            'snmpPrivPassphrase': 'snmpPrivPassphrase',
            
            'ipAddressList': 'ipAddressList',
            
            'snmpMode': 'snmpMode',
            
            'snmpVersion': 'snmpVersion',
            
            'discoveryType': 'discoveryType',
            
            'cdpLevel': 'cdpLevel',
            
            'ipFilterList': 'ipFilterList',
            
            'protocolOrder': 'protocolOrder',
            
            'retry': 'retry',
            
            'snmpAuthProtocol': 'snmpAuthProtocol',
            
            'snmpPrivProtocol': 'snmpPrivProtocol',
            
            'snmpROCommunity': 'snmpROCommunity',
            
            'snmpRWCommunity': 'snmpRWCommunity',
            
            'snmpUserName': 'snmpUserName',
            
            'globalCredentialIdList': 'globalCredentialIdList',
            
            'name': 'name'
            
        }       

        
        #Time to wait for device response in seconds
        
        self.timeout = None # int
        
        #Username of the devices to be discovered
        
        self.userNameList = None # list[str]
        
        #Password of the devices to be discovered
        
        self.passwordList = None # list[str]
        
        #Enable Password of the devices to be discovered
        
        self.enablePasswordList = None # list[str]
        
        #Auth Pass phrase for SNMP
        
        self.snmpAuthPassphrase = None # str
        
        #Pass phrase for SNMP privacy
        
        self.snmpPrivPassphrase = None # str
        
        #Ip address of the device to be discovered
        
        self.ipAddressList = None # str
        
        #Mode of SNMP. Available values:&#39;AUTHPRIV&#39; or &#39;AUTHNOPRIV&#39; or &#39;NOAUTHNOPRIV&#39;
        
        self.snmpMode = None # str
        
        #Version of SNMP. Can be v2 or v3
        
        self.snmpVersion = None # str
        
        #Available types are: single, auto cdp discovery, range, multi range
        
        self.discoveryType = None # str
        
        #CDP level to which neighbor devices to be discovered
        
        self.cdpLevel = None # int
        
        #Username of the devices to be discovered
        
        self.ipFilterList = None # list[str]
        
        #Order of protocol in which device connection establishment to be tried
        
        self.protocolOrder = None # str
        
        #Number of times to try establishing connection to device
        
        self.retry = None # int
        
        #SNMP auth protocol. Available values:&#39;SHA&#39; or &#39;MD5&#39;
        
        self.snmpAuthProtocol = None # str
        
        #SNMP privacy protocol. Available values:&#39;DES&#39; or &#39;AES128&#39;
        
        self.snmpPrivProtocol = None # str
        
        #Snmp RO community of the devices to be discovered
        
        self.snmpROCommunity = None # str
        
        #Snmp RW community of the devices to be discovered
        
        self.snmpRWCommunity = None # str
        
        #SNMP username of the device
        
        self.snmpUserName = None # str
        
        #List of global credential ids to be used
        
        self.globalCredentialIdList = None # list[str]
        
        #Name for discovery
        
        self.name = None # str
        
