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

class ActionProperty(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'relevanceLevel': 'str',


            'PrimaryPathPref': 'list[str]',


            'SecondaryPathPref': 'list[str]',


            'pathControlFlag': 'bool',


            'pathPreferenceFlag': 'bool',


            'TertiaryPathPref': 'list[str]',


            'PathOfLastResort': 'str',


            'priorityLevel': 'str',


            'experienceLevel': 'str',


            'destinations': 'list[str]',


            'pathPreference': 'str',


            'maintainExperience': 'str',


            'trustLevel': 'str'

        }

        self.attributeMap = {

            'relevanceLevel': 'relevanceLevel',

            'PrimaryPathPref': 'PrimaryPathPref',

            'SecondaryPathPref': 'SecondaryPathPref',

            'pathControlFlag': 'pathControlFlag',

            'pathPreferenceFlag': 'pathPreferenceFlag',

            'TertiaryPathPref': 'TertiaryPathPref',

            'PathOfLastResort': 'PathOfLastResort',

            'priorityLevel': 'priorityLevel',

            'experienceLevel': 'experienceLevel',

            'destinations': 'destinations',

            'pathPreference': 'pathPreference',

            'maintainExperience': 'maintainExperience',

            'trustLevel': 'trustLevel'

        }


        #relevance level for a policy

        self.relevanceLevel = None # str


        self.PrimaryPathPref = None # list[str]


        self.SecondaryPathPref = None # list[str]

        #path control flag

        self.pathControlFlag = None # bool

        #path preference flag

        self.pathPreferenceFlag = None # bool


        self.TertiaryPathPref = None # list[str]


        self.PathOfLastResort = None # str

        #priority level for a policy

        self.priorityLevel = None # str

        #experience level for a policy

        self.experienceLevel = None # str


        self.destinations = None # list[str]

        #path preference for a policy

        self.pathPreference = None # str


        self.maintainExperience = None # str

        #trust level for a policy

        self.trustLevel = None # str

