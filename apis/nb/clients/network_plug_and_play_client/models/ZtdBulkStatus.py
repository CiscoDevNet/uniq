#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ZtdBulkStatus(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'format': 'str',
            
            
            'date': 'date-time',
            
            
            'status': 'str',
            
            
            'report': 'str',
            
            
            'siteAdded': 'int',
            
            
            'siteFailed': 'int',
            
            
            'siteSkipped': 'int',
            
            
            'deviceAdded': 'int',
            
            
            'deviceFailed': 'int',
            
            
            'deviceSkipped': 'int',
            
            
            'username': 'str',
            
            
            'requestFilename': 'str',
            
            
            'taskId': 'str',
            
            
            'type': 'str'
            
        }

        self.attributeMap = {
            
            'format': 'format',
            
            'date': 'date',
            
            'status': 'status',
            
            'report': 'report',
            
            'siteAdded': 'siteAdded',
            
            'siteFailed': 'siteFailed',
            
            'siteSkipped': 'siteSkipped',
            
            'deviceAdded': 'deviceAdded',
            
            'deviceFailed': 'deviceFailed',
            
            'deviceSkipped': 'deviceSkipped',
            
            'username': 'username',
            
            'requestFilename': 'requestFilename',
            
            'taskId': 'taskId',
            
            'type': 'type'
            
        }       

        
        
        self.format = None # str
        
        
        self.date = None # date-time
        
        
        self.status = None # str
        
        
        self.report = None # str
        
        
        self.siteAdded = None # int
        
        
        self.siteFailed = None # int
        
        
        self.siteSkipped = None # int
        
        
        self.deviceAdded = None # int
        
        
        self.deviceFailed = None # int
        
        
        self.deviceSkipped = None # int
        
        
        self.username = None # str
        
        
        self.requestFilename = None # str
        
        
        self.taskId = None # str
        
        
        self.type = None # str
        
