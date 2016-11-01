#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class NodeWrapper(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'customParam': 'NodeWrapperCustom',
            
            
            'greyOut': 'bool',
            
            
            'tags': 'list[str]',
            
            
            'aclApplied': 'bool',
            
            
            'role': 'str',
            
            
            'order': 'int',
            
            
            'id': 'str',
            
            
            'roleSource': 'str',
            
            
            'family': 'str',
            
            
            'platformId': 'str',
            
            
            'softwareVersion': 'str',
            
            
            'userId': 'str',
            
            
            'vlanId': 'str',
            
            
            'osType': 'str',
            
            
            'networkType': 'str',
            
            
            'deviceType': 'str',
            
            
            'y': 'int',
            
            
            'x': 'int',
            
            
            'label': 'str',
            
            
            'ip': 'str',
            
            
            'nodeType': 'str',
            
            
            'upperNode': 'str',
            
            
            'fixed': 'bool',
            
            
            'dataPathId': 'str'
            
        }

        self.attributeMap = {
            
            'customParam': 'customParam',
            
            'greyOut': 'greyOut',
            
            'tags': 'tags',
            
            'aclApplied': 'aclApplied',
            
            'role': 'role',
            
            'order': 'order',
            
            'id': 'id',
            
            'roleSource': 'roleSource',
            
            'family': 'family',
            
            'platformId': 'platformId',
            
            'softwareVersion': 'softwareVersion',
            
            'userId': 'userId',
            
            'vlanId': 'vlanId',
            
            'osType': 'osType',
            
            'networkType': 'networkType',
            
            'deviceType': 'deviceType',
            
            'y': 'y',
            
            'x': 'x',
            
            'label': 'label',
            
            'ip': 'ip',
            
            'nodeType': 'nodeType',
            
            'upperNode': 'upperNode',
            
            'fixed': 'fixed',
            
            'dataPathId': 'dataPathId'
            
        }       

        
        #Device custom parameters
        
        self.customParam = None # NodeWrapperCustom
        
        #Indicates if the device is active for this topology view
        
        self.greyOut = None # bool
        
        #List of tags applied on this device
        
        self.tags = None # list[str]
        
        #Indicates if the ACL that is applied on the device
        
        self.aclApplied = None # bool
        
        #Role of the device
        
        self.role = None # str
        
        #Device order by link number
        
        self.order = None # int
        
        #Unique identifier for device
        
        self.id = None # str
        
        #Indicates whether role is assigned manually or automatically
        
        self.roleSource = None # str
        
        #Product family which is part of the product identifier
        
        self.family = None # str
        
        #Device platform description
        
        self.platformId = None # str
        
        #Device OS version
        
        self.softwareVersion = None # str
        
        #ID of the host 
        
        self.userId = None # str
        
        #VLan id
        
        self.vlanId = None # str
        
        #OS type of the device
        
        self.osType = None # str
        
        #Type of network
        
        self.networkType = None # str
        
        #Type of the device
        
        self.deviceType = None # str
        
        #Y position of the device on the displayed topology view
        
        self.y = None # int
        
        #X position of the device on the displayed topology view
        
        self.x = None # int
        
        #Hostname of the device
        
        self.label = None # str
        
        #IP address of the device
        
        self.ip = None # str
        
        #Host or device
        
        self.nodeType = None # str
        
        #Start node ID
        
        self.upperNode = None # str
        
        #Indication of whether the position is fixed or will use auto layout 
        
        self.fixed = None # bool
        
        #ID of the path between devices
        
        self.dataPathId = None # str
        
