#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class HubSiteWanDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'capacity': 'str',
            
            
            'vspEnabled': 'bool',
            
            
            'lanInterfaceName': 'list[str]',
            
            
            'deviceId': 'str',
            
            
            'wanCloud': 'WanCloudDTO',
            
            
            'wanType': 'str',
            
            
            'deviceType': 'str',
            
            
            'managementIpAddress': 'str',
            
            
            'bandwidth': 'str',
            
            
            'serviceProvider': 'str',
            
            
            'downloadBW': 'str',
            
            
            'natIp': 'str',
            
            
            'pathId': 'int',
            
            
            'mcDevice': 'bool',
            
            
            'defaultGW': 'str',
            
            
            'wanInterfaceName': 'str',
            
            
            'wanIp': 'str',
            
            
            'coexistenceLoopbackInterfaceName': 'str',
            
            
            'coexistenceLoopbackInterfaceIpAddress': 'str',
            
            
            'vspWanLebel': 'str',
            
            
            'wanLabel': 'str',
            
            
            'geoLocation': 'str',
            
            
            'vspWanType': 'str',
            
            
            'dhcpEnabled': 'bool',
            
            
            'id': 'str'
            
        }

        self.attributeMap = {
            
            'capacity': 'capacity',
            
            'vspEnabled': 'vspEnabled',
            
            'lanInterfaceName': 'lanInterfaceName',
            
            'deviceId': 'deviceId',
            
            'wanCloud': 'wanCloud',
            
            'wanType': 'wanType',
            
            'deviceType': 'deviceType',
            
            'managementIpAddress': 'managementIpAddress',
            
            'bandwidth': 'bandwidth',
            
            'serviceProvider': 'serviceProvider',
            
            'downloadBW': 'downloadBW',
            
            'natIp': 'natIp',
            
            'pathId': 'pathId',
            
            'mcDevice': 'mcDevice',
            
            'defaultGW': 'defaultGW',
            
            'wanInterfaceName': 'wanInterfaceName',
            
            'wanIp': 'wanIp',
            
            'coexistenceLoopbackInterfaceName': 'coexistenceLoopbackInterfaceName',
            
            'coexistenceLoopbackInterfaceIpAddress': 'coexistenceLoopbackInterfaceIpAddress',
            
            'vspWanLebel': 'vspWanLebel',
            
            'wanLabel': 'wanLabel',
            
            'geoLocation': 'geoLocation',
            
            'vspWanType': 'vspWanType',
            
            'dhcpEnabled': 'dhcpEnabled',
            
            'id': 'id'
            
        }       

        
        
        self.capacity = None # str
        
        
        self.vspEnabled = None # bool
        
        
        self.lanInterfaceName = None # list[str]
        
        
        self.deviceId = None # str
        
        
        self.wanCloud = None # WanCloudDTO
        
        
        self.wanType = None # str
        
        
        self.deviceType = None # str
        
        
        self.managementIpAddress = None # str
        
        
        self.bandwidth = None # str
        
        
        self.serviceProvider = None # str
        
        
        self.downloadBW = None # str
        
        
        self.natIp = None # str
        
        
        self.pathId = None # int
        
        
        self.mcDevice = None # bool
        
        
        self.defaultGW = None # str
        
        
        self.wanInterfaceName = None # str
        
        
        self.wanIp = None # str
        
        
        self.coexistenceLoopbackInterfaceName = None # str
        
        
        self.coexistenceLoopbackInterfaceIpAddress = None # str
        
        
        self.vspWanLebel = None # str
        
        
        self.wanLabel = None # str
        
        
        self.geoLocation = None # str
        
        
        self.vspWanType = None # str
        
        
        self.dhcpEnabled = None # bool
        
        
        self.id = None # str
        
