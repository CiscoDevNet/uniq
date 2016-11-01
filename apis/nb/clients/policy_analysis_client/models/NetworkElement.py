#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class NetworkElement(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'deviceStatistics': 'DeviceStatistics',
            
            
            'perfMonStatistics': 'list[PerfMonitorStatistics]',
            
            
            'perfMonCollectionFailureReason': 'str',
            
            
            'deviceStatsCollection': 'str',
            
            
            'deviceStatsCollectionFailureReason': 'str',
            
            
            'detailedStatus': 'DetailedStatus',
            
            
            'tunnels': 'list[str]',
            
            
            'linkInformationSource': 'str',
            
            
            'accuracyList': 'list[Accuracy]',
            
            
            'perfMonCollection': 'str',
            
            
            'name': 'str',
            
            
            'id': 'str',
            
            
            'type': 'str',
            
            
            'role': 'str',
            
            
            'ip': 'str',
            
            
            'egressPhysicalInterface': 'Interface',
            
            
            'egressVirtualInterface': 'Interface',
            
            
            'ingressPhysicalInterface': 'Interface',
            
            
            'ingressVirtualInterface': 'Interface'
            
        }

        self.attributeMap = {
            
            'deviceStatistics': 'deviceStatistics',
            
            'perfMonStatistics': 'perfMonStatistics',
            
            'perfMonCollectionFailureReason': 'perfMonCollectionFailureReason',
            
            'deviceStatsCollection': 'deviceStatsCollection',
            
            'deviceStatsCollectionFailureReason': 'deviceStatsCollectionFailureReason',
            
            'detailedStatus': 'detailedStatus',
            
            'tunnels': 'tunnels',
            
            'linkInformationSource': 'linkInformationSource',
            
            'accuracyList': 'accuracyList',
            
            'perfMonCollection': 'perfMonCollection',
            
            'name': 'name',
            
            'id': 'id',
            
            'type': 'type',
            
            'role': 'role',
            
            'ip': 'ip',
            
            'egressPhysicalInterface': 'egressPhysicalInterface',
            
            'egressVirtualInterface': 'egressVirtualInterface',
            
            'ingressPhysicalInterface': 'ingressPhysicalInterface',
            
            'ingressVirtualInterface': 'ingressVirtualInterface'
            
        }       

        
        
        self.deviceStatistics = None # DeviceStatistics
        
        
        self.perfMonStatistics = None # list[PerfMonitorStatistics]
        
        
        self.perfMonCollectionFailureReason = None # str
        
        #A status value from [ INPROGRESS, SUCCESS, FAILED ] 
        
        self.deviceStatsCollection = None # str
        
        
        self.deviceStatsCollectionFailureReason = None # str
        
        
        self.detailedStatus = None # DetailedStatus
        
        #Tunnels this network element is in
        
        self.tunnels = None # list[str]
        
        #The source of the link information to the next hop
        
        self.linkInformationSource = None # str
        
        
        self.accuracyList = None # list[Accuracy]
        
        #A status value from [ INPROGRESS, SUCCESS, FAILED ] 
        
        self.perfMonCollection = None # str
        
        #Network Device name
        
        self.name = None # str
        
        #Network Device ID
        
        self.id = None # str
        
        #Network Device Type(can be switch,router,wired host or wireless host)
        
        self.type = None # str
        
        #Role of device in network(can be access,core,distribution or border router)
        
        self.role = None # str
        
        #Network Device IP
        
        self.ip = None # str
        
        #Egress physical interface of the network device
        
        self.egressPhysicalInterface = None # Interface
        
        #Egress virtual interface of the network device
        
        self.egressVirtualInterface = None # Interface
        
        #Igress physical interface of the network device
        
        self.ingressPhysicalInterface = None # Interface
        
        #Ingress virtual interface of the network device
        
        self.ingressVirtualInterface = None # Interface
        
