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
            
            'imageId': 'str',
            
            
            'imageName': 'str',
            
            
            'platform': 'list[ZtdPlatform]',
            
            
            'imageSize': 'str',
            
            
            'imageVersion': 'str'
            
        }

        self.attributeMap = {
            
            'imageId': 'imageId',
            
            'imageName': 'imageName',
            
            'platform': 'platform',
            
            'imageSize': 'imageSize',
            
            'imageVersion': 'imageVersion'
            
        }       

        
        #Image ID
        
        self.imageId = None # str
        
        #Image name
        
        self.imageName = None # str
        
        
        self.platform = None # list[ZtdPlatform]
        
        #Image size in bytes
        
        self.imageSize = None # str
        
        #Image version
        
        self.imageVersion = None # str
        
