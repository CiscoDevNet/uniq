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

class ZtdBulkStatus(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'format': 'str',


            'type': 'str',


            'date': 'date-time',


            'status': 'str',


            'username': 'str',


            'report': 'str',


            'siteAdded': 'int',


            'siteFailed': 'int',


            'siteSkipped': 'int',


            'deviceAdded': 'int',


            'deviceFailed': 'int',


            'deviceSkipped': 'int',


            'requestFilename': 'str',


            'taskId': 'str'

        }

        self.attributeMap = {

            'format': 'format',

            'type': 'type',

            'date': 'date',

            'status': 'status',

            'username': 'username',

            'report': 'report',

            'siteAdded': 'siteAdded',

            'siteFailed': 'siteFailed',

            'siteSkipped': 'siteSkipped',

            'deviceAdded': 'deviceAdded',

            'deviceFailed': 'deviceFailed',

            'deviceSkipped': 'deviceSkipped',

            'requestFilename': 'requestFilename',

            'taskId': 'taskId'

        }



        self.format = None # str


        self.type = None # str


        self.date = None # date-time


        self.status = None # str


        self.username = None # str


        self.report = None # str


        self.siteAdded = None # int


        self.siteFailed = None # int


        self.siteSkipped = None # int


        self.deviceAdded = None # int


        self.deviceFailed = None # int


        self.deviceSkipped = None # int


        self.requestFilename = None # str


        self.taskId = None # str

