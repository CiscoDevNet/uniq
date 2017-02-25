#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class DiscoveryJobNIO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'pingStatus': 'str',
            
            
            'snmpStatus': 'str',
            
            
            'cliStatus': 'str',
            
            
            'inventoryReachabilityStatus': 'str',
            
            
            'name': 'str',
            
            
            'startTime': 'str',
            
            
            'endTime': 'str',
            
            
            'taskId': 'str',
            
            
            'inventoryCollectionStatus': 'str',
            
            
            'jobStatus': 'str',
            
            
            'ipAddress': 'str',
            
            
            'discoveryStatus': 'str',
            
            
            'id': 'str',
            
            
            'attributeInfo': 'dict'
            
        }

        self.attributeMap = {
            
            'pingStatus': 'pingStatus',
            
            'snmpStatus': 'snmpStatus',
            
            'cliStatus': 'cliStatus',
            
            'inventoryReachabilityStatus': 'inventoryReachabilityStatus',
            
            'name': 'name',
            
            'startTime': 'startTime',
            
            'endTime': 'endTime',
            
            'taskId': 'taskId',
            
            'inventoryCollectionStatus': 'inventoryCollectionStatus',
            
            'jobStatus': 'jobStatus',
            
            'ipAddress': 'ipAddress',
            
            'discoveryStatus': 'discoveryStatus',
            
            'id': 'id',
            
            'attributeInfo': 'attributeInfo'
            
        }       

        
        #Ping status for the IP during this job run
        
        self.pingStatus = None # str
        
        #SNMP status for the IP during this job run
        
        self.snmpStatus = None # str
        
        #CLI status for the IP during this job run
        
        self.cliStatus = None # str
        
        #Last known reachabilty status of the device
        
        self.inventoryReachabilityStatus = None # str
        
        #Discovery job name
        
        self.name = None # str
        
        #Discovery job start time
        
        self.startTime = None # str
        
        #End time for the discovery job
        
        self.endTime = None # str
        
        #Discovery job task id
        
        self.taskId = None # str
        
        #Last known inventory collection status of the device
        
        self.inventoryCollectionStatus = None # str
        
        #Status of the job
        
        self.jobStatus = None # str
        
        #IP Address
        
        self.ipAddress = None # str
        
        #Discovery status for the IP
        
        self.discoveryStatus = None # str
        
        
        self.id = None # str
        
        
        self.attributeInfo = None # dict
        
