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
            
            
            'policies': 'list[Policy]',
            
            
            'state': 'str',
            
            
            'networkDeviceIds': 'list[str]',
            
            
            'id': 'str',
            
            
            'lastUpdateTime': 'int',
            
            
            'createTime': 'int'
            
        }

        self.attributeMap = {
            
            'deviceConfigs': 'deviceConfigs',
            
            'policies': 'policies',
            
            'state': 'state',
            
            'networkDeviceIds': 'networkDeviceIds',
            
            'id': 'id',
            
            'lastUpdateTime': 'lastUpdateTime',
            
            'createTime': 'createTime'
            
        }       

        
        #list of preview device configs
        
        self.deviceConfigs = None # list[PolicyPreviewDeviceConfigDTO]
        
        #list of policies
        
        self.policies = None # list[Policy]
        
        #one of {DISABLE, ENABLE_DEVICE}
        
        self.state = None # str
        
        #list of network device ids, required when state is ENABLE_DEVICE
        
        self.networkDeviceIds = None # list[str]
        
        #id
        
        self.id = None # str
        
        #lastUpdateTime
        
        self.lastUpdateTime = None # int
        
        #createTime
        
        self.createTime = None # int
        
