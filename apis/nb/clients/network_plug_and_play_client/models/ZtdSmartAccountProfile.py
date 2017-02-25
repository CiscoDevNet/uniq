#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ZtdSmartAccountProfile(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'description': 'str',
            
            
            'id': 'str',
            
            
            'userId': 'str',
            
            
            'controllerAttributes': 'ZtdSmartAccountControllerAttribute',
            
            
            'profileName': 'str',
            
            
            'makeDefault': 'bool',
            
            
            'attributeInfo': 'dict'
            
        }

        self.attributeMap = {
            
            'description': 'description',
            
            'id': 'id',
            
            'userId': 'userId',
            
            'controllerAttributes': 'controllerAttributes',
            
            'profileName': 'profileName',
            
            'makeDefault': 'makeDefault',
            
            'attributeInfo': 'attributeInfo'
            
        }       

        
        
        self.description = None # str
        
        #profile ID
        
        self.id = None # str
        
        #user ID
        
        self.userId = None # str
        
        
        self.controllerAttributes = None # ZtdSmartAccountControllerAttribute
        
        #Default profile name is PNP-DEFAULT-APICEM
        
        self.profileName = None # str
        
        #Register profile as default profile
        
        self.makeDefault = None # bool
        
        
        self.attributeInfo = None # dict
        
