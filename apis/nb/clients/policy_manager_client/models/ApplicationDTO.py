#!/usr/bin/env python
#pylint: skip-file
"""
Copyright 2016 Cisco Systems

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

class ApplicationDTO(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'name': 'str',


            'id': 'str',


            'trafficClass': 'str',


            'rank': 'int',


            'status': 'str',


            'categoryId': 'str',


            'instanceUuid': 'str',


            'subCategory': 'str',


            'globalId': 'str',


            'engineId': 'str',


            'selectorId': 'str',


            'helpString': 'str',


            'references': 'str',


            'applicationGroup': 'str',


            'encrypted': 'str',


            'tunnel': 'str',


            'category': 'str',


            'longDescription': 'str',


            'appProtocol': 'str',


            'tcpPorts': 'str',


            'indicativeTcpPorts': 'str',


            'udpPorts': 'str',


            'indicativeUdpPorts': 'str',


            'ipPorts': 'str',


            'url': 'str',


            'enabled': 'str',


            'indicativeIpPorts': 'str',


            'isRepresentativeApp': 'bool',


            'nbarId': 'str',


            'p2pTechnology': 'str',


            'pfrThresholdJitterPriority': 'int',


            'pfrThresholdLossRatePriority': 'int',


            'pfrThresholdOneWayDelayPriority': 'int',


            'dscp': 'str',


            'pfrThresholdJitter': 'int',


            'pfrThresholdLossRate': 'int',


            'pfrThresholdOneWayDelay': 'int',


            'popularity': 'int',


            'transportIps': 'str',


            'ignoreConflict': 'bool'

        }

        self.attributeMap = {

            'name': 'name',

            'id': 'id',

            'trafficClass': 'trafficClass',

            'rank': 'rank',

            'status': 'status',

            'categoryId': 'categoryId',

            'instanceUuid': 'instanceUuid',

            'subCategory': 'subCategory',

            'globalId': 'globalId',

            'engineId': 'engineId',

            'selectorId': 'selectorId',

            'helpString': 'helpString',

            'references': 'references',

            'applicationGroup': 'applicationGroup',

            'encrypted': 'encrypted',

            'tunnel': 'tunnel',

            'category': 'category',

            'longDescription': 'longDescription',

            'appProtocol': 'appProtocol',

            'tcpPorts': 'tcpPorts',

            'indicativeTcpPorts': 'indicativeTcpPorts',

            'udpPorts': 'udpPorts',

            'indicativeUdpPorts': 'indicativeUdpPorts',

            'ipPorts': 'ipPorts',

            'url': 'url',

            'enabled': 'enabled',

            'indicativeIpPorts': 'indicativeIpPorts',

            'isRepresentativeApp': 'isRepresentativeApp',

            'nbarId': 'nbarId',

            'p2pTechnology': 'p2pTechnology',

            'pfrThresholdJitterPriority': 'pfrThresholdJitterPriority',

            'pfrThresholdLossRatePriority': 'pfrThresholdLossRatePriority',

            'pfrThresholdOneWayDelayPriority': 'pfrThresholdOneWayDelayPriority',

            'dscp': 'dscp',

            'pfrThresholdJitter': 'pfrThresholdJitter',

            'pfrThresholdLossRate': 'pfrThresholdLossRate',

            'pfrThresholdOneWayDelay': 'pfrThresholdOneWayDelay',

            'popularity': 'popularity',

            'transportIps': 'transportIps',

            'ignoreConflict': 'ignoreConflict'

        }


        #App Name

        self.name = None # str

        #id

        self.id = None # str

        #Traffic class to which the app belongs

        self.trafficClass = None # str

        #rank

        self.rank = None # int

        #Gives status of the app

        self.status = None # str

        #Category id

        self.categoryId = None # str

        #

        self.instanceUuid = None # str

        #Sub-Category Id

        self.subCategory = None # str

        #global id

        self.globalId = None # str

        #engine id

        self.engineId = None # str

        #selector id

        self.selectorId = None # str

        #help string to describe the app

        self.helpString = None # str

        #references of the app

        self.references = None # str

        #App group name

        self.applicationGroup = None # str

        #If the app is encrypted

        self.encrypted = None # str

        #If the app is a tunnel

        self.tunnel = None # str

        #Category name

        self.category = None # str

        #Long description of the app

        self.longDescription = None # str

        #protocol of the app. Valid values are tcp, udp, tcp/udp, ip or it could be empty. Values are case sensitive.

        self.appProtocol = None # str

        #list of tcp ports

        self.tcpPorts = None # str

        #Indicative tcp ports

        self.indicativeTcpPorts = None # str

        #list of udp ports

        self.udpPorts = None # str

        #Indicative udp ports

        self.indicativeUdpPorts = None # str

        #list of ip ports

        self.ipPorts = None # str

        #url of the app

        self.url = None # str

        #If the app enabled

        self.enabled = None # str

        #Indicative ip ports

        self.indicativeIpPorts = None # str

        #If the app is representative

        self.isRepresentativeApp = None # bool

        #nbar id

        self.nbarId = None # str

        #If the app is a p2p technology

        self.p2pTechnology = None # str

        #PfR Threshold Jitter Priority

        self.pfrThresholdJitterPriority = None # int

        #PfR Threshold Loss Rate Priority

        self.pfrThresholdLossRatePriority = None # int

        #PfR Threshold One Way Delay Priority

        self.pfrThresholdOneWayDelayPriority = None # int

        #dscp value

        self.dscp = None # str

        #PfR Threshold Jitter

        self.pfrThresholdJitter = None # int

        #PfR Threshold Loss Rate

        self.pfrThresholdLossRate = None # int

        #PfR Threshold One Way Delay

        self.pfrThresholdOneWayDelay = None # int

        #popularity of the app

        self.popularity = None # int

        #Transport IP of the app

        self.transportIps = None # str

        #If true ignore conflicts with other Applications

        self.ignoreConflict = None # bool

