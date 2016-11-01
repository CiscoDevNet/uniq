#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class WanLinkDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'id': 'str',
            
            
            'nextHopAddress': 'str',
            
            
            'natAddress': 'str',
            
            
            'uploadBW': 'float',
            
            
            'tunnelId': 'int',
            
            
            'interfaceName': 'str',
            
            
            'deviceUuid': 'str',
            
            
            'downloadBW': 'float',
            
            
            'serviceProvider': 'str',
            
            
            'wanAddress': 'str',
            
            
            'wanAddressSubnetMask': 'str',
            
            
            'wanCloudUuid': 'str'
            
        }

        self.attributeMap = {
            
            'id': 'id',
            
            'nextHopAddress': 'nextHopAddress',
            
            'natAddress': 'natAddress',
            
            'uploadBW': 'uploadBW',
            
            'tunnelId': 'tunnelId',
            
            'interfaceName': 'interfaceName',
            
            'deviceUuid': 'deviceUuid',
            
            'downloadBW': 'downloadBW',
            
            'serviceProvider': 'serviceProvider',
            
            'wanAddress': 'wanAddress',
            
            'wanAddressSubnetMask': 'wanAddressSubnetMask',
            
            'wanCloudUuid': 'wanCloudUuid'
            
        }       

        
        
        self.id = None # str
        
        
        self.nextHopAddress = None # str
        
        
        self.natAddress = None # str
        
        
        self.uploadBW = None # float
        
        
        self.tunnelId = None # int
        
        
        self.interfaceName = None # str
        
        
        self.deviceUuid = None # str
        
        
        self.downloadBW = None # float
        
        
        self.serviceProvider = None # str
        
        
        self.wanAddress = None # str
        
        
        self.wanAddressSubnetMask = None # str
        
        
        self.wanCloudUuid = None # str
        
