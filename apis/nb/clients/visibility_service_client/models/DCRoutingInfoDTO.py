#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class DCRoutingInfoDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'dcPrefixDTOs': 'list[DCPrefixDTO]',
            
            
            'managementIps': 'list[str]',
            
            
            'asProtocolDTOs': 'list[ASProtocolDTO]'
            
        }

        self.attributeMap = {
            
            'dcPrefixDTOs': 'dcPrefixDTOs',
            
            'managementIps': 'managementIps',
            
            'asProtocolDTOs': 'asProtocolDTOs'
            
        }       

        
        
        self.dcPrefixDTOs = None # list[DCPrefixDTO]
        
        
        self.managementIps = None # list[str]
        
        
        self.asProtocolDTOs = None # list[ASProtocolDTO]
        
