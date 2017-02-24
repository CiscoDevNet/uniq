#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ActionProperty(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'bandwidthProfileId': 'str',
            
            
            'priorityLevel': 'str',
            
            
            'experienceLevel': 'str',
            
            
            'destinations': 'list[str]',
            
            
            'pathPreference': 'str',
            
            
            'maintainExperience': 'str',
            
            
            'trustLevel': 'str',
            
            
            'pathControlFlag': 'bool',
            
            
            'pathPreferenceFlag': 'bool',
            
            
            'PrimaryPathPref': 'list[str]',
            
            
            'SecondaryPathPref': 'list[str]',
            
            
            'PathOfLastResort': 'str',
            
            
            'TertiaryPathPref': 'list[str]',
            
            
            'relevanceLevel': 'str'
            
        }

        self.attributeMap = {
            
            'bandwidthProfileId': 'bandwidthProfileId',
            
            'priorityLevel': 'priorityLevel',
            
            'experienceLevel': 'experienceLevel',
            
            'destinations': 'destinations',
            
            'pathPreference': 'pathPreference',
            
            'maintainExperience': 'maintainExperience',
            
            'trustLevel': 'trustLevel',
            
            'pathControlFlag': 'pathControlFlag',
            
            'pathPreferenceFlag': 'pathPreferenceFlag',
            
            'PrimaryPathPref': 'PrimaryPathPref',
            
            'SecondaryPathPref': 'SecondaryPathPref',
            
            'PathOfLastResort': 'PathOfLastResort',
            
            'TertiaryPathPref': 'TertiaryPathPref',
            
            'relevanceLevel': 'relevanceLevel'
            
        }       

        
        #ID of the bandwidth profile
        
        self.bandwidthProfileId = None # str
        
        #priority level for a policy
        
        self.priorityLevel = None # str
        
        #experience level for a policy
        
        self.experienceLevel = None # str
        
        
        self.destinations = None # list[str]
        
        #path preference for a policy
        
        self.pathPreference = None # str
        
        
        self.maintainExperience = None # str
        
        #trust level for a policy
        
        self.trustLevel = None # str
        
        #path control flag
        
        self.pathControlFlag = None # bool
        
        #path preference flag
        
        self.pathPreferenceFlag = None # bool
        
        
        self.PrimaryPathPref = None # list[str]
        
        
        self.SecondaryPathPref = None # list[str]
        
        
        self.PathOfLastResort = None # str
        
        
        self.TertiaryPathPref = None # list[str]
        
        #relevance level for a policy
        
        self.relevanceLevel = None # str
        
