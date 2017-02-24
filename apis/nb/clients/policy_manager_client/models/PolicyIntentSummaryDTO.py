#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PolicyIntentSummaryDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'numberOfDevices': 'int',
            
            
            'applicationsStale': 'bool',
            
            
            'allPoliciesDeleted': 'bool',
            
            
            'serviceProviderProfileStale': 'bool',
            
            
            'bandwidthProfileStale': 'bool',
            
            
            'operations': 'list[str]',
            
            
            'lastUpdateTime': 'int',
            
            
            'policyScope': 'str',
            
            
            'numberOfAssignedApplications': 'int',
            
            
            'latestPolicyVersion': 'int',
            
            
            'scopeWirelessSegment': 'str'
            
        }

        self.attributeMap = {
            
            'numberOfDevices': 'numberOfDevices',
            
            'applicationsStale': 'applicationsStale',
            
            'allPoliciesDeleted': 'allPoliciesDeleted',
            
            'serviceProviderProfileStale': 'serviceProviderProfileStale',
            
            'bandwidthProfileStale': 'bandwidthProfileStale',
            
            'operations': 'operations',
            
            'lastUpdateTime': 'lastUpdateTime',
            
            'policyScope': 'policyScope',
            
            'numberOfAssignedApplications': 'numberOfAssignedApplications',
            
            'latestPolicyVersion': 'latestPolicyVersion',
            
            'scopeWirelessSegment': 'scopeWirelessSegment'
            
        }       

        
        #The number of devices in the policy scope
        
        self.numberOfDevices = None # int
        
        #Flag to indicate if applications are stale in the policy
        
        self.applicationsStale = None # bool
        
        #Flag to indicate if all policies are deleted in the policy scope
        
        self.allPoliciesDeleted = None # bool
        
        #Flag to indicate if Service Provider Profiles are stale in the policy scope
        
        self.serviceProviderProfileStale = None # bool
        
        #Flag to indicate if Bandwidth Profile associated with the policy is stale
        
        self.bandwidthProfileStale = None # bool
        
        #The operations in that version. (policy-add, policy-update, policy-delete)
        
        self.operations = None # list[str]
        
        #Last update time of the policy
        
        self.lastUpdateTime = None # int
        
        #Scope of the policy
        
        self.policyScope = None # str
        
        #The number of assigned applications in the policy
        
        self.numberOfAssignedApplications = None # int
        
        #Latest version of the policy
        
        self.latestPolicyVersion = None # int
        
        #Wireless segment of the policy
        
        self.scopeWirelessSegment = None # str
        
