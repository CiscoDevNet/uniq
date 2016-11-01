#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class LinkWrapper(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'endPortID': 'str',
            
            
            'startPortID': 'str',
            
            
            'greyOut': 'bool',
            
            
            'source': 'str',
            
            
            'target': 'str',
            
            
            'id': 'str',
            
            
            'endPortName': 'str',
            
            
            'endPortSpeed': 'str',
            
            
            'startPortName': 'str',
            
            
            'startPortSpeed': 'str',
            
            
            'linkStatus': 'str',
            
            
            'tag': 'str',
            
            
            'startPortIpv4Mask': 'str',
            
            
            'startPortIpv4Address': 'str',
            
            
            'endPortIpv4Mask': 'str',
            
            
            'endPortIpv4Address': 'str'
            
        }

        self.attributeMap = {
            
            'endPortID': 'endPortID',
            
            'startPortID': 'startPortID',
            
            'greyOut': 'greyOut',
            
            'source': 'source',
            
            'target': 'target',
            
            'id': 'id',
            
            'endPortName': 'endPortName',
            
            'endPortSpeed': 'endPortSpeed',
            
            'startPortName': 'startPortName',
            
            'startPortSpeed': 'startPortSpeed',
            
            'linkStatus': 'linkStatus',
            
            'tag': 'tag',
            
            'startPortIpv4Mask': 'startPortIpv4Mask',
            
            'startPortIpv4Address': 'startPortIpv4Address',
            
            'endPortIpv4Mask': 'endPortIpv4Mask',
            
            'endPortIpv4Address': 'endPortIpv4Address'
            
        }       

        
        #Device port ID corresponding to end devices
        
        self.endPortID = None # str
        
        #Device port ID corresponding to start devices
        
        self.startPortID = None # str
        
        #Device greyout
        
        self.greyOut = None # bool
        
        #Device ID correspondng to the source device 
        
        self.source = None # str
        
        #Device ID corresponding to the target device
        
        self.target = None # str
        
        #Unified identifier for device
        
        self.id = None # str
        
        #Interface port name corresponding to end devices
        
        self.endPortName = None # str
        
        #Interface port speed corresponding to end devices
        
        self.endPortSpeed = None # str
        
        #Interface port name corresponding to start devices
        
        self.startPortName = None # str
        
        #Interface port speed corresponding to start devices
        
        self.startPortSpeed = None # str
        
        #Indicates whether link is working
        
        self.linkStatus = None # str
        
        #Tag for the devices
        
        self.tag = None # str
        
        #Interface port IPv4 mask corresponding to start devices
        
        self.startPortIpv4Mask = None # str
        
        #Interface port IPv4 address corresponding to start devices
        
        self.startPortIpv4Address = None # str
        
        #Interface port IPv4 mask corresponding to end devices
        
        self.endPortIpv4Mask = None # str
        
        #Interface port IPv4 address corresponding to end devices
        
        self.endPortIpv4Address = None # str
        
