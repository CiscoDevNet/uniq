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

class PolicyStatusDTO(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'status': 'str',


            'instanceUuid': 'str',


            'applicationPolicyCount': 'int',


            'policyScope': 'str',


            'scopeWirelessSegment': 'str',


            'networkDeviceId': 'str',


            'networkDeviceName': 'str',


            'failureReason': 'str',


            'lastUpdated': 'str',


            'outOfScope': 'bool',


            'businessRelevantApplications': 'list[PolicyApplication]',


            'businessIrrelevantApplications': 'list[PolicyApplication]',


            'networkDeviceIp': 'str'

        }

        self.attributeMap = {

            'status': 'status',

            'instanceUuid': 'instanceUuid',

            'applicationPolicyCount': 'applicationPolicyCount',

            'policyScope': 'policyScope',

            'scopeWirelessSegment': 'scopeWirelessSegment',

            'networkDeviceId': 'networkDeviceId',

            'networkDeviceName': 'networkDeviceName',

            'failureReason': 'failureReason',

            'lastUpdated': 'lastUpdated',

            'outOfScope': 'outOfScope',

            'businessRelevantApplications': 'businessRelevantApplications',

            'businessIrrelevantApplications': 'businessIrrelevantApplications',

            'networkDeviceIp': 'networkDeviceIp'

        }



        self.status = None # str


        self.instanceUuid = None # str


        self.applicationPolicyCount = None # int


        self.policyScope = None # str


        self.scopeWirelessSegment = None # str


        self.networkDeviceId = None # str


        self.networkDeviceName = None # str


        self.failureReason = None # str


        self.lastUpdated = None # str


        self.outOfScope = None # bool


        self.businessRelevantApplications = None # list[PolicyApplication]


        self.businessIrrelevantApplications = None # list[PolicyApplication]


        self.networkDeviceIp = None # str

