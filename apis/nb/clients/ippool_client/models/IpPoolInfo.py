#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class IpPoolInfo(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'role': 'str',
            
            
            'id': 'str',
            
            
            'createTime': 'int',
            
            
            'nextAddress': 'str',
            
            
            'endAddress': 'str',
            
            
            'startAddress': 'str',
            
            
            'ipPool': 'str',
            
            
            'apicAppName': 'str',
            
            
            'excludeNetworkBroadcastAddress': 'bool',
            
            
            'ipPoolName': 'str',
            
            
            'dhcpServerIp': 'list[str]',
            
            
            'gateway': 'list[str]',
            
            
            'interAppOverlap': 'bool',
            
            
            'creationOrder': 'int',
            
            
            'lastUpdateTime': 'int',
            
            
            'parentId': 'str',
            
            
            'usagePercentage': 'int',
            
            
            'freeIpCount': 'int',
            
            
            'shared': 'bool'
            
        }

        self.attributeMap = {
            
            'role': 'role',
            
            'id': 'id',
            
            'createTime': 'createTime',
            
            'nextAddress': 'nextAddress',
            
            'endAddress': 'endAddress',
            
            'startAddress': 'startAddress',
            
            'ipPool': 'ipPool',
            
            'apicAppName': 'apicAppName',
            
            'excludeNetworkBroadcastAddress': 'excludeNetworkBroadcastAddress',
            
            'ipPoolName': 'ipPoolName',
            
            'dhcpServerIp': 'dhcpServerIp',
            
            'gateway': 'gateway',
            
            'interAppOverlap': 'interAppOverlap',
            
            'creationOrder': 'creationOrder',
            
            'lastUpdateTime': 'lastUpdateTime',
            
            'parentId': 'parentId',
            
            'usagePercentage': 'usagePercentage',
            
            'freeIpCount': 'freeIpCount',
            
            'shared': 'shared'
            
        }       

        
        #Used to group IP Address Pools
        
        self.role = None # str
        
        #UUID of IP Address Pool
        
        self.id = None # str
        
        #IP Address Pool creation time
        
        self.createTime = None # int
        
        #Next available IP address in IP Address Pool
        
        self.nextAddress = None # str
        
        #Last IP address in IP Address Pool
        
        self.endAddress = None # str
        
        #First IP address in IP Address Pool
        
        self.startAddress = None # str
        
        #IP subnet in CIDR format
        
        self.ipPool = None # str
        
        #APIC-EM App Name
        
        self.apicAppName = None # str
        
        #If true then network and broadcast IP address will not be used in the usable range. Default value is false
        
        self.excludeNetworkBroadcastAddress = None # bool
        
        #IP Address Pool name
        
        self.ipPoolName = None # str
        
        #DHCP server hostname or IP address list
        
        self.dhcpServerIp = None # list[str]
        
        #Gateway IP address list
        
        self.gateway = None # list[str]
        
        #If true then overlapping IP pool is supported between APIC-EM Apps. Default value is false
        
        self.interAppOverlap = None # bool
        
        #Creation order of IP Address Pool
        
        self.creationOrder = None # int
        
        #IP Address Pool last updated time
        
        self.lastUpdateTime = None # int
        
        #Parent IP Address Pool UUID
        
        self.parentId = None # str
        
        #Current usage percentage of IP Address Pool
        
        self.usagePercentage = None # int
        
        #IP Address Pool free IP count
        
        self.freeIpCount = None # int
        
        #If true then duplicate/overlapping pool is supported. Default value is false
        
        self.shared = None # bool
        
