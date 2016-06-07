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

class TopologyViewDto(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'id': 'str',


            'description': 'str',


            'topology': 'Topology',


            'applicationUuid': 'str',


            'pageUuid': 'str',


            'name': 'str'

        }

        self.attributeMap = {

            'id': 'id',

            'description': 'description',

            'topology': 'topology',

            'applicationUuid': 'applicationUuid',

            'pageUuid': 'pageUuid',

            'name': 'name'

        }


        #Unique Identifier for View

        self.id = None # str

        #View description

        self.description = None # str

        #Topology being represented by this view

        self.topology = None # Topology

        #Application unique identifier for this view

        self.applicationUuid = None # str

        #Page unique identifier for this view inside the corresponding application

        self.pageUuid = None # str

        #View name

        self.name = None # str

