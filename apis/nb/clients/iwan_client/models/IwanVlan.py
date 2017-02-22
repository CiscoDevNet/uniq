#!/usr/bin/env python
#pylint: skip-file

class IwanVlan(object):
    """ Class to hold IWAN branch VLAN information """


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """

        self.swaggerTypes = {
            'vlanType': 'str',
            'vlanId': 'int',
            'numberOfIPs': 'int',
            'dhcpIp': 'str',
            'dhcpEnabled': 'bool'
        }

        self.attributeMap = {
            'vlanType': 'vlanType',
            'vlanId': 'vlanId',
            'numberOfIPs': 'numberOfIPs',
            'dhcpIp': 'dhcpIp',
            'dhcpEnabled': 'dhcpEnabled'
        }

        self.vlanType = None
        self.vlanId = None
        self.numberOfIPs = None
        self.dhcpIp = None
        self.dhcpEnabled = None
