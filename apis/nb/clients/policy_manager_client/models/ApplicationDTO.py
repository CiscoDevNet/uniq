#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ApplicationDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'category': 'str',
            
            
            'trafficClass': 'str',
            
            
            'name': 'str',
            
            
            'id': 'str',
            
            
            'status': 'str',
            
            
            'rank': 'int',
            
            
            'longDescription': 'str',
            
            
            'instanceUuid': 'str',
            
            
            'url': 'str',
            
            
            'references': 'str',
            
            
            'dscp': 'str',
            
            
            'ipPorts': 'str',
            
            
            'appProtocol': 'str',
            
            
            'applicationGroup': 'str',
            
            
            'categoryId': 'str',
            
            
            'enabled': 'str',
            
            
            'encrypted': 'str',
            
            
            'engineId': 'str',
            
            
            'globalId': 'str',
            
            
            'helpString': 'str',
            
            
            'ignoreConflict': 'bool',
            
            
            'indicativeIpPorts': 'str',
            
            
            'indicativeTcpPorts': 'str',
            
            
            'indicativeUdpPorts': 'str',
            
            
            'isRepresentativeApp': 'bool',
            
            
            'nbarId': 'str',
            
            
            'p2pTechnology': 'str',
            
            
            'pfrThresholdJitter': 'int',
            
            
            'pfrThresholdJitterPriority': 'int',
            
            
            'pfrThresholdLossRate': 'int',
            
            
            'pfrThresholdLossRatePriority': 'int',
            
            
            'pfrThresholdOneWayDelay': 'int',
            
            
            'pfrThresholdOneWayDelayPriority': 'int',
            
            
            'popularity': 'int',
            
            
            'selectorId': 'str',
            
            
            'subCategory': 'str',
            
            
            'tcpPorts': 'str',
            
            
            'transportIps': 'str',
            
            
            'tunnel': 'str',
            
            
            'udpPorts': 'str',
            
            
            'applicationIpPortClassifiers': 'list[ApplicationIpPortClassifierDTO]'
            
        }

        self.attributeMap = {
            
            'category': 'category',
            
            'trafficClass': 'trafficClass',
            
            'name': 'name',
            
            'id': 'id',
            
            'status': 'status',
            
            'rank': 'rank',
            
            'longDescription': 'longDescription',
            
            'instanceUuid': 'instanceUuid',
            
            'url': 'url',
            
            'references': 'references',
            
            'dscp': 'dscp',
            
            'ipPorts': 'ipPorts',
            
            'appProtocol': 'appProtocol',
            
            'applicationGroup': 'applicationGroup',
            
            'categoryId': 'categoryId',
            
            'enabled': 'enabled',
            
            'encrypted': 'encrypted',
            
            'engineId': 'engineId',
            
            'globalId': 'globalId',
            
            'helpString': 'helpString',
            
            'ignoreConflict': 'ignoreConflict',
            
            'indicativeIpPorts': 'indicativeIpPorts',
            
            'indicativeTcpPorts': 'indicativeTcpPorts',
            
            'indicativeUdpPorts': 'indicativeUdpPorts',
            
            'isRepresentativeApp': 'isRepresentativeApp',
            
            'nbarId': 'nbarId',
            
            'p2pTechnology': 'p2pTechnology',
            
            'pfrThresholdJitter': 'pfrThresholdJitter',
            
            'pfrThresholdJitterPriority': 'pfrThresholdJitterPriority',
            
            'pfrThresholdLossRate': 'pfrThresholdLossRate',
            
            'pfrThresholdLossRatePriority': 'pfrThresholdLossRatePriority',
            
            'pfrThresholdOneWayDelay': 'pfrThresholdOneWayDelay',
            
            'pfrThresholdOneWayDelayPriority': 'pfrThresholdOneWayDelayPriority',
            
            'popularity': 'popularity',
            
            'selectorId': 'selectorId',
            
            'subCategory': 'subCategory',
            
            'tcpPorts': 'tcpPorts',
            
            'transportIps': 'transportIps',
            
            'tunnel': 'tunnel',
            
            'udpPorts': 'udpPorts',
            
            'applicationIpPortClassifiers': 'applicationIpPortClassifiers'
            
        }       

        
        #Category name
        
        self.category = None # str
        
        #Traffic class to which the app belongs
        
        self.trafficClass = None # str
        
        #App Name
        
        self.name = None # str
        
        #id
        
        self.id = None # str
        
        #Gives status of the app
        
        self.status = None # str
        
        #rank
        
        self.rank = None # int
        
        #Long description of the app
        
        self.longDescription = None # str
        
        #
        
        self.instanceUuid = None # str
        
        #url of the app
        
        self.url = None # str
        
        #references of the app
        
        self.references = None # str
        
        #dscp value
        
        self.dscp = None # str
        
        #list of ip ports
        
        self.ipPorts = None # str
        
        #protocol of the app. Valid values are tcp, udp, tcp/udp, ip or it could be empty. Values are case sensitive.
        
        self.appProtocol = None # str
        
        #App group name
        
        self.applicationGroup = None # str
        
        #Category id
        
        self.categoryId = None # str
        
        #If the app enabled
        
        self.enabled = None # str
        
        #If the app is encrypted
        
        self.encrypted = None # str
        
        #engine id
        
        self.engineId = None # str
        
        #global id
        
        self.globalId = None # str
        
        #help string to describe the app
        
        self.helpString = None # str
        
        #If true ignore conflicts with other Applications
        
        self.ignoreConflict = None # bool
        
        #Indicative ip ports
        
        self.indicativeIpPorts = None # str
        
        #Indicative tcp ports
        
        self.indicativeTcpPorts = None # str
        
        #Indicative udp ports
        
        self.indicativeUdpPorts = None # str
        
        #If the app is representative
        
        self.isRepresentativeApp = None # bool
        
        #nbar id
        
        self.nbarId = None # str
        
        #If the app is a p2p technology
        
        self.p2pTechnology = None # str
        
        #PfR Threshold Jitter
        
        self.pfrThresholdJitter = None # int
        
        #PfR Threshold Jitter Priority
        
        self.pfrThresholdJitterPriority = None # int
        
        #PfR Threshold Loss Rate
        
        self.pfrThresholdLossRate = None # int
        
        #PfR Threshold Loss Rate Priority
        
        self.pfrThresholdLossRatePriority = None # int
        
        #PfR Threshold One Way Delay
        
        self.pfrThresholdOneWayDelay = None # int
        
        #PfR Threshold One Way Delay Priority
        
        self.pfrThresholdOneWayDelayPriority = None # int
        
        #popularity of the app
        
        self.popularity = None # int
        
        #selector id
        
        self.selectorId = None # str
        
        #Sub-Category Id
        
        self.subCategory = None # str
        
        #list of tcp ports
        
        self.tcpPorts = None # str
        
        #Transport IP of the app
        
        self.transportIps = None # str
        
        #If the app is a tunnel
        
        self.tunnel = None # str
        
        #list of udp ports
        
        self.udpPorts = None # str
        
        #IP Port classifiers for the application
        
        self.applicationIpPortClassifiers = None # list[ApplicationIpPortClassifierDTO]
        
