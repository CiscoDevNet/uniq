#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class VersionDiffDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'policies': 'list[PolicyDiffDTO]',
            
            
            'id': 'str'
            
        }

        self.attributeMap = {
            
            'policies': 'policies',
            
            'id': 'id'
            
        }       

        
        #Policies from the cached diff. This attribute enables the user to make changes to the diffs that he can post for rollback.
        
        self.policies = None # list[PolicyDiffDTO]
        
        #Id of the cached diff. Use id in the post api if you don&#39;t want to make any modifications to the diff corresponding to the diff id.
        
        self.id = None # str
        
