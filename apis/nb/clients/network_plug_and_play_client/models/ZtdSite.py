#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ZtdSite(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'id': 'str',
            
            
            'provisionedBy': 'str',
            
            
            'provisionedOn': 'str',
            
            
            'siteName': 'str',
            
            
            'tftpServer': 'str',
            
            
            'tftpPath': 'str',
            
            
            'note': 'str',
            
            
            'deviceCount': 'int',
            
            
            'pendingDeviceCount': 'int',
            
            
            'deviceLastUpdate': 'str',
            
            
            'installerUserID': 'str',
            
            
            'state': 'str'
            
        }

        self.attributeMap = {
            
            'id': 'id',
            
            'provisionedBy': 'provisionedBy',
            
            'provisionedOn': 'provisionedOn',
            
            'siteName': 'siteName',
            
            'tftpServer': 'tftpServer',
            
            'tftpPath': 'tftpPath',
            
            'note': 'note',
            
            'deviceCount': 'deviceCount',
            
            'pendingDeviceCount': 'pendingDeviceCount',
            
            'deviceLastUpdate': 'deviceLastUpdate',
            
            'installerUserID': 'installerUserID',
            
            'state': 'state'
            
        }       

        
        #Project ID
        
        self.id = None # str
        
        #User creating the project
        
        self.provisionedBy = None # str
        
        #Creation time for project
        
        self.provisionedOn = None # str
        
        #Project name
        
        self.siteName = None # str
        
        #TFTP server host name or IP address
        
        self.tftpServer = None # str
        
        #TFTP server path
        
        self.tftpPath = None # str
        
        #Project notes. Any file can be attached
        
        self.note = None # str
        
        #Number of devices under the project
        
        self.deviceCount = None # int
        
        #Number of devices in pending state
        
        self.pendingDeviceCount = None # int
        
        #Last contact time among all devices in this project
        
        self.deviceLastUpdate = None # str
        
        #Installer user ID
        
        self.installerUserID = None # str
        
        #Project state
        
        self.state = None # str
        
