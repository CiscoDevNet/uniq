#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class HostDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'hostName': 'str',
            
            
            'source': 'str',
            
            
            'avgUpdateFrequency': 'str',
            
            
            'lastUpdated': 'str',
            
            
            'subType': 'str',
            
            
            'vlanId': 'str',
            
            
            'id': 'str',
            
            
            'connectedInterfaceName': 'str',
            
            
            'connectedNetworkDeviceId': 'str',
            
            
            'connectedNetworkDeviceIpAddress': 'str',
            
            
            'hostMac': 'str',
            
            
            'hostType': 'str',
            
            
            'pointOfAttachment': 'str',
            
            
            'pointOfPresence': 'str',
            
            
            'connectedAPMacAddress': 'str',
            
            
            'connectedAPName': 'str',
            
            
            'connectedInterfaceId': 'str',
            
            
            'hostIp': 'str',
            
            
            'attributeInfo': 'dict'
            
        }

        self.attributeMap = {
            
            'hostName': 'hostName',
            
            'source': 'source',
            
            'avgUpdateFrequency': 'avgUpdateFrequency',
            
            'lastUpdated': 'lastUpdated',
            
            'subType': 'subType',
            
            'vlanId': 'vlanId',
            
            'id': 'id',
            
            'connectedInterfaceName': 'connectedInterfaceName',
            
            'connectedNetworkDeviceId': 'connectedNetworkDeviceId',
            
            'connectedNetworkDeviceIpAddress': 'connectedNetworkDeviceIpAddress',
            
            'hostMac': 'hostMac',
            
            'hostType': 'hostType',
            
            'pointOfAttachment': 'pointOfAttachment',
            
            'pointOfPresence': 'pointOfPresence',
            
            'connectedAPMacAddress': 'connectedAPMacAddress',
            
            'connectedAPName': 'connectedAPName',
            
            'connectedInterfaceId': 'connectedInterfaceId',
            
            'hostIp': 'hostIp',
            
            'attributeInfo': 'attributeInfo'
            
        }       

        
        #Name of the host
        
        self.hostName = None # str
        
        #Source from which the host gets collected. Available option:200 for inventory collection and 300 for trap based data collection
        
        self.source = None # str
        
        #Frequency in which host info gets updated
        
        self.avgUpdateFrequency = None # str
        
        #Time when the host info last got updated
        
        self.lastUpdated = None # str
        
        
        self.subType = None # str
        
        #Vlan Id of the host
        
        self.vlanId = None # str
        
        #Id of the host
        
        self.id = None # str
        
        #Name of the interface to which host gets connected
        
        self.connectedInterfaceName = None # str
        
        #Id of the network device to which host gets connected
        
        self.connectedNetworkDeviceId = None # str
        
        #Ip address of the network device to which host gets connected
        
        self.connectedNetworkDeviceIpAddress = None # str
        
        #Mac address of the host
        
        self.hostMac = None # str
        
        #Type of the host. Available options are: Wired, Wireless
        
        self.hostType = None # str
        
        #Id of the Host&#39;s Point of attachment network device (wlc). Based on mobility
        
        self.pointOfAttachment = None # str
        
        #Id of the Host&#39;s Point of presence network device (wlc). Based on mobility
        
        self.pointOfPresence = None # str
        
        #Mac address of the AP to which wireless host gets connected
        
        self.connectedAPMacAddress = None # str
        
        #Name of the AP to which wireless host gets connected
        
        self.connectedAPName = None # str
        
        #Id of the interface to which host gets connected
        
        self.connectedInterfaceId = None # str
        
        #Ip address of the host
        
        self.hostIp = None # str
        
        
        self.attributeInfo = None # dict
        
