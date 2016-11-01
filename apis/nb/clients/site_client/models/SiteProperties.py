#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.

class SiteProperties(object):
    """ Class to hold IWAN site properties information """


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """

        self.swaggerTypes = {
            'iwan_site_type': 'str',
            'iwan_site_provisioned': 'bool',
            'status': 'str',
            'iwan_status_timestamp': 'str',
            'status_detail': 'str',
            'numberOfIntendedDevice': 'str',
        }

        self.attributeMap = {
            'iwan_site_type': 'iwan_site_type',
            'iwan_site_provisioned': 'iwan_site_provisioned',
            'status': 'status',
            'iwan_status_timestamp': 'iwan_status_timestamp',
            'status_detail': 'status_detail',
            'numberOfIntendedDevice': 'numberOfIntendedDevice',
        }

        self.iwan_site_type = None
        self.iwan_site_provisioned = None
        self.status = None
        self.iwan_status_timestamp = None
        self.status_detail = None
        self.numberOfIntendedDevice = None
