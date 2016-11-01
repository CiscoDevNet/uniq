#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PkiTrustPoint(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'entityName': 'str',
            
            
            'serialNumber': 'str',
            
            
            'id': 'str',
            
            
            'platformId': 'str',
            
            
            'trustProfileName': 'str',
            
            
            'entityType': 'str',
            
            
            'networkDeviceId': 'str',
            
            
            'certificateAuthorityId': 'str',
            
            
            'controllerIpAddress': 'str',
            
            
            'attributeInfo': 'dict'
            
        }

        self.attributeMap = {
            
            'entityName': 'entityName',
            
            'serialNumber': 'serialNumber',
            
            'id': 'id',
            
            'platformId': 'platformId',
            
            'trustProfileName': 'trustProfileName',
            
            'entityType': 'entityType',
            
            'networkDeviceId': 'networkDeviceId',
            
            'certificateAuthorityId': 'certificateAuthorityId',
            
            'controllerIpAddress': 'controllerIpAddress',
            
            'attributeInfo': 'attributeInfo'
            
        }       

        
        #Devices hostname
        
        self.entityName = None # str
        
        #Devices serial-number
        
        self.serialNumber = None # str
        
        #Trust-point identification. Automatically generated
        
        self.id = None # str
        
        #Platform identification. Eg. ASR1006
        
        self.platformId = None # str
        
        #Name of trust-profile (must already exist). Default: sdn-network-infra-iwan
        
        self.trustProfileName = None # str
        
        #Available options: router, switch. Currently not used
        
        self.entityType = None # str
        
        #Device identification. Currently not used
        
        self.networkDeviceId = None # str
        
        #CA identification. Automatically populated
        
        self.certificateAuthorityId = None # str
        
        #IP address device uses to connect to APIC-EM. Eg. Proxy server IP address. Automatically populated if not set
        
        self.controllerIpAddress = None # str
        
        
        self.attributeInfo = None # dict
        
