#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class NetworkWideSettingsDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'netflow': 'NetflowSettingsDTO',
            
            
            'aaa': 'AAASettingsDTO',
            
            
            'dns': 'DNSSettingsDTO',
            
            
            'snmp': 'SNMPSettingsDTO',
            
            
            'dhcp': 'DHCPServerSettingsDTO',
            
            
            'systemSettingsDTO': 'SystemSettingsDTO',
            
            
            'hubSiteDTO': 'list[HubSiteDTO]',
            
            
            'errorHandleCondition': 'str',
            
            
            'ipAddressPoolWrapperDTO': 'IpAddressPoolWrapperDTO',
            
            
            'ldap': 'LDAPSettingsDTO',
            
            
            'syslog': 'list[SyslogSettingsDTO]',
            
            
            'ntp': 'NTPSettingsDTO',
            
            
            'ipPoolGlobalDTO': 'IpAddressGlobalDTO',
            
            
            'certifiedIOSRelease': 'list[CertifiedImageDTO]',
            
            
            'configurationType': 'str'
            
        }

        self.attributeMap = {
            
            'netflow': 'netflow',
            
            'aaa': 'aaa',
            
            'dns': 'dns',
            
            'snmp': 'snmp',
            
            'dhcp': 'dhcp',
            
            'systemSettingsDTO': 'systemSettingsDTO',
            
            'hubSiteDTO': 'hubSiteDTO',
            
            'errorHandleCondition': 'errorHandleCondition',
            
            'ipAddressPoolWrapperDTO': 'ipAddressPoolWrapperDTO',
            
            'ldap': 'ldap',
            
            'syslog': 'syslog',
            
            'ntp': 'ntp',
            
            'ipPoolGlobalDTO': 'ipPoolGlobalDTO',
            
            'certifiedIOSRelease': 'certifiedIOSRelease',
            
            'configurationType': 'configurationType'
            
        }       

        
        
        self.netflow = None # NetflowSettingsDTO
        
        
        self.aaa = None # AAASettingsDTO
        
        
        self.dns = None # DNSSettingsDTO
        
        
        self.snmp = None # SNMPSettingsDTO
        
        
        self.dhcp = None # DHCPServerSettingsDTO
        
        
        self.systemSettingsDTO = None # SystemSettingsDTO
        
        
        self.hubSiteDTO = None # list[HubSiteDTO]
        
        
        self.errorHandleCondition = None # str
        
        
        self.ipAddressPoolWrapperDTO = None # IpAddressPoolWrapperDTO
        
        
        self.ldap = None # LDAPSettingsDTO
        
        
        self.syslog = None # list[SyslogSettingsDTO]
        
        
        self.ntp = None # NTPSettingsDTO
        
        
        self.ipPoolGlobalDTO = None # IpAddressGlobalDTO
        
        
        self.certifiedIOSRelease = None # list[CertifiedImageDTO]
        
        
        self.configurationType = None # str
        
