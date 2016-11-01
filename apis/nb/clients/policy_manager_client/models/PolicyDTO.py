#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PolicyDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'priority': 'int',
            
            
            'name': 'str',
            
            
            'description': 'str',
            
            
            'contract': 'PolicyContractDTO',
            
            
            'consumer': 'ConsumerDTO',
            
            
            'producer': 'ProducerDTO',
            
            
            'id': 'str',
            
            
            'lastUpdateTime': 'int',
            
            
            'createTime': 'int'
            
        }

        self.attributeMap = {
            
            'priority': 'priority',
            
            'name': 'name',
            
            'description': 'description',
            
            'contract': 'contract',
            
            'consumer': 'consumer',
            
            'producer': 'producer',
            
            'id': 'id',
            
            'lastUpdateTime': 'lastUpdateTime',
            
            'createTime': 'createTime'
            
        }       

        
        #priority
        
        self.priority = None # int
        
        #name
        
        self.name = None # str
        
        #description
        
        self.description = None # str
        
        #contract
        
        self.contract = None # PolicyContractDTO
        
        #consumer
        
        self.consumer = None # ConsumerDTO
        
        #producer
        
        self.producer = None # ProducerDTO
        
        #id
        
        self.id = None # str
        
        #lastUpdateTime
        
        self.lastUpdateTime = None # int
        
        #createTime
        
        self.createTime = None # int
        
