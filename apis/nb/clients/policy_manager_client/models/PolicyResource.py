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

class PolicyResource(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'categories': 'list[CategoryDTO]',


            'applications': 'list[PolicyApplication]',


            'userIdentifiers': 'list[str]',


            'deviceTypes': 'list[str]',


            'locations': 'list[str]',


            'applicationDiffs': 'list[PolicyApplicationDiffDTO]'

        }

        self.attributeMap = {

            'categories': 'categories',

            'applications': 'applications',

            'userIdentifiers': 'userIdentifiers',

            'deviceTypes': 'deviceTypes',

            'locations': 'locations',

            'applicationDiffs': 'applicationDiffs'

        }



        self.categories = None # list[CategoryDTO]


        self.applications = None # list[PolicyApplication]


        self.userIdentifiers = None # list[str]


        self.deviceTypes = None # list[str]


        self.locations = None # list[str]


        self.applicationDiffs = None # list[PolicyApplicationDiffDTO]

