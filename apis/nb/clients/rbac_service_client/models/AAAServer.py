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

class AAAServer(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'protocol': 'str',


            'authenticationPort': 'int',


            'accountingPort': 'int',


            'retries': 'int',


            'socketTimeout': 'int',


            'serverId': 'UUID',


            'serverIp': 'str',


            'sharedSecret': 'str'

        }

        self.attributeMap = {

            'protocol': 'protocol',

            'authenticationPort': 'authenticationPort',

            'accountingPort': 'accountingPort',

            'retries': 'retries',

            'socketTimeout': 'socketTimeout',

            'serverId': 'serverId',

            'serverIp': 'serverIp',

            'sharedSecret': 'sharedSecret'

        }


        #Protocol

        self.protocol = None # str

        #Authentication Port

        self.authenticationPort = None # int

        #Accounting Port

        self.accountingPort = None # int

        #Retries

        self.retries = None # int

        #Socket Timeout

        self.socketTimeout = None # int

        #Server Id

        self.serverId = None # UUID

        #Server IP Address

        self.serverIp = None # str

        #Shared Secret

        self.sharedSecret = None # str

