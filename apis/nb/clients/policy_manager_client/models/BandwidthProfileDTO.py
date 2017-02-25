#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class BandwidthProfileDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'defaultProfile': 'bool',
            
            
            'interfaceTrafficClassBandwidthSettingsList': 'list[InterfaceTrafficClassBandwidthSettingsDTO]',
            
            
            'bandwidthProfileAssociatedPolicyScopes': 'list[BandwidthProfileAssociatedPolicyScopeDTO]',
            
            
            'version': 'int',
            
            
            'description': 'str',
            
            
            'name': 'str',
            
            
            'id': 'str',
            
            
            'createTime': 'int',
            
            
            'lastUpdateTime': 'int'
            
        }

        self.attributeMap = {
            
            'defaultProfile': 'defaultProfile',
            
            'interfaceTrafficClassBandwidthSettingsList': 'interfaceTrafficClassBandwidthSettingsList',
            
            'bandwidthProfileAssociatedPolicyScopes': 'bandwidthProfileAssociatedPolicyScopes',
            
            'version': 'version',
            
            'description': 'description',
            
            'name': 'name',
            
            'id': 'id',
            
            'createTime': 'createTime',
            
            'lastUpdateTime': 'lastUpdateTime'
            
        }       

        
        #A flag to indicate if the BandwidthProfile is a default/user-defined one
        
        self.defaultProfile = None # bool
        
        #List of Traffic Class Bandwidth Settings for the different interface speeds supported
        
        self.interfaceTrafficClassBandwidthSettingsList = None # list[InterfaceTrafficClassBandwidthSettingsDTO]
        
        #read only list of policy scopes using the BandwidthProfile
        
        self.bandwidthProfileAssociatedPolicyScopes = None # list[BandwidthProfileAssociatedPolicyScopeDTO]
        
        #Incremental number representing the version of the BandwidthProfile
        
        self.version = None # int
        
        #Description for the BandwidthProfile
        
        self.description = None # str
        
        #unique name for the BandwidthProfile
        
        self.name = None # str
        
        #id
        
        self.id = None # str
        
        #createTime
        
        self.createTime = None # int
        
        #lastUpdateTime
        
        self.lastUpdateTime = None # int
        
