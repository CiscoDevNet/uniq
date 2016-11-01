#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class DCPrefixDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'siteId': 'str',
            
            
            'dataCenterNetworkIp': 'str',
            
            
            'dataCenterNetworkLength': 'str',
            
            
            'id': 'str'
            
        }

        self.attributeMap = {
            
            'siteId': 'siteId',
            
            'dataCenterNetworkIp': 'dataCenterNetworkIp',
            
            'dataCenterNetworkLength': 'dataCenterNetworkLength',
            
            'id': 'id'
            
        }       

        
        
        self.siteId = None # str
        
        
        self.dataCenterNetworkIp = None # str
        
        
        self.dataCenterNetworkLength = None # str
        
        
        self.id = None # str
        
