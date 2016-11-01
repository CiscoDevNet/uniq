#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class AAAServer(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'sharedSecret': 'str',


            'serverIp': 'str',


            'authenticationPort': 'int',


            'accountingPort': 'int',


            'retries': 'int',


            'socketTimeout': 'int',


            #changed this manually from UUID to str
            'serverId': 'str',


            'protocol': 'str'

        }

        self.attributeMap = {

            'sharedSecret': 'sharedSecret',

            'serverIp': 'serverIp',

            'authenticationPort': 'authenticationPort',

            'accountingPort': 'accountingPort',

            'retries': 'retries',

            'socketTimeout': 'socketTimeout',

            'serverId': 'serverId',

            'protocol': 'protocol'

        }


        #Shared Secret

        self.sharedSecret = None # str

        #Server IP Address

        self.serverIp = None # str

        #Authentication Port

        self.authenticationPort = None # int

        #Accounting Port

        self.accountingPort = None # int

        #Retries

        self.retries = None # int

        #Socket Timeout

        self.socketTimeout = None # int

        #Server Id
        #changed this manually from UUID to str
        self.serverId = None # str

        #Protocol

        self.protocol = None # str

