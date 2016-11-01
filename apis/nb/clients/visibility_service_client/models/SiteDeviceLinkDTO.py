#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class SiteDeviceLinkDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'id': 'str',
            
            
            'ipAddress': 'str',
            
            
            'interfaceName': 'str',
            
            
            'deviceUuid': 'str',
            
            
            'label': 'str',
            
            
            'bandwidth': 'float',
            
            
            'downloadBW': 'float',
            
            
            'serviceProvider': 'str',
            
            
            'wanName': 'str',
            
            
            'wanCloudUuid': 'str'
            
        }

        self.attributeMap = {
            
            'id': 'id',
            
            'ipAddress': 'ipAddress',
            
            'interfaceName': 'interfaceName',
            
            'deviceUuid': 'deviceUuid',
            
            'label': 'label',
            
            'bandwidth': 'bandwidth',
            
            'downloadBW': 'downloadBW',
            
            'serviceProvider': 'serviceProvider',
            
            'wanName': 'wanName',
            
            'wanCloudUuid': 'wanCloudUuid'
            
        }       

        
        
        self.id = None # str
        
        
        self.ipAddress = None # str
        
        
        self.interfaceName = None # str
        
        
        self.deviceUuid = None # str
        
        
        self.label = None # str
        
        
        self.bandwidth = None # float
        
        
        self.downloadBW = None # float
        
        
        self.serviceProvider = None # str
        
        
        self.wanName = None # str
        
        
        self.wanCloudUuid = None # str
        
