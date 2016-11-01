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
            
            
            'applicationPolicyCount': 'int',
            
            
            'businessIrrelevantApplications': 'list[PolicyApplication]',
            
            
            'pending': 'bool',
            
            
            'businessRelevantApplications': 'list[PolicyApplication]',
            
            
            'status': 'str',
            
            
            'instanceUuid': 'str',
            
            
            'lastUpdated': 'str',
            
            
            'policyScope': 'str',
            
            
            'failureReason': 'str',
            
            
            'lastSuccessfulPolicyVersion': 'str',
            
            
            'policyVersion': 'str',
            
            
            'networkDeviceId': 'str',
            
            
            'networkDeviceName': 'str',
            
            
            'outOfScope': 'bool',
            
            
            'scopeWirelessSegment': 'str',
            
            
            'networkDeviceIp': 'str'
            
        }

        self.attributeMap = {
            
            'businessRelevantConsumerProducerApplications': 'businessRelevantConsumerProducerApplications',
            
            'businessIrrelevantConsumerProducerApplications': 'businessIrrelevantConsumerProducerApplications',
            
            'applicationPolicyCount': 'applicationPolicyCount',
            
            'businessIrrelevantApplications': 'businessIrrelevantApplications',
            
            'pending': 'pending',
            
            'businessRelevantApplications': 'businessRelevantApplications',
            
            'status': 'status',
            
            'instanceUuid': 'instanceUuid',
            
            'lastUpdated': 'lastUpdated',
            
            'policyScope': 'policyScope',
            
            'failureReason': 'failureReason',
            
            'lastSuccessfulPolicyVersion': 'lastSuccessfulPolicyVersion',
            
            'policyVersion': 'policyVersion',
            
            'networkDeviceId': 'networkDeviceId',
            
            'networkDeviceName': 'networkDeviceName',
            
            'outOfScope': 'outOfScope',
            
            'scopeWirelessSegment': 'scopeWirelessSegment',
            
            'networkDeviceIp': 'networkDeviceIp'
            
        }       

        
        
        self.businessRelevantConsumerProducerApplications = None # list[PolicyConsumerProducerApplication]
        
        
        self.businessIrrelevantConsumerProducerApplications = None # list[PolicyConsumerProducerApplication]
        
        
        self.applicationPolicyCount = None # int
        
        
        self.businessIrrelevantApplications = None # list[PolicyApplication]
        
        
        self.pending = None # bool
        
        
        self.businessRelevantApplications = None # list[PolicyApplication]
        
        
        self.status = None # str
        
        
        self.instanceUuid = None # str
        
        
        self.lastUpdated = None # str
        
        
        self.policyScope = None # str
        
        
        self.failureReason = None # str
        
        
        self.lastSuccessfulPolicyVersion = None # str
        
        
        self.policyVersion = None # str
        
        
        self.networkDeviceId = None # str
        
        
        self.networkDeviceName = None # str
        
        
        self.outOfScope = None # bool
        
        
        self.scopeWirelessSegment = None # str
        
        
        self.networkDeviceIp = None # str
        
