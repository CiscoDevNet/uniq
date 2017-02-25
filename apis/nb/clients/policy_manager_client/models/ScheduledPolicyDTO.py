#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ScheduledPolicyDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'policy': 'Policy',
            
            
            'scheduleTime': 'str',
            
            
            'scheduledWorkSpecificationId': 'str'
            
        }

        self.attributeMap = {
            
            'policy': 'policy',
            
            'scheduleTime': 'scheduleTime',
            
            'scheduledWorkSpecificationId': 'scheduledWorkSpecificationId'
            
        }       

        
        #policy
        
        self.policy = None # Policy
        
        #scheduleTime
        
        self.scheduleTime = None # str
        
        #scheduledWorkSpecificationId
        
        self.scheduledWorkSpecificationId = None # str
        
