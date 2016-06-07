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

class ScheduleInfoOutput(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'startTime': 'date-time',


            'endTime': 'date-time',


            'description': 'str',


            'origin': 'str',


            'operation': 'str',


            'groupName': 'str',


            'prevTime': 'date-time',


            'taskId': 'str',


            'nextTime': 'date-time',


            'scheduledWorkSpecId': 'str'

        }

        self.attributeMap = {

            'startTime': 'startTime',

            'endTime': 'endTime',

            'description': 'description',

            'origin': 'origin',

            'operation': 'operation',

            'groupName': 'groupName',

            'prevTime': 'prevTime',

            'taskId': 'taskId',

            'nextTime': 'nextTime',

            'scheduledWorkSpecId': 'scheduledWorkSpecId'

        }



        self.startTime = None # date-time


        self.endTime = None # date-time


        self.description = None # str


        self.origin = None # str


        self.operation = None # str


        self.groupName = None # str


        self.prevTime = None # date-time


        self.taskId = None # str


        self.nextTime = None # date-time


        self.scheduledWorkSpecId = None # str

