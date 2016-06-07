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

class AugmentedTaskDTO(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'id': 'str',


            'startTime': 'date-time',


            'endTime': 'date-time',


            'progress': 'str',


            'errorCode': 'str',


            'data': 'str',


            'version': 'int',


            'serviceType': 'str',


            'username': 'str',


            'parentId': 'str',


            'rootId': 'str',


            'operationIdList': 'list[str]',


            'lastUpdate': 'date-time',


            'failureReason': 'str',


            'isError': 'bool'

        }

        self.attributeMap = {

            'id': 'id',

            'startTime': 'startTime',

            'endTime': 'endTime',

            'progress': 'progress',

            'errorCode': 'errorCode',

            'data': 'data',

            'version': 'version',

            'serviceType': 'serviceType',

            'username': 'username',

            'parentId': 'parentId',

            'rootId': 'rootId',

            'operationIdList': 'operationIdList',

            'lastUpdate': 'lastUpdate',

            'failureReason': 'failureReason',

            'isError': 'isError'

        }


        #id

        self.id = None # str

        #startTime

        self.startTime = None # date-time

        #endTime

        self.endTime = None # date-time

        #progress

        self.progress = None # str

        #errorCode

        self.errorCode = None # str

        #data

        self.data = None # str

        #version

        self.version = None # int

        #serviceType

        self.serviceType = None # str

        #username

        self.username = None # str

        #parentId

        self.parentId = None # str

        #rootId

        self.rootId = None # str


        self.operationIdList = None # list[str]

        #lastUpdate

        self.lastUpdate = None # date-time

        #failureReason

        self.failureReason = None # str

        #isError

        self.isError = None # bool

