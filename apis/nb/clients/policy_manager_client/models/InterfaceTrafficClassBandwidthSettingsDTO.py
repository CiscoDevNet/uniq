#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class InterfaceTrafficClassBandwidthSettingsDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'trafficClassBandwidthSettingDTOList': 'list[TrafficClassBandwidthSettingDTO]',
            
            
            'interfaceSpeed': 'str'
            
        }

        self.attributeMap = {
            
            'trafficClassBandwidthSettingDTOList': 'trafficClassBandwidthSettingDTOList',
            
            'interfaceSpeed': 'interfaceSpeed'
            
        }       

        
        #List of Traffic Class Bandwidth Settings for the interface speed
        
        self.trafficClassBandwidthSettingDTOList = None # list[TrafficClassBandwidthSettingDTO]
        
        #Interface Speed. Allowed values are: 1 Mbps, 10 Mbps, 100 Mbps, 1 Gbps, 10 Gbps, 100 Gbps
        
        self.interfaceSpeed = None # str
        
