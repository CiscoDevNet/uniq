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

class CiscoIseDTO(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'username': 'str',


            'id': 'str',


            'password': 'str',


            'description': 'str',


            'ipAddress': 'str',


            'subscriberName': 'str',


            'keystoreFileId': 'str',


            'keystoreFilePassPhrase': 'str',


            'truststoreFileId': 'str',


            'truststoreFilePassPhrase': 'str',


            'serverState': 'str'

        }

        self.attributeMap = {

            'username': 'username',

            'id': 'id',

            'password': 'password',

            'description': 'description',

            'ipAddress': 'ipAddress',

            'subscriberName': 'subscriberName',

            'keystoreFileId': 'keystoreFileId',

            'keystoreFilePassPhrase': 'keystoreFilePassPhrase',

            'truststoreFileId': 'truststoreFileId',

            'truststoreFilePassPhrase': 'truststoreFilePassPhrase',

            'serverState': 'serverState'

        }


        #username

        self.username = None # str

        #id

        self.id = None # str

        #password

        self.password = None # str

        #description

        self.description = None # str

        #ipAddress

        self.ipAddress = None # str

        #subscriberName

        self.subscriberName = None # str

        #keystoreFileId

        self.keystoreFileId = None # str

        #keystoreFilePassPhrase

        self.keystoreFilePassPhrase = None # str

        #truststoreFileId

        self.truststoreFileId = None # str

        #truststoreFilePassPhrase

        self.truststoreFilePassPhrase = None # str

        #serverState

        self.serverState = None # str

