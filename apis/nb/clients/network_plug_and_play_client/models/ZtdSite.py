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
            
            
            'tftpServer': 'str',
            
            
            'siteName': 'str',
            
            
            'deviceCount': 'int',
            
            
            'tftpPath': 'str',
            
            
            'installerUserID': 'str',
            
            
            'note': 'str',
            
            
            'deviceLastUpdate': 'str',
            
            
            'provisionedOn': 'str',
            
            
            'provisionedBy': 'str',
            
            
            'pendingDeviceCount': 'int',
            
            
            'state': 'str'
            
        }

        self.attributeMap = {
            
            'id': 'id',
            
            'tftpServer': 'tftpServer',
            
            'siteName': 'siteName',
            
            'deviceCount': 'deviceCount',
            
            'tftpPath': 'tftpPath',
            
            'installerUserID': 'installerUserID',
            
            'note': 'note',
            
            'deviceLastUpdate': 'deviceLastUpdate',
            
            'provisionedOn': 'provisionedOn',
            
            'provisionedBy': 'provisionedBy',
            
            'pendingDeviceCount': 'pendingDeviceCount',
            
            'state': 'state'
            
        }       

        
        #Project ID
        
        self.id = None # str
        
        #TFTP server host name or IP address
        
        self.tftpServer = None # str
        
        #Project name
        
        self.siteName = None # str
        
        #Number of devices under the project
        
        self.deviceCount = None # int
        
        #TFTP server path
        
        self.tftpPath = None # str
        
        #Installer user ID
        
        self.installerUserID = None # str
        
        #Project notes. Any file can be attached
        
        self.note = None # str
        
        #Last contact time among all devices in this project
        
        self.deviceLastUpdate = None # str
        
        #Creation time for project
        
        self.provisionedOn = None # str
        
        #User creating the project
        
        self.provisionedBy = None # str
        
        #Number of devices in pending state
        
        self.pendingDeviceCount = None # int
        
        #Project state
        
        self.state = None # str
        
