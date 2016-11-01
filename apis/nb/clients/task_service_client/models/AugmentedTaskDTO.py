#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class AugmentedTaskDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'id': 'str',
            
            
            'progress': 'str',
            
            
            'version': 'int',
            
            
            'startTime': 'date-time',
            
            
            'endTime': 'date-time',
            
            
            'data': 'str',
            
            
            'errorCode': 'str',
            
            
            'serviceType': 'str',
            
            
            'username': 'str',
            
            
            'isError': 'bool',
            
            
            'lastUpdate': 'date-time',
            
            
            'operationIdList': 'list[str]',
            
            
            'parentId': 'str',
            
            
            'rootId': 'str',
            
            
            'failureReason': 'str'
            
        }

        self.attributeMap = {
            
            'id': 'id',
            
            'progress': 'progress',
            
            'version': 'version',
            
            'startTime': 'startTime',
            
            'endTime': 'endTime',
            
            'data': 'data',
            
            'errorCode': 'errorCode',
            
            'serviceType': 'serviceType',
            
            'username': 'username',
            
            'isError': 'isError',
            
            'lastUpdate': 'lastUpdate',
            
            'operationIdList': 'operationIdList',
            
            'parentId': 'parentId',
            
            'rootId': 'rootId',
            
            'failureReason': 'failureReason'
            
        }       

        
        #id
        
        self.id = None # str
        
        #progress
        
        self.progress = None # str
        
        #version
        
        self.version = None # int
        
        #startTime
        
        self.startTime = None # date-time
        
        #endTime
        
        self.endTime = None # date-time
        
        #data
        
        self.data = None # str
        
        #errorCode
        
        self.errorCode = None # str
        
        #serviceType
        
        self.serviceType = None # str
        
        #username
        
        self.username = None # str
        
        #isError
        
        self.isError = None # bool
        
        #lastUpdate
        
        self.lastUpdate = None # date-time
        
        
        self.operationIdList = None # list[str]
        
        #parentId
        
        self.parentId = None # str
        
        #rootId
        
        self.rootId = None # str
        
        #failureReason
        
        self.failureReason = None # str
        
