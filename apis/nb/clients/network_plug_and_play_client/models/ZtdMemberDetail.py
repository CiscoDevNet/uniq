#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ZtdMemberDetail(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'serialNumber': 'str',


            'rank': 'int',


            'role': 'str',


            'macAddress': 'str',


            'hardwareVersion': 'str',


            'imageVersion': 'str',


            'priority': 'int',


            'state': 'str',


            'attributeInfo': 'object',


            'id': 'str'

        }

        self.attributeMap = {

            'serialNumber': 'serialNumber',

            'rank': 'rank',

            'role': 'role',

            'macAddress': 'macAddress',

            'hardwareVersion': 'hardwareVersion',

            'imageVersion': 'imageVersion',

            'priority': 'priority',

            'state': 'state',

            'attributeInfo': 'attributeInfo',

            'id': 'id'

        }



        self.serialNumber = None # str


        self.rank = None # int


        self.role = None # str


        self.macAddress = None # str


        self.hardwareVersion = None # str


        self.imageVersion = None # str


        self.priority = None # int


        self.state = None # str


        self.attributeInfo = None # object


        self.id = None # str

