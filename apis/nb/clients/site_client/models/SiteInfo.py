#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.

class SiteInfo(object):
    """ Class to hold IWAN site status information """


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """

        self.swaggerTypes = {
            'id': 'str',
            'siteId': 'str',
            'name': 'str',
            'description': 'str',
            'location': 'str',
            'properties': 'SiteProperties',
            'deviceCount': 'int'
        }

        self.attributeMap = {
            'id': 'id',
            'siteId': 'siteId',
            'name': 'name',
            'description': 'description',
            'location': 'location',
            'properties': 'properties',
            'deviceCount': 'deviceCount'
        }

        self.id = None
        self.siteId = None
        self.name = None
        self.description = None
        self.location = None
        self.properties = None
        self.deviceCount = None
