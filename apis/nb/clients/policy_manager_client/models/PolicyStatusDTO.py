#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PolicyStatusDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'businessRelevantConsumerProducerApplications': 'list[PolicyConsumerProducerApplication]',
            
            
            'businessIrrelevantConsumerProducerApplications': 'list[PolicyConsumerProducerApplication]',
            
            
            'networkDeviceIp': 'str',
            
            
            'businessRelevantApplications': 'list[PolicyApplication]',
            
            
            'businessIrrelevantApplications': 'list[PolicyApplication]',
            
            
            'applicationPolicyCount': 'int',
            
            
            'pending': 'bool',
            
            
            'status': 'str',
            
            
            'instanceUuid': 'str',
            
            
            'lastUpdated': 'str',
            
            
            'failureReason': 'str',
            
            
            'lastSuccessfulPolicyVersion': 'str',
            
            
            'policyVersion': 'str',
            
            
            'policyScope': 'str',
            
            
            'outOfScope': 'bool',
            
            
            'networkDeviceId': 'str',
            
            
            'networkDeviceName': 'str',
            
            
            'scopeWirelessSegment': 'str'
            
        }

        self.attributeMap = {
            
            'businessRelevantConsumerProducerApplications': 'businessRelevantConsumerProducerApplications',
            
            'businessIrrelevantConsumerProducerApplications': 'businessIrrelevantConsumerProducerApplications',
            
            'networkDeviceIp': 'networkDeviceIp',
            
            'businessRelevantApplications': 'businessRelevantApplications',
            
            'businessIrrelevantApplications': 'businessIrrelevantApplications',
            
            'applicationPolicyCount': 'applicationPolicyCount',
            
            'pending': 'pending',
            
            'status': 'status',
            
            'instanceUuid': 'instanceUuid',
            
            'lastUpdated': 'lastUpdated',
            
            'failureReason': 'failureReason',
            
            'lastSuccessfulPolicyVersion': 'lastSuccessfulPolicyVersion',
            
            'policyVersion': 'policyVersion',
            
            'policyScope': 'policyScope',
            
            'outOfScope': 'outOfScope',
            
            'networkDeviceId': 'networkDeviceId',
            
            'networkDeviceName': 'networkDeviceName',
            
            'scopeWirelessSegment': 'scopeWirelessSegment'
            
        }       

        
        
        self.businessRelevantConsumerProducerApplications = None # list[PolicyConsumerProducerApplication]
        
        
        self.businessIrrelevantConsumerProducerApplications = None # list[PolicyConsumerProducerApplication]
        
        
        self.networkDeviceIp = None # str
        
        
        self.businessRelevantApplications = None # list[PolicyApplication]
        
        
        self.businessIrrelevantApplications = None # list[PolicyApplication]
        
        
        self.applicationPolicyCount = None # int
        
        
        self.pending = None # bool
        
        
        self.status = None # str
        
        
        self.instanceUuid = None # str
        
        
        self.lastUpdated = None # str
        
        
        self.failureReason = None # str
        
        
        self.lastSuccessfulPolicyVersion = None # str
        
        
        self.policyVersion = None # str
        
        
        self.policyScope = None # str
        
        
        self.outOfScope = None # bool
        
        
        self.networkDeviceId = None # str
        
        
        self.networkDeviceName = None # str
        
        
        self.scopeWirelessSegment = None # str
        
