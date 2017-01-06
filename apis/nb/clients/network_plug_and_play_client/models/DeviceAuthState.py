#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class DeviceAuthState(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'timestamp': 'int',
            
            
            'status': 'str',
            
            
            'errorMessage': 'str',
            
            
            'certInfo': 'CertificateInfo',
            
            
            'type': 'str'
            
        }

        self.attributeMap = {
            
            'timestamp': 'timestamp',
            
            'status': 'status',
            
            'errorMessage': 'errorMessage',
            
            'certInfo': 'certInfo',
            
            'type': 'type'
            
        }       

        
        
        self.timestamp = None # int
        
        
        self.status = None # str
        
        
        self.errorMessage = None # str
        
        
        self.certInfo = None # CertificateInfo
        
        
        self.type = None # str
        
