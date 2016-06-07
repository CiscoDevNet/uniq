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

class CertificateBrief(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'issuer': 'str',


            'commonName': 'str',


            'serialNumber': 'str',


            'proxyEnabled': 'str',


            'selfSigned': 'str',


            'gvSerialId': 'str',


            'expiry': 'str',


            'filePath': 'str',


            'lastCertFilePath': 'str',


            'attributeInfo': 'object',


            'id': 'str'

        }

        self.attributeMap = {

            'issuer': 'issuer',

            'commonName': 'commonName',

            'serialNumber': 'serialNumber',

            'proxyEnabled': 'proxyEnabled',

            'selfSigned': 'selfSigned',

            'gvSerialId': 'gvSerialId',

            'expiry': 'expiry',

            'filePath': 'filePath',

            'lastCertFilePath': 'lastCertFilePath',

            'attributeInfo': 'attributeInfo',

            'id': 'id'

        }



        self.issuer = None # str


        self.commonName = None # str


        self.serialNumber = None # str


        self.proxyEnabled = None # str


        self.selfSigned = None # str


        self.gvSerialId = None # str


        self.expiry = None # str


        self.filePath = None # str


        self.lastCertFilePath = None # str


        self.attributeInfo = None # object


        self.id = None # str

