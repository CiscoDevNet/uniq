#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PolicyPreviewDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'deviceConfigs': 'list[PolicyPreviewDeviceConfigDTO]',
            
            
            'state': 'str',
            
            
            'networkDeviceIds': 'list[str]',
            
            
            'policies': 'list[Policy]',
            
            
            'id': 'str',
            
            
            'createTime': 'int',
            
            
            'lastUpdateTime': 'int'
            
        }

        self.attributeMap = {
            
            'deviceConfigs': 'deviceConfigs',
            
            'state': 'state',
            
            'networkDeviceIds': 'networkDeviceIds',
            
            'policies': 'policies',
            
            'id': 'id',
            
            'createTime': 'createTime',
            
            'lastUpdateTime': 'lastUpdateTime'
            
        }       

        
        #list of preview device configs
        
        self.deviceConfigs = None # list[PolicyPreviewDeviceConfigDTO]
        
        #one of {DISABLE, ENABLE_DEVICE}
        
        self.state = None # str
        
        #list of network device ids, required when state is ENABLE_DEVICE
        
        self.networkDeviceIds = None # list[str]
        
        #list of policies
        
        self.policies = None # list[Policy]
        
        #id
        
        self.id = None # str
        
        #createTime
        
        self.createTime = None # int
        
        #lastUpdateTime
        
        self.lastUpdateTime = None # int
        
