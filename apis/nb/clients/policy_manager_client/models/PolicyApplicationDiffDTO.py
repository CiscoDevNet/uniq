#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PolicyApplicationDiffDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'policyApplication': 'PolicyApplication',
            
            
            'operation': 'str'
            
        }

        self.attributeMap = {
            
            'policyApplication': 'policyApplication',
            
            'operation': 'operation'
            
        }       

        
        #application
        
        self.policyApplication = None # PolicyApplication
        
        #operation
        
        self.operation = None # str
        
