#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ZtdPlatformImage(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'imageName': 'str',
            
            
            'imageId': 'str',
            
            
            'platform': 'list[ZtdPlatform]',
            
            
            'imageVersion': 'str',
            
            
            'imageSize': 'str'
            
        }

        self.attributeMap = {
            
            'imageName': 'imageName',
            
            'imageId': 'imageId',
            
            'platform': 'platform',
            
            'imageVersion': 'imageVersion',
            
            'imageSize': 'imageSize'
            
        }       

        
        #Image name
        
        self.imageName = None # str
        
        #Image ID
        
        self.imageId = None # str
        
        
        self.platform = None # list[ZtdPlatform]
        
        #Image version
        
        self.imageVersion = None # str
        
        #Image size in bytes
        
        self.imageSize = None # str
        
