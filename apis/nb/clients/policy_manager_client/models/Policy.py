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

class Policy(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'resource': 'PolicyResource',


            'id': 'str',


            'state': 'str',


            'policyScope': 'str',


            'instanceUuid': 'str',


            'policyName': 'str',


            'taskId': 'str',


            'actionProperty': 'ActionProperty',


            'scopeWirelessSegment': 'str',


            'policyPriority': 'int',


            'actions': 'list[str]',


            'networkUser': 'NetworkUser',


            'policyOwner': 'str'

        }

        self.attributeMap = {

            'resource': 'resource',

            'id': 'id',

            'state': 'state',

            'policyScope': 'policyScope',

            'instanceUuid': 'instanceUuid',

            'policyName': 'policyName',

            'taskId': 'taskId',

            'actionProperty': 'actionProperty',

            'scopeWirelessSegment': 'scopeWirelessSegment',

            'policyPriority': 'policyPriority',

            'actions': 'actions',

            'networkUser': 'networkUser',

            'policyOwner': 'policyOwner'

        }


        #Resource

        self.resource = None # PolicyResource

        #id

        self.id = None # str


        self.state = None # str

        #policyScope

        self.policyScope = None # str

        #

        self.instanceUuid = None # str

        #name of the policy

        self.policyName = None # str

        #Task ID

        self.taskId = None # str

        #ActionProperty

        self.actionProperty = None # ActionProperty


        self.scopeWirelessSegment = None # str

        #Policy Priority

        self.policyPriority = None # int

        #Action Set

        self.actions = None # list[str]

        #Network User

        self.networkUser = None # NetworkUser

        #Policy Owner

        self.policyOwner = None # str

