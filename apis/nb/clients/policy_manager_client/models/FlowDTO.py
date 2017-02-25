#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class FlowDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'id': 'str',
            
            
            'protocol': 'str',
            
            
            'codec': 'str',
            
            
            'status': 'str',
            
            
            'applicationName': 'str',
            
            
            'interfaceName': 'str',
            
            
            'sourcePort': 'str',
            
            
            'failureReason': 'str',
            
            
            'clientReference': 'str',
            
            
            'destPort': 'str',
            
            
            'detailedFlowType': 'str',
            
            
            'flowType': 'str',
            
            
            'interfaceId': 'str',
            
            
            'matchDSCP': 'str',
            
            
            'networkDeviceId': 'str',
            
            
            'networkDeviceName': 'str',
            
            
            'peakBandwidth': 'str',
            
            
            'averageBandwidth': 'str',
            
            
            'destIP': 'str',
            
            
            'sourceIP': 'str'
            
        }

        self.attributeMap = {
            
            'id': 'id',
            
            'protocol': 'protocol',
            
            'codec': 'codec',
            
            'status': 'status',
            
            'applicationName': 'applicationName',
            
            'interfaceName': 'interfaceName',
            
            'sourcePort': 'sourcePort',
            
            'failureReason': 'failureReason',
            
            'clientReference': 'clientReference',
            
            'destPort': 'destPort',
            
            'detailedFlowType': 'detailedFlowType',
            
            'flowType': 'flowType',
            
            'interfaceId': 'interfaceId',
            
            'matchDSCP': 'matchDSCP',
            
            'networkDeviceId': 'networkDeviceId',
            
            'networkDeviceName': 'networkDeviceName',
            
            'peakBandwidth': 'peakBandwidth',
            
            'averageBandwidth': 'averageBandwidth',
            
            'destIP': 'destIP',
            
            'sourceIP': 'sourceIP'
            
        }       

        
        #id
        
        self.id = None # str
        
        #protocol
        
        self.protocol = None # str
        
        #codec
        
        self.codec = None # str
        
        
        self.status = None # str
        
        #APIC-EM application name
        
        self.applicationName = None # str
        
        #interfaceName
        
        self.interfaceName = None # str
        
        #sourcePort
        
        self.sourcePort = None # str
        
        
        self.failureReason = None # str
        
        #clientReference (can be used by the client as a reference to this resource
        
        self.clientReference = None # str
        
        #destPort
        
        self.destPort = None # str
        
        #detailedFlowType (more detailed classification than flowType)
        
        self.detailedFlowType = None # str
        
        #flowType
        
        self.flowType = None # str
        
        #interfaceId
        
        self.interfaceId = None # str
        
        #DSCP of the flow
        
        self.matchDSCP = None # str
        
        #networkDeviceId
        
        self.networkDeviceId = None # str
        
        #networkDeviceName
        
        self.networkDeviceName = None # str
        
        #peakBandwidth in kbps (min: 0, max: 2147483647 kbps)
        
        self.peakBandwidth = None # str
        
        #averageBandwidth in kbps (min: 0, max: 2147483647 kbps)
        
        self.averageBandwidth = None # str
        
        #destIP
        
        self.destIP = None # str
        
        #sourceIP
        
        self.sourceIP = None # str
        
