#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class Policy(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'policyScope': 'str',
            
            
            'actionProperty': 'ActionProperty',
            
            
            'actions': 'list[str]',
            
            
            'networkUser': 'NetworkUser',
            
            
            'policyOwner': 'str',
            
            
            'resource': 'PolicyResource',
            
            
            'id': 'str',
            
            
            'state': 'str',
            
            
            'instanceUuid': 'str',
            
            
            'taskId': 'str',
            
            
            'policyName': 'str',
            
            
            'policyPriority': 'int',
            
            
            'scopeWirelessSegment': 'str'
            
        }

        self.attributeMap = {
            
            'policyScope': 'policyScope',
            
            'actionProperty': 'actionProperty',
            
            'actions': 'actions',
            
            'networkUser': 'networkUser',
            
            'policyOwner': 'policyOwner',
            
            'resource': 'resource',
            
            'id': 'id',
            
            'state': 'state',
            
            'instanceUuid': 'instanceUuid',
            
            'taskId': 'taskId',
            
            'policyName': 'policyName',
            
            'policyPriority': 'policyPriority',
            
            'scopeWirelessSegment': 'scopeWirelessSegment'
            
        }       

        
        #policyScope
        
        self.policyScope = None # str
        
        #ActionProperty
        
        self.actionProperty = None # ActionProperty
        
        #Action Set
        
        self.actions = None # list[str]
        
        #Network User
        
        self.networkUser = None # NetworkUser
        
        #Policy Owner
        
        self.policyOwner = None # str
        
        #Resource
        
        self.resource = None # PolicyResource
        
        #id
        
        self.id = None # str
        
        
        self.state = None # str
        
        #
        
        self.instanceUuid = None # str
        
        #Task ID
        
        self.taskId = None # str
        
        #name of the policy
        
        self.policyName = None # str
        
        #Policy Priority
        
        self.policyPriority = None # int
        
        
        self.scopeWirelessSegment = None # str
        
