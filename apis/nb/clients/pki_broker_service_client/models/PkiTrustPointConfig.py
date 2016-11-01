#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


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
            
            
            'rsaKeySize': 'str',
            
            
            'fqdn': 'str',
            
            
            'enrollSubjectDN': 'str',
            
            
            'enrollPort': 'str',
            
            
            'enrollUrl': 'str',
            
            
            'enrollPassword': 'str',
            
            
            'caFingerprint': 'str',
            
            
            'enrollThreshold': 'str',
            
            
            'iosSecureCli': 'list[str]',
            
            
            'pkcs12Url': 'str',
            
            
            'pkcs12Password': 'str',
            
            
            'provisionType': 'str',
            
            
            'sdnIp': 'str'
            
        }

        self.attributeMap = {
            
            'id': 'id',
            
            'serialNumber': 'serialNumber',
            
            'platformId': 'platformId',
            
            'trustProfileName': 'trustProfileName',
            
            'iosCli': 'iosCli',
            
            'rsaKeySize': 'rsaKeySize',
            
            'fqdn': 'fqdn',
            
            'enrollSubjectDN': 'enrollSubjectDN',
            
            'enrollPort': 'enrollPort',
            
            'enrollUrl': 'enrollUrl',
            
            'enrollPassword': 'enrollPassword',
            
            'caFingerprint': 'caFingerprint',
            
            'enrollThreshold': 'enrollThreshold',
            
            'iosSecureCli': 'iosSecureCli',
            
            'pkcs12Url': 'pkcs12Url',
            
            'pkcs12Password': 'pkcs12Password',
            
            'provisionType': 'provisionType',
            
            'sdnIp': 'sdnIp'
            
        }       

        
        
        self.id = None # str
        
        
        self.serialNumber = None # str
        
        
        self.platformId = None # str
        
        
        self.trustProfileName = None # str
        
        
        self.iosCli = None # list[str]
        
        
        self.rsaKeySize = None # str
        
        
        self.fqdn = None # str
        
        
        self.enrollSubjectDN = None # str
        
        
        self.enrollPort = None # str
        
        
        self.enrollUrl = None # str
        
        
        self.enrollPassword = None # str
        
        
        self.caFingerprint = None # str
        
        
        self.enrollThreshold = None # str
        
        
        self.iosSecureCli = None # list[str]
        
        
        self.pkcs12Url = None # str
        
        
        self.pkcs12Password = None # str
        
        
        self.provisionType = None # str
        
        
        self.sdnIp = None # str
        
