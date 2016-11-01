#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class AugmentedAuditResourceDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'instanceUuid': 'str',
            
            
            'severity': 'str',
            
            
            'tag': 'str',
            
            
            'applicationName': 'str',
            
            
            'auditParameters': 'dict',
            
            
            'deviceIP': 'str',
            
            
            'auditDescription': 'str',
            
            
            'auditRequestor': 'str',
            
            
            'createdDateTime': 'date-time',
            
            
            'derivedParentId': 'str',
            
            
            'deviceName': 'str',
            
            
            'hasChildren': 'bool',
            
            
            'hasParent': 'bool',
            
            
            'persistDateTime': 'date-time',
            
            
            'siteName': 'str',
            
            
            'auditParentId': 'str',
            
            
            'auditId': 'str'
            
        }

        self.attributeMap = {
            
            'instanceUuid': 'instanceUuid',
            
            'severity': 'severity',
            
            'tag': 'tag',
            
            'applicationName': 'applicationName',
            
            'auditParameters': 'auditParameters',
            
            'deviceIP': 'deviceIP',
            
            'auditDescription': 'auditDescription',
            
            'auditRequestor': 'auditRequestor',
            
            'createdDateTime': 'createdDateTime',
            
            'derivedParentId': 'derivedParentId',
            
            'deviceName': 'deviceName',
            
            'hasChildren': 'hasChildren',
            
            'hasParent': 'hasParent',
            
            'persistDateTime': 'persistDateTime',
            
            'siteName': 'siteName',
            
            'auditParentId': 'auditParentId',
            
            'auditId': 'auditId'
            
        }       

        
        #This field is deprecated. Use &#39;id&#39; instead.
        
        self.instanceUuid = None # str
        
        
        self.severity = None # str
        
        
        self.tag = None # str
        
        
        self.applicationName = None # str
        
        
        self.auditParameters = None # dict
        
        
        self.deviceIP = None # str
        
        
        self.auditDescription = None # str
        
        
        self.auditRequestor = None # str
        
        
        self.createdDateTime = None # date-time
        
        
        self.derivedParentId = None # str
        
        
        self.deviceName = None # str
        
        
        self.hasChildren = None # bool
        
        
        self.hasParent = None # bool
        
        
        self.persistDateTime = None # date-time
        
        
        self.siteName = None # str
        
        
        self.auditParentId = None # str
        
        
        self.auditId = None # str
        
