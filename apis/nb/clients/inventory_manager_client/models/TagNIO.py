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

class TagNIO(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'id': 'str',


            'linkId': 'str',


            'lastUpdated': 'str',


            'networkDeviceId': 'str',


            'interfaceId': 'str',


            'locationId': 'str',


            'tag': 'str'

        }

        self.attributeMap = {

            'id': 'id',

            'linkId': 'linkId',

            'lastUpdated': 'lastUpdated',

            'networkDeviceId': 'networkDeviceId',

            'interfaceId': 'interfaceId',

            'locationId': 'locationId',

            'tag': 'tag'

        }


        #Unique identifier of tag

        self.id = None # str

        #Unique identifier of link

        self.linkId = None # str

        #Time when the device interface info last got updated

        self.lastUpdated = None # str

        #Unique identifier of device

        self.networkDeviceId = None # str

        #Unique identifier of the interface

        self.interfaceId = None # str

        #Unique identifier of location

        self.locationId = None # str

        #Tag Id

        self.tag = None # str

