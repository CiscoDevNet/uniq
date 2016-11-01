#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class AutoPassphrase(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'autoPassphrase': 'str'
            
        }

        self.attributeMap = {
            
            'autoPassphrase': 'autoPassphrase'
            
        }       

        
        #Auto generated passphrase
        
        self.autoPassphrase = None # str
        
