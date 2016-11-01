#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class URL(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'path': 'str',
            
            
            'authority': 'str',
            
            
            'query': 'str',
            
            
            'protocol': 'str',
            
            
            'file': 'str',
            
            
            'host': 'str',
            
            
            'ref': 'str',
            
            
            'userInfo': 'str',
            
            
            'port': 'int',
            
            
            'defaultPort': 'int',
            
            
            'content': 'dict'
            
        }

        self.attributeMap = {
            
            'path': 'path',
            
            'authority': 'authority',
            
            'query': 'query',
            
            'protocol': 'protocol',
            
            'file': 'file',
            
            'host': 'host',
            
            'ref': 'ref',
            
            'userInfo': 'userInfo',
            
            'port': 'port',
            
            'defaultPort': 'defaultPort',
            
            'content': 'content'
            
        }       

        
        
        self.path = None # str
        
        
        self.authority = None # str
        
        
        self.query = None # str
        
        
        self.protocol = None # str
        
        
        self.file = None # str
        
        
        self.host = None # str
        
        
        self.ref = None # str
        
        
        self.userInfo = None # str
        
        
        self.port = None # int
        
        
        self.defaultPort = None # int
        
        
        self.content = None # dict
        
