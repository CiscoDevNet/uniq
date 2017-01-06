#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ZtdDefaultImage(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'imageName': 'str',
            
            
            'platformId': 'str',
            
            
            'imageId': 'str'
            
        }

        self.attributeMap = {
            
            'imageName': 'imageName',
            
            'platformId': 'platformId',
            
            'imageId': 'imageId'
            
        }       

        
        
        self.imageName = None # str
        
        
        self.platformId = None # str
        
        
        self.imageId = None # str
        
