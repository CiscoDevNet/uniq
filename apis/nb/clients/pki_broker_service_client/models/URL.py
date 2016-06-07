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

class URL(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'path': 'str',


            'authority': 'str',


            'query': 'str',


            'protocol': 'str',


            'file': 'str',


            'host': 'str',


            'ref': 'str',


            'userInfo': 'str',


            'port': 'int',


            'defaultPort': 'int',


            'content': 'object'

        }

        self.attributeMap = {

            'path': 'path',

            'authority': 'authority',

            'query': 'query',

            'protocol': 'protocol',

            'file': 'file',

            'host': 'host',

            'ref': 'ref',

            'userInfo': 'userInfo',

            'port': 'port',

            'defaultPort': 'defaultPort',

            'content': 'content'

        }



        self.path = None # str


        self.authority = None # str


        self.query = None # str


        self.protocol = None # str


        self.file = None # str


        self.host = None # str


        self.ref = None # str


        self.userInfo = None # str


        self.port = None # int


        self.defaultPort = None # int


        self.content = None # object

