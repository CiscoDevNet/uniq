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

class SiteManagementInfo(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'description': 'str',


            'deviceIds': 'list[str]',


            'name': 'str',


            'location': 'str',


            'properties': 'object',


            'id': 'str'

        }

        self.attributeMap = {

            'description': 'description',

            'deviceIds': 'deviceIds',

            'name': 'name',

            'location': 'location',

            'properties': 'properties',

            'id': 'id'

        }


        #Description of site

        self.description = None # str

        #Unique identifier of devices that are associated with site

        self.deviceIds = None # list[str]

        #Name of site

        self.name = None # str

        #Location of site

        self.location = None # str

        #Properties of site

        self.properties = None # object

        #Unique identifier of site

        self.id = None # str

