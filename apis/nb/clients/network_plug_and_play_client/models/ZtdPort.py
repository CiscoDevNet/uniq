#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ZtdPort(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'status': 'str',
            
            
            'neighborRank': 'str'
            
        }

        self.attributeMap = {
            
            'status': 'status',
            
            'neighborRank': 'neighborRank'
            
        }       

        
        
        self.status = None # str
        
        
        self.neighborRank = None # str
        
