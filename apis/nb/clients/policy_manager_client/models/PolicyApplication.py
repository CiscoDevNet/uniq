#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PolicyApplication(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'raw': 'str',
            
            
            'trafficClass': 'str',
            
            
            'stale': 'bool',
            
            
            'id': 'str',
            
            
            'appName': 'str'
            
        }

        self.attributeMap = {
            
            'raw': 'raw',
            
            'trafficClass': 'trafficClass',
            
            'stale': 'stale',
            
            'id': 'id',
            
            'appName': 'appName'
            
        }       

        
        #Either raw Application of the form port:protocol should be specified or appId should be specified
        
        self.raw = None # str
        
        #Traffic class to which the app belongs
        
        self.trafficClass = None # str
        
        #Indicates whether the application has been updated since the last time this policy was provisioned
        
        self.stale = None # bool
        
        #id
        
        self.id = None # str
        
        
        self.appName = None # str
        
