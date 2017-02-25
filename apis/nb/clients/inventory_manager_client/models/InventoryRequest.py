#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class InventoryRequest(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'cdpLevel': 'int',
            
            
            'enablePasswordList': 'list[str]',
            
            
            'ipFilterList': 'list[str]',
            
            
            'passwordList': 'list[str]',
            
            
            'protocolOrder': 'str',
            
            
            'reDiscovery': 'bool',
            
            
            'retry': 'int',
            
            
            'snmpAuthPassphrase': 'str',
            
            
            'snmpAuthProtocol': 'str',
            
            
            'snmpPrivPassphrase': 'str',
            
            
            'snmpPrivProtocol': 'str',
            
            
            'snmpROCommunity': 'str',
            
            
            'snmpRWCommunity': 'str',
            
            
            'userNameList': 'list[str]',
            
            
            'globalCredentialIdList': 'list[str]',
            
            
            'parentDiscoveryId': 'str',
            
            
            'name': 'str',
            
            
            'timeout': 'int',
            
            
            'ipAddressList': 'str',
            
            
            'snmpVersion': 'str',
            
            
            'discoveryType': 'str',
            
            
            'snmpMode': 'str',
            
            
            'snmpUserName': 'str'
            
        }

        self.attributeMap = {
            
            'cdpLevel': 'cdpLevel',
            
            'enablePasswordList': 'enablePasswordList',
            
            'ipFilterList': 'ipFilterList',
            
            'passwordList': 'passwordList',
            
            'protocolOrder': 'protocolOrder',
            
            'reDiscovery': 'reDiscovery',
            
            'retry': 'retry',
            
            'snmpAuthPassphrase': 'snmpAuthPassphrase',
            
            'snmpAuthProtocol': 'snmpAuthProtocol',
            
            'snmpPrivPassphrase': 'snmpPrivPassphrase',
            
            'snmpPrivProtocol': 'snmpPrivProtocol',
            
            'snmpROCommunity': 'snmpROCommunity',
            
            'snmpRWCommunity': 'snmpRWCommunity',
            
            'userNameList': 'userNameList',
            
            'globalCredentialIdList': 'globalCredentialIdList',
            
            'parentDiscoveryId': 'parentDiscoveryId',
            
            'name': 'name',
            
            'timeout': 'timeout',
            
            'ipAddressList': 'ipAddressList',
            
            'snmpVersion': 'snmpVersion',
            
            'discoveryType': 'discoveryType',
            
            'snmpMode': 'snmpMode',
            
            'snmpUserName': 'snmpUserName'
            
        }       

        
        #CDP level to which neighbor devices to be discovered
        
        self.cdpLevel = None # int
        
        #Enable Password of the devices to be discovered
        
        self.enablePasswordList = None # list[str]
        
        #Ip addresses of the devices to be filtered out during discovery
        
        self.ipFilterList = None # list[str]
        
        #Password of the devices to be discovered
        
        self.passwordList = None # list[str]
        
        #Order of protocol in which device connection establishment to be tried
        
        self.protocolOrder = None # str
        
        #Flag to indicate if rediscovery is needed or not
        
        self.reDiscovery = None # bool
        
        #Number of times to try establishing connection to device
        
        self.retry = None # int
        
        #Auth Pass phrase for SNMP
        
        self.snmpAuthPassphrase = None # str
        
        #SNMP auth protocol. Available values:&#39;SHA&#39; or &#39;MD5&#39;
        
        self.snmpAuthProtocol = None # str
        
        #Pass phrase for SNMP privacy
        
        self.snmpPrivPassphrase = None # str
        
        #SNMP privacy protocol. Available values:&#39;DES&#39; or &#39;AES128&#39;
        
        self.snmpPrivProtocol = None # str
        
        #Snmp RO community of the devices to be discovered
        
        self.snmpROCommunity = None # str
        
        #Snmp RW community of the devices to be discovered
        
        self.snmpRWCommunity = None # str
        
        #Username of the devices to be discovered
        
        self.userNameList = None # list[str]
        
        #List of global credential ids to be used
        
        self.globalCredentialIdList = None # list[str]
        
        
        self.parentDiscoveryId = None # str
        
        #Name for discovery
        
        self.name = None # str
        
        #Time to wait for device response in seconds
        
        self.timeout = None # int
        
        #Ip address(es) of the device to be discovered
        
        self.ipAddressList = None # str
        
        #Version of SNMP. Can be v2 or v3
        
        self.snmpVersion = None # str
        
        #Available types are: single, auto cdp discovery, range, multi range
        
        self.discoveryType = None # str
        
        #Mode of SNMP. Available values:&#39;AUTHPRIV&#39; or &#39;AUTHNOPRIV&#39; or &#39;NOAUTHNOPRIV&#39;
        
        self.snmpMode = None # str
        
        #SNMP username of the device
        
        self.snmpUserName = None # str
        
