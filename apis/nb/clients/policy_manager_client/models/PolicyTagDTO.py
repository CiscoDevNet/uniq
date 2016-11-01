#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PolicyTagDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'policyTag': 'str'
            
        }

        self.attributeMap = {
            
            'policyTag': 'policyTag'
            
        }       

        
        #Policy Tag value
        
        self.policyTag = None # str
        
