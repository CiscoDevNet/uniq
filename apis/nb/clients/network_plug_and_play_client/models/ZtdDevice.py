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

class ZtdDevice(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'state': 'str',


            'hostName': 'str',


            'serialNumber': 'str',


            'ipAddress': 'str',


            'id': 'str',


            'platformId': 'str',


            'site': 'str',


            'macAddress': 'str',


            'configId': 'str',


            'licenseString': 'str',


            'apCount': 'str',


            'isMobilityController': 'str',


            'pkiEnabled': 'bool',


            'sudiRequired': 'bool',


            'memberUdi': 'str',


            'imageId': 'str',


            'firstContact': 'str',


            'lastContact': 'str',


            'fileDestination': 'str',


            'backoffTimer': 'str',


            'provisioningType': 'str',


            'unclaimedHint': 'str',


            'bootstrapId': 'str',


            'oldNetworkDeviceId': 'str',


            'hwRevision': 'str',


            'mainMemSize': 'str',


            'boardId': 'str',


            'boardReworkId': 'str',


            'midplaneVersion': 'str',


            'versionString': 'str',


            'imageFile': 'str',


            'returnToRomReason': 'str',


            'bootVariable': 'str',


            'bootLdrVariable': 'str',


            'configVariable': 'str',


            'configReg': 'str',


            'configRegNext': 'str',


            'topologyInfo': 'str',


            'filesystemInfo': 'str',


            'deviceDetailsLastUpdate': 'str',


            'slotNumber': 'str',


            'certificateNeededState': 'str',


            'pnpProfileUsedAddr': 'str',


            'pnpProfileUsedHost': 'str',


            'authStatus': 'DeviceAuthState',


            'deviceCertificate': 'str',


            'deviceType': 'str',


            'lastStateTransitionTime': 'str',


            'stateDisplay': 'str',


            'versionCompatible': 'str',


            'cleanup': 'bool',


            'memberDetail': 'list[ZtdMemberDetail]',


            'eulaAccepted': 'bool',


            'licenseLevel': 'str'
        }

        self.attributeMap = {

            'state': 'state',

            'hostName': 'hostName',

            'serialNumber': 'serialNumber',

            'ipAddress': 'ipAddress',

            'id': 'id',

            'platformId': 'platformId',

            'site': 'site',

            'macAddress': 'macAddress',

            'configId': 'configId',

            'licenseString': 'licenseString',

            'apCount': 'apCount',

            'isMobilityController': 'isMobilityController',

            'pkiEnabled': 'pkiEnabled',

            'sudiRequired': 'sudiRequired',

            'memberUdi': 'memberUdi',

            'imageId': 'imageId',

            'firstContact': 'firstContact',

            'lastContact': 'lastContact',

            'fileDestination': 'fileDestination',

            'backoffTimer': 'backoffTimer',

            'provisioningType': 'provisioningType',

            'unclaimedHint': 'unclaimedHint',

            'bootstrapId': 'bootstrapId',

            'oldNetworkDeviceId': 'oldNetworkDeviceId',

            'hwRevision': 'hwRevision',

            'mainMemSize': 'mainMemSize',

            'boardId': 'boardId',

            'boardReworkId': 'boardReworkId',

            'midplaneVersion': 'midplaneVersion',

            'versionString': 'versionString',

            'imageFile': 'imageFile',

            'returnToRomReason': 'returnToRomReason',

            'bootVariable': 'bootVariable',

            'bootLdrVariable': 'bootLdrVariable',

            'configVariable': 'configVariable',

            'configReg': 'configReg',

            'configRegNext': 'configRegNext',

            'topologyInfo': 'topologyInfo',

            'filesystemInfo': 'filesystemInfo',

            'deviceDetailsLastUpdate': 'deviceDetailsLastUpdate',

            'slotNumber': 'slotNumber',

            'certificateNeededState': 'certificateNeededState',

            'pnpProfileUsedAddr': 'pnpProfileUsedAddr',

            'pnpProfileUsedHost': 'pnpProfileUsedHost',

            'authStatus': 'authStatus',

            'deviceCertificate': 'deviceCertificate',

            'deviceType': 'deviceType',

            'lastStateTransitionTime': 'lastStateTransitionTime',

            'stateDisplay': 'stateDisplay',

            'versionCompatible': 'versionCompatible',

            'cleanup': 'cleanup',

            'memberDetail': 'memberDetail',

            'eulaAccepted': 'eulaAccepted',

            'licenseLevel': 'licenseLevel'

        }


        #Device state

        self.state = None # str

        #Host name

        self.hostName = None # str

        #Serial number

        self.serialNumber = None # str


        self.ipAddress = None # str

        #Device ID

        self.id = None # str

        #Platform ID

        self.platformId = None # str

        #Project to which device belongs if pre-provisioned

        self.site = None # str


        self.macAddress = None # str

        #Configuration file ID

        self.configId = None # str

        #License information

        self.licenseString = None # str

        #Wireless AP count

        self.apCount = None # str

        #Specify if device is a wireless mobility controller

        self.isMobilityController = None # str

        #Configure PKCS#12 trust point during PnP workflow if true

        self.pkiEnabled = None # bool


        self.sudiRequired = None # bool

        #Unique device ID of redundant/stack switches

        self.memberUdi = None # str

        #Image file ID

        self.imageId = None # str

        #First contact time of device

        self.firstContact = None # str

        #Last contact time of device

        self.lastContact = None # str

        #Location on device to which image/config files will be copied

        self.fileDestination = None # str

        #Backoff timer

        self.backoffTimer = None # str

        #Type of device

        self.provisioningType = None # str

        #Hint whether device might be RMA

        self.unclaimedHint = None # str

        #Bootstrap file ID

        self.bootstrapId = None # str

        #Inventory device of which this device is the replacement

        self.oldNetworkDeviceId = None # str

        #HW revision

        self.hwRevision = None # str

        #Main memory size

        self.mainMemSize = None # str

        #Board ID

        self.boardId = None # str

        #Board rework ID

        self.boardReworkId = None # str

        #Mid plane version

        self.midplaneVersion = None # str

        #IOS Version

        self.versionString = None # str

        #Image ID

        self.imageFile = None # str

        #Return to rom reason

        self.returnToRomReason = None # str

        #Boot variable

        self.bootVariable = None # str

        #Boot ldr variable

        self.bootLdrVariable = None # str

        #Config variable

        self.configVariable = None # str

        #Config reg

        self.configReg = None # str

        #Config reg next

        self.configRegNext = None # str

        #Information about topology

        self.topologyInfo = None # str

        #Information about filesystem

        self.filesystemInfo = None # str

        #Timestamp when the device details were last read

        self.deviceDetailsLastUpdate = None # str

        #Slot number

        self.slotNumber = None # str

        #State which is detected as happening over http instead of https

        self.certificateNeededState = None # str

        #PnP server ipv4 address used by pnp profile

        self.pnpProfileUsedAddr = None # str

        #PnP server hostname used by pnp profile

        self.pnpProfileUsedHost = None # str


        self.authStatus = None # DeviceAuthState


        self.deviceCertificate = None # str


        self.deviceType = None # str

        #Last state transition time of device

        self.lastStateTransitionTime = None # str


        self.stateDisplay = None # str


        self.versionCompatible = None # str

        self.cleanup = None # bool

        self.memberDetail = None # list[ZtdMemberDetail]

        #CLI execution EULA accepted or not
        self.eulaAccepted = None # bool

        #CLI execution license level
        self.licenseLevel = None # str

