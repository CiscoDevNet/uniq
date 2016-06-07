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

class PkiTrustPointConfig(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'id': 'str',


            'serialNumber': 'str',


            'platformId': 'str',


            'trustProfileName': 'str',


            'iosCli': 'list[str]',


            'iosSecureCli': 'list[str]',


            'pkcs12Url': 'str',


            'pkcs12Password': 'str',


            'provisionType': 'str',


            'sdnIp': 'str',


            'rsaKeySize': 'str',


            'fqdn': 'str',


            'enrollSubjectDN': 'str',


            'enrollPort': 'str',


            'enrollUrl': 'str',


            'enrollPassword': 'str',


            'caFingerprint': 'str',


            'enrollThreshold': 'str'

        }

        self.attributeMap = {

            'id': 'id',

            'serialNumber': 'serialNumber',

            'platformId': 'platformId',

            'trustProfileName': 'trustProfileName',

            'iosCli': 'iosCli',

            'iosSecureCli': 'iosSecureCli',

            'pkcs12Url': 'pkcs12Url',

            'pkcs12Password': 'pkcs12Password',

            'provisionType': 'provisionType',

            'sdnIp': 'sdnIp',

            'rsaKeySize': 'rsaKeySize',

            'fqdn': 'fqdn',

            'enrollSubjectDN': 'enrollSubjectDN',

            'enrollPort': 'enrollPort',

            'enrollUrl': 'enrollUrl',

            'enrollPassword': 'enrollPassword',

            'caFingerprint': 'caFingerprint',

            'enrollThreshold': 'enrollThreshold'

        }



        self.id = None # str


        self.serialNumber = None # str


        self.platformId = None # str


        self.trustProfileName = None # str


        self.iosCli = None # list[str]


        self.iosSecureCli = None # list[str]


        self.pkcs12Url = None # str


        self.pkcs12Password = None # str


        self.provisionType = None # str


        self.sdnIp = None # str


        self.rsaKeySize = None # str


        self.fqdn = None # str


        self.enrollSubjectDN = None # str


        self.enrollPort = None # str


        self.enrollUrl = None # str


        self.enrollPassword = None # str


        self.caFingerprint = None # str


        self.enrollThreshold = None # str

