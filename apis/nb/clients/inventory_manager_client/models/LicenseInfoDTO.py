#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class LicenseInfoDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'name': 'str',
            
            
            'priority': 'str',
            
            
            'type': 'str',
            
            
            'description': 'str',
            
            
            'validityPeriodRemaining': 'int',
            
            
            'maxUsageCount': 'int',
            
            
            'eulaStatus': 'bool',
            
            
            'validityPeriod': 'int',
            
            
            'usageCount': 'int',
            
            
            'physicalIndex': 'str',
            
            
            'licenseIndex': 'int',
            
            
            'featureVersion': 'str',
            
            
            'counted': 'bool',
            
            
            'totalCount': 'int',
            
            
            'provisionState': 'int',
            
            
            'parentId': 'int',
            
            
            'expiredPeriod': 'int',
            
            
            'usageCountRemaining': 'int',
            
            
            'status': 'str',
            
            
            'id': 'str',
            
            
            'deployPending': 'int',
            
            
            'hostId': 'str',
            
            
            'evalPeriodLeft': 'str',
            
            
            'evalPeriodUsed': 'str',
            
            
            'expiredDate': 'str',
            
            
            'isCounted': 'bool',
            
            
            'isEulaAccepted': 'bool',
            
            
            'isEulaApplicable': 'bool',
            
            
            'isTechnologyLicense': 'bool',
            
            
            'licenseFileCount': 'int',
            
            
            'licenseFileName': 'str',
            
            
            'storeName': 'str',
            
            
            'storedUsed': 'int',
            
            
            'attributeInfo': 'dict'
            
        }

        self.attributeMap = {
            
            'name': 'name',
            
            'priority': 'priority',
            
            'type': 'type',
            
            'description': 'description',
            
            'validityPeriodRemaining': 'validityPeriodRemaining',
            
            'maxUsageCount': 'maxUsageCount',
            
            'eulaStatus': 'eulaStatus',
            
            'validityPeriod': 'validityPeriod',
            
            'usageCount': 'usageCount',
            
            'physicalIndex': 'physicalIndex',
            
            'licenseIndex': 'licenseIndex',
            
            'featureVersion': 'featureVersion',
            
            'counted': 'counted',
            
            'totalCount': 'totalCount',
            
            'provisionState': 'provisionState',
            
            'parentId': 'parentId',
            
            'expiredPeriod': 'expiredPeriod',
            
            'usageCountRemaining': 'usageCountRemaining',
            
            'status': 'status',
            
            'id': 'id',
            
            'deployPending': 'deployPending',
            
            'hostId': 'hostId',
            
            'evalPeriodLeft': 'evalPeriodLeft',
            
            'evalPeriodUsed': 'evalPeriodUsed',
            
            'expiredDate': 'expiredDate',
            
            'isCounted': 'isCounted',
            
            'isEulaAccepted': 'isEulaAccepted',
            
            'isEulaApplicable': 'isEulaApplicable',
            
            'isTechnologyLicense': 'isTechnologyLicense',
            
            'licenseFileCount': 'licenseFileCount',
            
            'licenseFileName': 'licenseFileName',
            
            'storeName': 'storeName',
            
            'storedUsed': 'storedUsed',
            
            'attributeInfo': 'attributeInfo'
            
        }       

        
        #Name of the feature that is using or can use this license. Ex: &#39;IPBASE&#39;, &#39;ADVIPSERVICE&#39;
        
        self.name = None # str
        
        #License priority
        
        self.priority = None # str
        
        #Type of license based on the validity period
        
        self.type = None # str
        
        #Description about the license. It is populated  with comments from the license file
        
        self.description = None # str
        
        #Time period remaining before the license expires or transitions to rightToUse(9) license. Value will be in milliseconds
        
        self.validityPeriodRemaining = None # int
        
        #Maximum number of entities that can use this license
        
        self.maxUsageCount = None # int
        
        #Whether the user accepted end user license agreement for this license. Values are true(1)  - EULA accepted, false(2) - EULA not accepted
        
        self.eulaStatus = None # bool
        
        #Time period the license is valid for. Value will be in milliseconds
        
        self.validityPeriod = None # int
        
        #Number of current usages of this licensed feature
        
        self.usageCount = None # int
        
        #Physical entity index
        
        self.physicalIndex = None # str
        
        #Index of the license to uniquely identify a license within the device
        
        self.licenseIndex = None # int
        
        #Version of the feature that is using or can use this license. Ex: &#39;1.0&#39;, &#39;2.0&#39; 
        
        self.featureVersion = None # str
        
        #If license feature is counted as part of the license. Values are true(1)  - counted license, false(2) - uncounted license
        
        self.counted = None # bool
        
        #Total number of this licensed feature
        
        self.totalCount = None # int
        
        #Provision state of the license feature
        
        self.provisionState = None # int
        
        #Parent Id of the license
        
        self.parentId = None # int
        
        #Time period after the license expires. Value will be in milliseconds
        
        self.expiredPeriod = None # int
        
        #Number of entities that can still use this license
        
        self.usageCountRemaining = None # int
        
        #Status of the license
        
        self.status = None # str
        
        #Id of the license
        
        self.id = None # str
        
        #Deploy Pending information of license
        
        self.deployPending = None # int
        
        #An administratively-assigned fully-qualified domain name for this managed node
        
        self.hostId = None # str
        
        #Number of days remaining in the eval period
        
        self.evalPeriodLeft = None # str
        
        #Number of days used in the eval period
        
        self.evalPeriodUsed = None # str
        
        #Expired date of the license
        
        self.expiredDate = None # str
        
        #Whether the license is counted license. Values are true(1)  - counted license,false(2) - uncounted license
        
        self.isCounted = None # bool
        
        #This field is based on eulaStatus. Ex: If eulaStatus is true then it will be accepted else false
        
        self.isEulaAccepted = None # bool
        
        #This field is based on eulaStatus. Ex: If eulaStatus is true then it will be applicable else false
        
        self.isEulaApplicable = None # bool
        
        #Whether the license is technology license. Values are true(1)  - technology license,false(2) - nontechnology license
        
        self.isTechnologyLicense = None # bool
        
        #Number of installed license file in this feature
        
        self.licenseFileCount = None # int
        
        #Installed License file name
        
        self.licenseFileName = None # str
        
        #Name of the license store within the device. Ex: &#39;disk1:lic_store_1.txt&#39; or  &#39;flash:lic_store_2.txt
        
        self.storeName = None # str
        
        #License store that is used for storing this license
        
        self.storedUsed = None # int
        
        
        self.attributeInfo = None # dict
        
