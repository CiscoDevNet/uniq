#!/usr/bin/env python
#pylint: skip-file

class UnclaimedDevice(object):
    """ IWAN unclaimed device (with PnP completed) """


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """

        self.swaggerTypes = {
            'deviceId': 'str',
            'unclaimedDeviceId': 'str',
            'serialNumber': 'str',
            'platformType': 'str',
            'ipAddress': 'str',
            'hostName': 'str'
        }

        self.attributeMap = {
            'deviceId': 'deviceId',
            'unclaimedDeviceId': 'unclaimedDeviceId',
            'serialNumber': 'serialNumber',
            'platformType': 'platformType',
            'ipAddress': 'ipAddress',
            'hostName': 'hostName'
        }

        self.deviceId = None
        self.unclaimedDeviceId = None
        self.serialNumber = None
        self.platformType = None
        self.ipAddress = None
        self.hostName = None
