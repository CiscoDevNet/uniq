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

class ZtdRule(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'serialNumber': 'str',


            'id': 'str',


            'site': 'str',


            'imageId': 'str',


            'platformId': 'str',


            'hostName': 'str',


            'configId': 'str',


            'bootStrapId': 'str',


            'pkiEnabled': 'bool',


            'sudiRequired': 'bool',


            'licenseString': 'str',


            'apCount': 'str',


            'isMobilityController': 'str',


            'connectedToDeviceId': 'str',


            'connectedToPortId': 'str',


            'tag': 'str',


            'configPreference': 'str',


            'imagePreference': 'str',


            'connetedToLocationCivicAddr': 'str',


            'connetedToLocationGeoAddr': 'str',


            'connectedToDeviceHostName': 'str',


            'connectedToPortName': 'str',


            'eulaAccepted': 'bool',


            'licenseLevel': 'str',


            'memberCount': 'int'

        }

        self.attributeMap = {

            'serialNumber': 'serialNumber',

            'id': 'id',

            'site': 'site',

            'imageId': 'imageId',

            'platformId': 'platformId',

            'hostName': 'hostName',

            'configId': 'configId',

            'bootStrapId': 'bootStrapId',

            'pkiEnabled': 'pkiEnabled',

            'sudiRequired': 'sudiRequired',

            'licenseString': 'licenseString',

            'apCount': 'apCount',

            'isMobilityController': 'isMobilityController',

            'connectedToDeviceId': 'connectedToDeviceId',

            'connectedToPortId': 'connectedToPortId',

            'tag': 'tag',

            'configPreference': 'configPreference',

            'imagePreference': 'imagePreference',

            'connetedToLocationCivicAddr': 'connetedToLocationCivicAddr',

            'connetedToLocationGeoAddr': 'connetedToLocationGeoAddr',

            'connectedToDeviceHostName': 'connectedToDeviceHostName',

            'connectedToPortName': 'connectedToPortName',

            'eulaAccepted': 'eulaAccepted',

            'licenseLevel': 'licenseLevel',

            'memberCount': 'memberCount'

        }


        #Serial number

        self.serialNumber = None # str

        #ID of device

        self.id = None # str

        #Site to which device belongs if auto-provisioned

        self.site = None # str

        #Image file ID

        self.imageId = None # str

        #Platform ID

        self.platformId = None # str

        #Host name

        self.hostName = None # str

        #Configuration file id

        self.configId = None # str

        #Bootstrap file id

        self.bootStrapId = None # str

        #Configure PKCS#12 trust point during PNP workflow if true

        self.pkiEnabled = None # bool


        self.sudiRequired = None # bool

        #License string

        self.licenseString = None # str

        #Wireless AP count

        self.apCount = None # str

        #Specify if device is a wireless mobility controller

        self.isMobilityController = None # str


        self.connectedToDeviceId = None # str


        self.connectedToPortId = None # str

        #Tag of device

        self.tag = None # str


        self.configPreference = None # str


        self.imagePreference = None # str


        self.connetedToLocationCivicAddr = None # str


        self.connetedToLocationGeoAddr = None # str


        self.connectedToDeviceHostName = None # str


        self.connectedToPortName = None # str

        #CLI execution EULA accepted or not
        self.eulaAccepted = None # bool

        #CLI execution license level
        self.licenseLevel = None # str

        #Count of members in a stack switch excluding master
        self.memberCount = None # int

