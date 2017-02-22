#!/usr/bin/env python
#pylint: skip-file

class IwanBranchDeviceDTO(object):
    """ Class to host IWAN branch site information """


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """

        self.swaggerTypes = {
            'unclaimedDeviceId': 'str',
            'deviceType': 'str',
            'serialNumber': 'str',
            'platformType': 'str',
            'ipAddress': 'str',
            'hostname': 'str',
            'links': 'list[IwanBranchLinkDTO]'
        }

        self.attributeMap = {
            'unclaimedDeviceId': 'unclaimedDeviceId',
            'deviceType': 'deviceType',
            'serialNumber': 'serialNumber',
            'platformType': 'platformType',
            'ipAddress': 'ipAddress',
            'hostname': 'hostname',
            'links': 'links'
        }

        self.unclaimedDeviceId = None
        self.deviceType = None
        self.serialNumber = None
        self.platformType = None
        self.ipAddress = None
        self.hostname = None
        self.links = None
