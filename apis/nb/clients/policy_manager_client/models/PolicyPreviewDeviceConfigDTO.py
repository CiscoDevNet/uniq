#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PolicyPreviewDeviceConfigDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'status': 'str',
            
            
            'deviceId': 'str',
            
            
            'operationId': 'str',
            
            
            'failureReason': 'str',
            
            
            'fileId': 'str',
            
            
            'id': 'str',
            
            
            'createTime': 'int',
            
            
            'lastUpdateTime': 'int'
            
        }

        self.attributeMap = {
            
            'status': 'status',
            
            'deviceId': 'deviceId',
            
            'operationId': 'operationId',
            
            'failureReason': 'failureReason',
            
            'fileId': 'fileId',
            
            'id': 'id',
            
            'createTime': 'createTime',
            
            'lastUpdateTime': 'lastUpdateTime'
            
        }       

        
        #status
        
        self.status = None # str
        
        #network device id
        
        self.deviceId = None # str
        
        #operation id
        
        self.operationId = None # str
        
        #failure reason
        
        self.failureReason = None # str
        
        #file id
        
        self.fileId = None # str
        
        #id
        
        self.id = None # str
        
        #createTime
        
        self.createTime = None # int
        
        #lastUpdateTime
        
        self.lastUpdateTime = None # int
        
