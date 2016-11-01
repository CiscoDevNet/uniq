#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class SystemSettingsDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'id': 'str',
            
            
            'snmp': 'SNMPSettingsDTO',
            
            
            'ntp': 'NTPSettingsDTO',
            
            
            'aaa': 'AAASettingsDTO',
            
            
            'dns': 'DNSSettingsDTO',
            
            
            'netflow': 'NetflowSettingsDTO',
            
            
            'ldap': 'LDAPSettingsDTO',
            
            
            'syslog': 'list[SyslogSettingsDTO]',
            
            
            'dhcp': 'DHCPServerSettingsDTO',
            
            
            'certifiedIOSRelease': 'list[CertifiedImageDTO]'
            
        }

        self.attributeMap = {
            
            'id': 'id',
            
            'snmp': 'snmp',
            
            'ntp': 'ntp',
            
            'aaa': 'aaa',
            
            'dns': 'dns',
            
            'netflow': 'netflow',
            
            'ldap': 'ldap',
            
            'syslog': 'syslog',
            
            'dhcp': 'dhcp',
            
            'certifiedIOSRelease': 'certifiedIOSRelease'
            
        }       

        
        
        self.id = None # str
        
        
        self.snmp = None # SNMPSettingsDTO
        
        
        self.ntp = None # NTPSettingsDTO
        
        
        self.aaa = None # AAASettingsDTO
        
        
        self.dns = None # DNSSettingsDTO
        
        
        self.netflow = None # NetflowSettingsDTO
        
        
        self.ldap = None # LDAPSettingsDTO
        
        
        self.syslog = None # list[SyslogSettingsDTO]
        
        
        self.dhcp = None # DHCPServerSettingsDTO
        
        
        self.certifiedIOSRelease = None # list[CertifiedImageDTO]
        
