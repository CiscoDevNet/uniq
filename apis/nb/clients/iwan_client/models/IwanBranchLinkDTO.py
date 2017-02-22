#!/usr/bin/env python
#pylint: skip-file

class IwanBranchLinkDTO(object):
    """ Class to host IWAN branch link information """


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """

        self.swaggerTypes = {
            'peAddress': 'str',
            'ceAddress': 'str',
            'interfaceName': 'str',
            'wanName': 'str',
            'bandwidth': 'int',
            'label': 'str',
            'downloadBW': 'int',
            'serviceProvider': 'str',
            'ipAddress': 'str',
            'type': 'str',
            'ceAddressSubnetMask': 'str',
        }

        self.attributeMap = {
            'peAddress': 'peAddress',
            'ceAddress': 'ceAddress',
            'interfaceName': 'interfaceName',
            'wanName': 'wanName',
            'bandwidth': 'bandwidth',
            'label': 'label',
            'downloadBW': 'downloadBW',
            'serviceProvider': 'serviceProvider',
            'ipAddress': 'ipAddress',
            'type': 'type',
            'ceAddressSubnetMask': 'ceAddressSubnetMask',
        }

        self.peAddress = None
        self.ceAddress = None
        self.interfaceName = None
        self.wanName = None
        self.bandwidth = None
        self.label = None
        self.downloadBW = None
        self.serviceProvider = None
        self.ipAddress = None
        self.type = None
        self.ceAddressSubnetMask = None
