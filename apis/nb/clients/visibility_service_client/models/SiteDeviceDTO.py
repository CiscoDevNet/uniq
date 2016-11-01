#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class SiteDeviceDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'serialNumber': 'str',
            
            
            'status': 'str',
            
            
            'id': 'str',
            
            
            'mcDevice': 'bool',
            
            
            'siteId': 'str',
            
            
            'deviceId': 'str',
            
            
            'ipAddress': 'str',
            
            
            'unclaimedDeviceId': 'str',
            
            
            'hostName': 'str',
            
            
            'platformType': 'str',
            
            
            'discoveryType': 'str',
            
            
            'links': 'list[SiteDeviceLinkDTO]',
            
            
            'deviceValidationStatusDetail': 'str',
            
            
            'deviceValidationStatus': 'str',
            
            
            'coexistenceLoopbackIpAddress': 'str',
            
            
            'coexistenceLoopbackName': 'str',
            
            
            'defaultGW': 'str',
            
            
            'deviceType': 'str',
            
            
            'lanInterfaceName': 'list[str]',
            
            
            'brownFieldDevice': 'bool'
            
        }

        self.attributeMap = {
            
            'serialNumber': 'serialNumber',
            
            'status': 'status',
            
            'id': 'id',
            
            'mcDevice': 'mcDevice',
            
            'siteId': 'siteId',
            
            'deviceId': 'deviceId',
            
            'ipAddress': 'ipAddress',
            
            'unclaimedDeviceId': 'unclaimedDeviceId',
            
            'hostName': 'hostName',
            
            'platformType': 'platformType',
            
            'discoveryType': 'discoveryType',
            
            'links': 'links',
            
            'deviceValidationStatusDetail': 'deviceValidationStatusDetail',
            
            'deviceValidationStatus': 'deviceValidationStatus',
            
            'coexistenceLoopbackIpAddress': 'coexistenceLoopbackIpAddress',
            
            'coexistenceLoopbackName': 'coexistenceLoopbackName',
            
            'defaultGW': 'defaultGW',
            
            'deviceType': 'deviceType',
            
            'lanInterfaceName': 'lanInterfaceName',
            
            'brownFieldDevice': 'brownFieldDevice'
            
        }       

        
        
        self.serialNumber = None # str
        
        
        self.status = None # str
        
        
        self.id = None # str
        
        
        self.mcDevice = None # bool
        
        
        self.siteId = None # str
        
        
        self.deviceId = None # str
        
        
        self.ipAddress = None # str
        
        
        self.unclaimedDeviceId = None # str
        
        
        self.hostName = None # str
        
        
        self.platformType = None # str
        
        
        self.discoveryType = None # str
        
        
        self.links = None # list[SiteDeviceLinkDTO]
        
        
        self.deviceValidationStatusDetail = None # str
        
        
        self.deviceValidationStatus = None # str
        
        
        self.coexistenceLoopbackIpAddress = None # str
        
        
        self.coexistenceLoopbackName = None # str
        
        
        self.defaultGW = None # str
        
        
        self.deviceType = None # str
        
        
        self.lanInterfaceName = None # list[str]
        
        
        self.brownFieldDevice = None # bool
        
