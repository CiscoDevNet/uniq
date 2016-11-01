#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ContractListResult(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'version': 'str',
            
            
            'response': 'list[ContractDTO]'
            
        }

        self.attributeMap = {
            
            'version': 'version',
            
            'response': 'response'
            
        }       

        
        
        self.version = None # str
        
        
        self.response = None # list[ContractDTO]
        
