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

class LongQuantity(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'longAmount': 'int',


            'units': 'str',


            'instanceId': 'int',


            'instanceUuid': 'str',


            'instanceVersion': 'int'

        }

        self.attributeMap = {

            'longAmount': 'longAmount',

            'units': 'units',

            'instanceId': 'instanceId',

            'instanceUuid': 'instanceUuid',

            'instanceVersion': 'instanceVersion'

        }



        self.longAmount = None # int


        self.units = None # str


        self.instanceId = None # int


        self.instanceUuid = None # str


        self.instanceVersion = None # int

