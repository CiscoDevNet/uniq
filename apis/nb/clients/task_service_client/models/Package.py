#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class Package(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'specificationTitle': 'str',
            
            
            'specificationVersion': 'str',
            
            
            'specificationVendor': 'str',
            
            
            'implementationTitle': 'str',
            
            
            'implementationVersion': 'str',
            
            
            'implementationVendor': 'str',
            
            
            'name': 'str',
            
            
            'annotations': 'list[Annotation]',
            
            
            'declaredAnnotations': 'list[Annotation]',
            
            
            'sealed': 'bool'
            
        }

        self.attributeMap = {
            
            'specificationTitle': 'specificationTitle',
            
            'specificationVersion': 'specificationVersion',
            
            'specificationVendor': 'specificationVendor',
            
            'implementationTitle': 'implementationTitle',
            
            'implementationVersion': 'implementationVersion',
            
            'implementationVendor': 'implementationVendor',
            
            'name': 'name',
            
            'annotations': 'annotations',
            
            'declaredAnnotations': 'declaredAnnotations',
            
            'sealed': 'sealed'
            
        }       

        
        
        self.specificationTitle = None # str
        
        
        self.specificationVersion = None # str
        
        
        self.specificationVendor = None # str
        
        
        self.implementationTitle = None # str
        
        
        self.implementationVersion = None # str
        
        
        self.implementationVendor = None # str
        
        
        self.name = None # str
        
        
        self.annotations = None # list[Annotation]
        
        
        self.declaredAnnotations = None # list[Annotation]
        
        
        self.sealed = None # bool
        
