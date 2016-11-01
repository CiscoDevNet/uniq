#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


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

