#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class NodeWrapperCustom(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'parentNodeId': 'str',
            
            
            'y': 'int',
            
            
            'x': 'int',
            
            
            'label': 'str',
            
            
            'id': 'str'
            
        }

        self.attributeMap = {
            
            'parentNodeId': 'parentNodeId',
            
            'y': 'y',
            
            'x': 'x',
            
            'label': 'label',
            
            'id': 'id'
            
        }       

        
        #Unique Id of the Node for ehich the custom properties are being represented
        
        self.parentNodeId = None # str
        
        #Y - Coordinate for this Node in the topology View
        
        self.y = None # int
        
        #X - Coordinate for this Node in the topology View
        
        self.x = None # int
        
        #Label for the node
        
        self.label = None # str
        
        
        self.id = None # str
        
