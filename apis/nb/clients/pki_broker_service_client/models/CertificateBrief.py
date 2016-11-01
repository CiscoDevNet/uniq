#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class CertificateBrief(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'commonName': 'str',
            
            
            'issuer': 'str',
            
            
            'serialNumber': 'str',
            
            
            'gvSerialId': 'str',
            
            
            'selfSigned': 'str',
            
            
            'proxyEnabled': 'str',
            
            
            'expiry': 'str',
            
            
            'attributeInfo': 'dict',
            
            
            'id': 'str'
            
        }

        self.attributeMap = {
            
            'commonName': 'commonName',
            
            'issuer': 'issuer',
            
            'serialNumber': 'serialNumber',
            
            'gvSerialId': 'gvSerialId',
            
            'selfSigned': 'selfSigned',
            
            'proxyEnabled': 'proxyEnabled',
            
            'expiry': 'expiry',
            
            'attributeInfo': 'attributeInfo',
            
            'id': 'id'
            
        }       

        
        #Certificate common name
        
        self.commonName = None # str
        
        #Certificate issuer
        
        self.issuer = None # str
        
        #Certificate serial-number
        
        self.serialNumber = None # str
        
        #Grapevine certificate serial identification
        
        self.gvSerialId = None # str
        
        #Set if this is a self-signed certificate
        
        self.selfSigned = None # str
        
        #Set if this is a proxy certificate
        
        self.proxyEnabled = None # str
        
        #Certificate expiry
        
        self.expiry = None # str
        
        
        self.attributeInfo = None # dict
        
        
        self.id = None # str
        
