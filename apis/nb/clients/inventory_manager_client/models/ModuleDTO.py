#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ModuleDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'isFieldReplaceable': 'str',
            
            
            'entityPhysicalIndex': 'str',
            
            
            'containmentEntity': 'str',
            
            
            'name': 'str',
            
            
            'serialNumber': 'str',
            
            
            'description': 'str',
            
            
            'assemblyNumber': 'str',
            
            
            'assemblyRevision': 'str',
            
            
            'isReportingAlarmsAllowed': 'str',
            
            
            'manufacturer': 'str',
            
            
            'operationalStateCode': 'str',
            
            
            'partNumber': 'str',
            
            
            'vendorEquipmentType': 'str',
            
            
            'id': 'str',
            
            
            'moduleIndex': 'int',
            
            
            'attributeInfo': 'dict'
            
        }

        self.attributeMap = {
            
            'isFieldReplaceable': 'isFieldReplaceable',
            
            'entityPhysicalIndex': 'entityPhysicalIndex',
            
            'containmentEntity': 'containmentEntity',
            
            'name': 'name',
            
            'serialNumber': 'serialNumber',
            
            'description': 'description',
            
            'assemblyNumber': 'assemblyNumber',
            
            'assemblyRevision': 'assemblyRevision',
            
            'isReportingAlarmsAllowed': 'isReportingAlarmsAllowed',
            
            'manufacturer': 'manufacturer',
            
            'operationalStateCode': 'operationalStateCode',
            
            'partNumber': 'partNumber',
            
            'vendorEquipmentType': 'vendorEquipmentType',
            
            'id': 'id',
            
            'moduleIndex': 'moduleIndex',
            
            'attributeInfo': 'attributeInfo'
            
        }       

        
        #To mention if field is replaceable
        
        self.isFieldReplaceable = None # str
        
        #Entity physical index of the module
        
        self.entityPhysicalIndex = None # str
        
        #Containment entity of the module
        
        self.containmentEntity = None # str
        
        #Name of the module
        
        self.name = None # str
        
        #Serial number of the module
        
        self.serialNumber = None # str
        
        #Description of the module
        
        self.description = None # str
        
        #Assembly number of the module
        
        self.assemblyNumber = None # str
        
        #Assembly revision of the module
        
        self.assemblyRevision = None # str
        
        #To mention if reporting alarms are allowed
        
        self.isReportingAlarmsAllowed = None # str
        
        #Manufacturer of the module
        
        self.manufacturer = None # str
        
        #Operational state of the module
        
        self.operationalStateCode = None # str
        
        #Part number of the module
        
        self.partNumber = None # str
        
        #Vendor euipment type of the module
        
        self.vendorEquipmentType = None # str
        
        #Id of the module
        
        self.id = None # str
        
        #Index of the module
        
        self.moduleIndex = None # int
        
        
        self.attributeInfo = None # dict
        
