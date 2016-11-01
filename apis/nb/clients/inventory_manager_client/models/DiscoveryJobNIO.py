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
            
            'startTime': 'str',
            
            
            'endTime': 'str',
            
            
            'name': 'str',
            
            
            'pingStatus': 'str',
            
            
            'snmpStatus': 'str',
            
            
            'cliStatus': 'str',
            
            
            'inventoryReachabilityStatus': 'str',
            
            
            'taskId': 'str',
            
            
            'discoveryStatus': 'str',
            
            
            'inventoryCollectionStatus': 'str',
            
            
            'jobStatus': 'str',
            
            
            'ipAddress': 'str',
            
            
            'id': 'str',
            
            
            'attributeInfo': 'dict'
            
        }

        self.attributeMap = {
            
            'startTime': 'startTime',
            
            'endTime': 'endTime',
            
            'name': 'name',
            
            'pingStatus': 'pingStatus',
            
            'snmpStatus': 'snmpStatus',
            
            'cliStatus': 'cliStatus',
            
            'inventoryReachabilityStatus': 'inventoryReachabilityStatus',
            
            'taskId': 'taskId',
            
            'discoveryStatus': 'discoveryStatus',
            
            'inventoryCollectionStatus': 'inventoryCollectionStatus',
            
            'jobStatus': 'jobStatus',
            
            'ipAddress': 'ipAddress',
            
            'id': 'id',
            
            'attributeInfo': 'attributeInfo'
            
        }       

        
        #Discovery job start time
        
        self.startTime = None # str
        
        
        self.endTime = None # str
        
        #Discovery job name
        
        self.name = None # str
        
        #Ping status for the IP during this job run
        
        self.pingStatus = None # str
        
        #SNMP status for the IP during this job run
        
        self.snmpStatus = None # str
        
        #CLI status for the IP during this job run
        
        self.cliStatus = None # str
        
        #Last known reachabilty status of the device
        
        self.inventoryReachabilityStatus = None # str
        
        #Discovery job task id
        
        self.taskId = None # str
        
        #Discovery status for the IP
        
        self.discoveryStatus = None # str
        
        #Last known inventory collection status of the device
        
        self.inventoryCollectionStatus = None # str
        
        
        self.jobStatus = None # str
        
        #IP Address
        
        self.ipAddress = None # str
        
        
        self.id = None # str
        
        
        self.attributeInfo = None # dict
        
