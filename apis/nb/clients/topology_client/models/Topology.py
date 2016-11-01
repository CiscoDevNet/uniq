#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class Topology(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'links': 'list[LinkWrapper]',
            
            
            'nodes': 'list[NodeWrapper]',
            
            
            'id': 'str'
            
        }

        self.attributeMap = {
            
            'links': 'links',
            
            'nodes': 'nodes',
            
            'id': 'id'
            
        }       

        
        #List of link between devices
        
        self.links = None # list[LinkWrapper]
        
        #List of devices and hosts
        
        self.nodes = None # list[NodeWrapper]
        
        
        self.id = None # str
        
