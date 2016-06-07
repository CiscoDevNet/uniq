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

class PathResponse(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'request': 'FlowAnalysis',


            'networkElements': 'list[NetworkElement]',


            'lastUpdate': 'str',


            'networkElementsInfo': 'list[NetworkElementInfo]',


            'detailedStatus': 'DetailedStatus',


            'properties': 'list[str]'

        }

        self.attributeMap = {

            'request': 'request',

            'networkElements': 'networkElements',

            'lastUpdate': 'lastUpdate',

            'networkElementsInfo': 'networkElementsInfo',

            'detailedStatus': 'detailedStatus',

            'properties': 'properties'

        }


        #Describes the source and destination for a path trace

        self.request = None # FlowAnalysis


        self.networkElements = None # list[NetworkElement]

        #Last updated time

        self.lastUpdate = None # str

        #Nodes travesed along a path, including source and destination

        self.networkElementsInfo = None # list[NetworkElementInfo]

        #Detailed Status of the calculation of Path Trace with its inclusions

        self.detailedStatus = None # DetailedStatus

        #Properties for path trace

        self.properties = None # list[str]

