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
            
            
            'name': 'str',
            
            
            'interfaces': 'list[ServiceProviderProfileInterfaceDTO]',
            
            
            'description': 'str',
            
            
            'vendor': 'str',
            
            
            'currentVersion': 'int',
            
            
            'defaultModel': 'bool',
            
            
            'modelType': 'str',
            
            
            'id': 'str',
            
            
            'lastUpdateTime': 'int',
            
            
            'createTime': 'int'
            
        }

        self.attributeMap = {
            
            'classModels': 'classModels',
            
            'name': 'name',
            
            'interfaces': 'interfaces',
            
            'description': 'description',
            
            'vendor': 'vendor',
            
            'currentVersion': 'currentVersion',
            
            'defaultModel': 'defaultModel',
            
            'modelType': 'modelType',
            
            'id': 'id',
            
            'lastUpdateTime': 'lastUpdateTime',
            
            'createTime': 'createTime'
            
        }       

        
        #classModels list size should match the modelType
        
        self.classModels = None # list[ClassModelDTO]
        
        #unique name for the ServiceProviderProfile
        
        self.name = None # str
        
        #read only details of interfaces on which the ServiceProviderProfile has been provisioned
        
        self.interfaces = None # list[ServiceProviderProfileInterfaceDTO]
        
        
        self.description = None # str
        
        
        self.vendor = None # str
        
        
        self.currentVersion = None # int
        
        #Read only attribute to indicate whether the ServiceProviderProfile is default(&#39;true&#39;) or custom(&#39;false&#39;)
        
        self.defaultModel = None # bool
        
        #Available options are: Three-Class, Four-Class, Five-Class, Six-Class, Eight-Class
        
        self.modelType = None # str
        
        #id
        
        self.id = None # str
        
        #lastUpdateTime
        
        self.lastUpdateTime = None # int
        
        #createTime
        
        self.createTime = None # int
        
