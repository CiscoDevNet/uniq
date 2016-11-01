#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class DeviceStatistics(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'cpuStatistics': 'CpuStatistics',
            
            
            'memoryStatistics': 'MemoryStatistics'
            
        }

        self.attributeMap = {
            
            'cpuStatistics': 'cpuStatistics',
            
            'memoryStatistics': 'memoryStatistics'
            
        }       

        
        #Device CPU statistics
        
        self.cpuStatistics = None # CpuStatistics
        
        #Device Memory statistics
        
        self.memoryStatistics = None # MemoryStatistics
        
