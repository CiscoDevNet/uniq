#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class NetworkDeviceReachabilityInfoNIO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'snmpCommunity': 'str',
            
            
            'mgmtIp': 'str',
            
            
            'protocolList': 'str',
            
            
            'protocolUsed': 'str',
            
            
            'discoveryStartTime': 'str',
            
            
            'userName': 'str',
            
            
            'password': 'str',
            
            
            'id': 'str',
            
            
            'discoveryId': 'str',
            
            
            'reachabilityFailureReason': 'str',
            
            
            'reachabilityStatus': 'str',
            
            
            'enablePassword': 'str',
            
            
            'attributeInfo': 'dict'
            
        }

        self.attributeMap = {
            
            'snmpCommunity': 'snmpCommunity',
            
            'mgmtIp': 'mgmtIp',
            
            'protocolList': 'protocolList',
            
            'protocolUsed': 'protocolUsed',
            
            'discoveryStartTime': 'discoveryStartTime',
            
            'userName': 'userName',
            
            'password': 'password',
            
            'id': 'id',
            
            'discoveryId': 'discoveryId',
            
            'reachabilityFailureReason': 'reachabilityFailureReason',
            
            'reachabilityStatus': 'reachabilityStatus',
            
            'enablePassword': 'enablePassword',
            
            'attributeInfo': 'attributeInfo'
            
        }       

        
        #SNMP community used for device connectivity
        
        self.snmpCommunity = None # str
        
        #IP address of the device
        
        self.mgmtIp = None # str
        
        #Protocol order given for discovery
        
        self.protocolList = None # str
        
        #Protocol used for device discovery
        
        self.protocolUsed = None # str
        
        #Time when the discovery was started
        
        self.discoveryStartTime = None # str
        
        #CLI username used for device connectivity
        
        self.userName = None # str
        
        #CLI password used for device connectivity
        
        self.password = None # str
        
        #Unique identifier for reachability-info
        
        self.id = None # str
        
        #ID of discovery thorugh which device was discovered
        
        self.discoveryId = None # str
        
        #Reason for failure if the device is not discovered successfully
        
        self.reachabilityFailureReason = None # str
        
        #Reachability status of the device as Reachable / Unreachable
        
        self.reachabilityStatus = None # str
        
        #CLI enable password used for device connectivity
        
        self.enablePassword = None # str
        
        
        self.attributeInfo = None # dict
        
