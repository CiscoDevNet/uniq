#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class InventoryDeviceInfo(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'snmpAuthPassphrase': 'str',
            
            
            'snmpAuthProtocol': 'str',
            
            
            'snmpPrivPassphrase': 'str',
            
            
            'snmpPrivProtocol': 'str',
            
            
            'snmpROCommunity': 'str',
            
            
            'snmpRWCommunity': 'str',
            
            
            'extendedDiscoveryInfo': 'str',
            
            
            'snmpRetry': 'int',
            
            
            'serialNumber': 'str',
            
            
            'snmpVersion': 'str',
            
            
            'userName': 'str',
            
            
            'enablePassword': 'str',
            
            
            'ipAddress': 'list[str]',
            
            
            'password': 'str',
            
            
            'snmpMode': 'str',
            
            
            'snmpTimeout': 'int',
            
            
            'snmpUserName': 'str',
            
            
            'cliTransport': 'str'
            
        }

        self.attributeMap = {
            
            'snmpAuthPassphrase': 'snmpAuthPassphrase',
            
            'snmpAuthProtocol': 'snmpAuthProtocol',
            
            'snmpPrivPassphrase': 'snmpPrivPassphrase',
            
            'snmpPrivProtocol': 'snmpPrivProtocol',
            
            'snmpROCommunity': 'snmpROCommunity',
            
            'snmpRWCommunity': 'snmpRWCommunity',
            
            'extendedDiscoveryInfo': 'extendedDiscoveryInfo',
            
            'snmpRetry': 'snmpRetry',
            
            'serialNumber': 'serialNumber',
            
            'snmpVersion': 'snmpVersion',
            
            'userName': 'userName',
            
            'enablePassword': 'enablePassword',
            
            'ipAddress': 'ipAddress',
            
            'password': 'password',
            
            'snmpMode': 'snmpMode',
            
            'snmpTimeout': 'snmpTimeout',
            
            'snmpUserName': 'snmpUserName',
            
            'cliTransport': 'cliTransport'
            
        }       

        
        #SNMPV3 auth passphrase
        
        self.snmpAuthPassphrase = None # str
        
        #SNMPV3 auth protocol. Supported values: sha, md5
        
        self.snmpAuthProtocol = None # str
        
        #SNMPV3 priv passphrase
        
        self.snmpPrivPassphrase = None # str
        
        #SNMPV3 priv protocol. Supported values: des, aes
        
        self.snmpPrivProtocol = None # str
        
        #SNMP RO community
        
        self.snmpROCommunity = None # str
        
        #SNMP RW community
        
        self.snmpRWCommunity = None # str
        
        
        self.extendedDiscoveryInfo = None # str
        
        #SNMP retry count. Max value supported is 3
        
        self.snmpRetry = None # int
        
        
        self.serialNumber = None # str
        
        #SNMP version. Values supported: v2, v3. Default is v2
        
        self.snmpVersion = None # str
        
        #CLI user name
        
        self.userName = None # str
        
        #CLI enable password
        
        self.enablePassword = None # str
        
        #IP Address of the device
        
        self.ipAddress = None # list[str]
        
        #CLI password
        
        self.password = None # str
        
        #SNMPV3 mode. Supported values: noAuthnoPriv, authNoPriv, authPriv
        
        self.snmpMode = None # str
        
        #SNMP timeout in seconds
        
        self.snmpTimeout = None # int
        
        #SNMPV3 user name
        
        self.snmpUserName = None # str
        
        #CLI transport. Supported values: telnet, ssh2
        
        self.cliTransport = None # str
        
