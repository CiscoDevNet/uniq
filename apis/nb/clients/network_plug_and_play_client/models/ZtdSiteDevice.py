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

class ZtdSiteDevice(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'state': 'str',


            'lastContact': 'str',


            'authStatus': 'DeviceAuthState',


            'deviceId': 'str',


            'lastStateTransitionTime': 'str',


            'stateDisplay': 'str',


            'hostName': 'str',


            'serialNumber': 'str',


            'tag': 'str',


            'id': 'str',


            'platformId': 'str',


            'site': 'str',


            'configId': 'str',


            'bootStrapId': 'str',


            'licenseString': 'str',


            'apCount': 'str',


            'isMobilityController': 'str',


            'pkiEnabled': 'bool',


            'sudiRequired': 'bool',


            'imageId': 'str',


            'connectedToDeviceId': 'str',


            'connectedToPortId': 'str',


            'imagePreference': 'str',


            'configPreference': 'str',


            'connetedToLocationGeoAddr': 'str',


            'connectedToDeviceHostName': 'str',


            'connectedToPortName': 'str',


            'connetedToLocationCivicAddr': 'str',


            # 'attributeInfo': 'object'

            'licenseLevel': 'str',


            'memberCount': 'int',


            'eulaAccepted': 'bool'


        }

        self.attributeMap = {

            'state': 'state',

            'lastContact': 'lastContact',

            'authStatus': 'authStatus',

            'deviceId': 'deviceId',

            'lastStateTransitionTime': 'lastStateTransitionTime',

            'stateDisplay': 'stateDisplay',

            'hostName': 'hostName',

            'serialNumber': 'serialNumber',

            'tag': 'tag',

            'id': 'id',

            'platformId': 'platformId',

            'site': 'site',

            'configId': 'configId',

            'bootStrapId': 'bootStrapId',

            'licenseString': 'licenseString',

            'apCount': 'apCount',

            'isMobilityController': 'isMobilityController',

            'pkiEnabled': 'pkiEnabled',

            'sudiRequired': 'sudiRequired',

            'imageId': 'imageId',

            'connectedToDeviceId': 'connectedToDeviceId',

            'connectedToPortId': 'connectedToPortId',

            'imagePreference': 'imagePreference',

            'configPreference': 'configPreference',

            'connetedToLocationGeoAddr': 'connetedToLocationGeoAddr',

            'connectedToDeviceHostName': 'connectedToDeviceHostName',

            'connectedToPortName': 'connectedToPortName',

            'connetedToLocationCivicAddr': 'connetedToLocationCivicAddr',

            # 'attributeInfo': 'attributeInfo'

            'licenseLevel': 'licenseLevel',

            'memberCount': 'memberCount',

            'eulaAccepted': 'eulaAccepted'

        }



        self.state = None # str


        self.lastContact = None # str


        self.authStatus = None # DeviceAuthState


        self.deviceId = None # str


        self.lastStateTransitionTime = None # str


        self.stateDisplay = None # str

        #Host name

        self.hostName = None # str

        #Serial number

        self.serialNumber = None # str

        #Tag of device

        self.tag = None # str

        #ID of device

        self.id = None # str

        #Platform ID

        self.platformId = None # str

        #Site to which device belongs if auto-provisioned

        self.site = None # str

        #Configuration file id

        self.configId = None # str

        #Bootstrap file id

        self.bootStrapId = None # str

        #License string

        self.licenseString = None # str

        #Wireless AP count

        self.apCount = None # str

        #Specify if device is a wireless mobility controller

        self.isMobilityController = None # str

        #Configure PKCS#12 trust point during PNP workflow if true

        self.pkiEnabled = None # bool


        self.sudiRequired = None # bool

        #Image file ID

        self.imageId = None # str


        self.connectedToDeviceId = None # str


        self.connectedToPortId = None # str


        self.imagePreference = None # str


        self.configPreference = None # str


        self.connetedToLocationGeoAddr = None # str


        self.connectedToDeviceHostName = None # str


        self.connectedToPortName = None # str


        self.connetedToLocationCivicAddr = None # str


        # self.attributeInfo = None # object


        #CLI execution license level
        self.licenseLevel = None # str

        #Count of members in a stack switch excluding master
        self.memberCount = None # int

        #CLI execution EULA accepted or not
        self.eulaAccepted = None # bool
