#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class VersionNumberDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'policyChanged': 'bool',
            
            
            'version': 'int',
            
            
            'createTime': 'int'
            
        }

        self.attributeMap = {
            
            'policyChanged': 'policyChanged',
            
            'version': 'version',
            
            'createTime': 'createTime'
            
        }       

        
        #true if the version was created as a result of put/post/delete on the policy
        
        self.policyChanged = None # bool
        
        #version number
        
        self.version = None # int
        
        #time at which the version was created
        
        self.createTime = None # int
        
