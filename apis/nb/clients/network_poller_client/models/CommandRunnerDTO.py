#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class CommandRunnerDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'name': 'str',
            
            
            'description': 'str',
            
            
            'timeout': 'int',
            
            
            'commands': 'list[str]',
            
            
            'deviceUuids': 'list[str]'
            
        }

        self.attributeMap = {
            
            'name': 'name',
            
            'description': 'description',
            
            'timeout': 'timeout',
            
            'commands': 'commands',
            
            'deviceUuids': 'deviceUuids'
            
        }       

        
        
        self.name = None # str
        
        
        self.description = None # str
        
        
        self.timeout = None # int
        
        #
        
        self.commands = None # list[str]
        
        #
        
        self.deviceUuids = None # list[str]
        
