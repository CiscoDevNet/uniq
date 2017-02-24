#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ServiceProviderProfileDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'classModels': 'list[ClassModelDTO]',
            
            
            'description': 'str',
            
            
            'name': 'str',
            
            
            'interfaces': 'list[ServiceProviderProfileInterfaceDTO]',
            
            
            'currentVersion': 'int',
            
            
            'vendor': 'str',
            
            
            'modelType': 'str',
            
            
            'defaultModel': 'bool',
            
            
            'id': 'str',
            
            
            'createTime': 'int',
            
            
            'lastUpdateTime': 'int'
            
        }

        self.attributeMap = {
            
            'classModels': 'classModels',
            
            'description': 'description',
            
            'name': 'name',
            
            'interfaces': 'interfaces',
            
            'currentVersion': 'currentVersion',
            
            'vendor': 'vendor',
            
            'modelType': 'modelType',
            
            'defaultModel': 'defaultModel',
            
            'id': 'id',
            
            'createTime': 'createTime',
            
            'lastUpdateTime': 'lastUpdateTime'
            
        }       

        
        #classModels list size should match the modelType
        
        self.classModels = None # list[ClassModelDTO]
        
        
        self.description = None # str
        
        #unique name for the ServiceProviderProfile
        
        self.name = None # str
        
        #read only details of interfaces on which the ServiceProviderProfile has been provisioned
        
        self.interfaces = None # list[ServiceProviderProfileInterfaceDTO]
        
        
        self.currentVersion = None # int
        
        
        self.vendor = None # str
        
        #Available options are: Three-Class, Four-Class, Five-Class, Six-Class, Eight-Class
        
        self.modelType = None # str
        
        #Read only attribute to indicate whether the ServiceProviderProfile is default(&#39;true&#39;) or custom(&#39;false&#39;)
        
        self.defaultModel = None # bool
        
        #id
        
        self.id = None # str
        
        #createTime
        
        self.createTime = None # int
        
        #lastUpdateTime
        
        self.lastUpdateTime = None # int
        
