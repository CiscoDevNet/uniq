#!/usr/bin/env python
#pylint: skip-file
"""
Copyright 2016 Cisco Systems

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

class ZtdSite(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'state': 'str',


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


            'installerUserID': 'str'

        }

        self.attributeMap = {

            'state': 'state',

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

            'installerUserID': 'installerUserID'

        }


        #Project state

        self.state = None # str

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

