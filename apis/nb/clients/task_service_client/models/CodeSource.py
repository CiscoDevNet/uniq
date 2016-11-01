#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class CodeSource(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'location': 'URL',
            
            
            'certificates': 'list[Certificate]',
            
            
            'codeSigners': 'list[CodeSigner]'
            
        }

        self.attributeMap = {
            
            'location': 'location',
            
            'certificates': 'certificates',
            
            'codeSigners': 'codeSigners'
            
        }       

        
        
        self.location = None # URL
        
        
        self.certificates = None # list[Certificate]
        
        
        self.codeSigners = None # list[CodeSigner]
        
