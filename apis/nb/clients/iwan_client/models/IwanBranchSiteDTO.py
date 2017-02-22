#!/usr/bin/env python
#pylint: skip-file

class IwanBranchSiteDTO(object):
    """ Class to provision IWAN branch site """


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """

        self.swaggerTypes = {
            'name': 'str',
            'location': 'str',
            'preferredPopName': 'str',
            'siteConfigurationType': 'str',
            'siteType': 'str',
            'apicSiteIdentifier': 'str',
            'devices': 'list[IwanBranchDevice]',
            'vlans': 'list[IwanVlan]'
        }

        self.attributeMap = {
            'name': 'name',
            'location': 'location',
            'preferredPopName': 'preferredPopName',
            'siteConfigurationType': 'siteConfigurationType',
            'siteType': 'siteType',
            'apicSiteIdentifier': 'apicSiteIdentifier',
            'devices': 'devices',
            'vlans': 'vlans'
        }

        self.name = None
        self.location = None
        self.preferredPopName = None
        self.siteConfigurationType = None
        self.siteType = None
        self.apicSiteIdentifier = None
        self.devices = None
        self.vlans = None
