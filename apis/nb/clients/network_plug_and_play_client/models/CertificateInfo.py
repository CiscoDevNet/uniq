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
            
            
            'serialNumber': 'str',
            
            
            'issuerDN': 'str',
            
            
            'subjectDN': 'str',
            
            
            'keyType': 'str',
            
            
            'noAfterDate': 'str',
            
            
            'beginDateISO8601': 'str',
            
            
            'noAfterDateISO8601': 'str',
            
            
            'beginDate': 'str',
            
            
            'signature': 'str'
            
        }

        self.attributeMap = {
            
            'keySize': 'keySize',
            
            'serialNumber': 'serialNumber',
            
            'issuerDN': 'issuerDN',
            
            'subjectDN': 'subjectDN',
            
            'keyType': 'keyType',
            
            'noAfterDate': 'noAfterDate',
            
            'beginDateISO8601': 'beginDateISO8601',
            
            'noAfterDateISO8601': 'noAfterDateISO8601',
            
            'beginDate': 'beginDate',
            
            'signature': 'signature'
            
        }       

        
        
        self.keySize = None # int
        
        
        self.serialNumber = None # str
        
        
        self.issuerDN = None # str
        
        
        self.subjectDN = None # str
        
        
        self.keyType = None # str
        
        
        self.noAfterDate = None # str
        
        
        self.beginDateISO8601 = None # str
        
        
        self.noAfterDateISO8601 = None # str
        
        
        self.beginDate = None # str
        
        
        self.signature = None # str
        
