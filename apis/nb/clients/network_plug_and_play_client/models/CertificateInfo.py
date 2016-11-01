#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class CertificateInfo(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'keySize': 'int',


            'signature': 'str',


            'serialNumber': 'str',


            'issuerDN': 'str',


            'subjectDN': 'str',


            'keyType': 'str',


            'beginDate': 'str',


            'noAfterDate': 'str'

        }

        self.attributeMap = {

            'keySize': 'keySize',

            'signature': 'signature',

            'serialNumber': 'serialNumber',

            'issuerDN': 'issuerDN',

            'subjectDN': 'subjectDN',

            'keyType': 'keyType',

            'beginDate': 'beginDate',

            'noAfterDate': 'noAfterDate'

        }



        self.keySize = None # int


        self.signature = None # str


        self.serialNumber = None # str


        self.issuerDN = None # str


        self.subjectDN = None # str


        self.keyType = None # str


        self.beginDate = None # str


        self.noAfterDate = None # str

