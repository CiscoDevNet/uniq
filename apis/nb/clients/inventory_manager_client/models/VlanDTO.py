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

class VlanDTO(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'mask': 'int',


            'prefix': 'str',


            'vlanType': 'str',


            'vlanNumber': 'int',


            'interfaceName': 'str',


            'numberOfIPs': 'int',


            'ipAddress': 'str',


            'networkAddress': 'str'

        }

        self.attributeMap = {

            'mask': 'mask',

            'prefix': 'prefix',

            'vlanType': 'vlanType',

            'vlanNumber': 'vlanNumber',

            'interfaceName': 'interfaceName',

            'numberOfIPs': 'numberOfIPs',

            'ipAddress': 'ipAddress',

            'networkAddress': 'networkAddress'

        }



        self.mask = None # int


        self.prefix = None # str


        self.vlanType = None # str


        self.vlanNumber = None # int


        self.interfaceName = None # str


        self.numberOfIPs = None # int


        self.ipAddress = None # str


        self.networkAddress = None # str

