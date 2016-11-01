#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class DetailedStatus(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'aclTraceCalculationFailureReason': 'str',
            
            
            'aclTraceCalculation': 'str'
            
        }

        self.attributeMap = {
            
            'aclTraceCalculationFailureReason': 'aclTraceCalculationFailureReason',
            
            'aclTraceCalculation': 'aclTraceCalculation'
            
        }       

        
        
        self.aclTraceCalculationFailureReason = None # str
        
        
        self.aclTraceCalculation = None # str
        
