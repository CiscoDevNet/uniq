#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class AlarmDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'causedAlarmsUrl': 'str',
            
            
            'causingAlarmUrl': 'str',
            
            
            'alarmCreationTime': 'date-time',
            
            
            'applicationSpecificAlarmID': 'str',
            
            
            'eventCount': 'int',
            
            
            'isAcknowledged': 'bool',
            
            
            'lastModifiedTimestamp': 'date-time',
            
            
            'mayBeAutoCleared': 'bool',
            
            
            'ownerID': 'str',
            
            
            'previousSeverity': 'str',
            
            
            'subclassName': 'str',
            
            
            'causedAlarms': 'list[IdRef]',
            
            
            'causingAlarm': 'IdRef',
            
            
            'eventType': 'EventTypeEnum',
            
            
            'description': 'str',
            
            
            'severity': 'str',
            
            
            'source': 'str',
            
            
            'category': 'EventAlarmCategoryEnum',
            
            
            'sourceMacAddress': 'MacAddress',
            
            
            'srcObjectClassId': 'int',
            
            
            'srcObjectId': 'int',
            
            
            'stability': 'str',
            
            
            'transientNameValue': 'dict',
            
            
            'eventAlarmDetails': 'list[IdRef]',
            
            
            'alarmDisplayable': 'bool',
            
            
            'applicationCategoryData': 'str',
            
            
            'deviceTimestamp': 'date-time',
            
            
            'isDeviceMaster': 'bool',
            
            
            'notificationDeliveryMechanism': 'str',
            
            
            'notificationState': 'int',
            
            
            'pendingUntil': 'date-time',
            
            
            'reportingEntityAddress': 'InetAddress',
            
            
            'eventAlarmDetailsUrl': 'str',
            
            
            'instanceUuid': 'str',
            
            
            'id': 'str'
            
        }

        self.attributeMap = {
            
            'causedAlarmsUrl': 'causedAlarmsUrl',
            
            'causingAlarmUrl': 'causingAlarmUrl',
            
            'alarmCreationTime': 'alarmCreationTime',
            
            'applicationSpecificAlarmID': 'applicationSpecificAlarmID',
            
            'eventCount': 'eventCount',
            
            'isAcknowledged': 'isAcknowledged',
            
            'lastModifiedTimestamp': 'lastModifiedTimestamp',
            
            'mayBeAutoCleared': 'mayBeAutoCleared',
            
            'ownerID': 'ownerID',
            
            'previousSeverity': 'previousSeverity',
            
            'subclassName': 'subclassName',
            
            'causedAlarms': 'causedAlarms',
            
            'causingAlarm': 'causingAlarm',
            
            'eventType': 'eventType',
            
            'description': 'description',
            
            'severity': 'severity',
            
            'source': 'source',
            
            'category': 'category',
            
            'sourceMacAddress': 'sourceMacAddress',
            
            'srcObjectClassId': 'srcObjectClassId',
            
            'srcObjectId': 'srcObjectId',
            
            'stability': 'stability',
            
            'transientNameValue': 'transientNameValue',
            
            'eventAlarmDetails': 'eventAlarmDetails',
            
            'alarmDisplayable': 'alarmDisplayable',
            
            'applicationCategoryData': 'applicationCategoryData',
            
            'deviceTimestamp': 'deviceTimestamp',
            
            'isDeviceMaster': 'isDeviceMaster',
            
            'notificationDeliveryMechanism': 'notificationDeliveryMechanism',
            
            'notificationState': 'notificationState',
            
            'pendingUntil': 'pendingUntil',
            
            'reportingEntityAddress': 'reportingEntityAddress',
            
            'eventAlarmDetailsUrl': 'eventAlarmDetailsUrl',
            
            'instanceUuid': 'instanceUuid',
            
            'id': 'id'
            
        }       

        
        
        self.causedAlarmsUrl = None # str
        
        
        self.causingAlarmUrl = None # str
        
        
        self.alarmCreationTime = None # date-time
        
        
        self.applicationSpecificAlarmID = None # str
        
        
        self.eventCount = None # int
        
        
        self.isAcknowledged = None # bool
        
        
        self.lastModifiedTimestamp = None # date-time
        
        
        self.mayBeAutoCleared = None # bool
        
        
        self.ownerID = None # str
        
        
        self.previousSeverity = None # str
        
        
        self.subclassName = None # str
        
        
        self.causedAlarms = None # list[IdRef]
        
        
        self.causingAlarm = None # IdRef
        
        
        self.eventType = None # EventTypeEnum
        
        
        self.description = None # str
        
        
        self.severity = None # str
        
        
        self.source = None # str
        
        
        self.category = None # EventAlarmCategoryEnum
        
        
        self.sourceMacAddress = None # MacAddress
        
        
        self.srcObjectClassId = None # int
        
        
        self.srcObjectId = None # int
        
        
        self.stability = None # str
        
        
        self.transientNameValue = None # dict
        
        
        self.eventAlarmDetails = None # list[IdRef]
        
        
        self.alarmDisplayable = None # bool
        
        
        self.applicationCategoryData = None # str
        
        
        self.deviceTimestamp = None # date-time
        
        
        self.isDeviceMaster = None # bool
        
        
        self.notificationDeliveryMechanism = None # str
        
        
        self.notificationState = None # int
        
        
        self.pendingUntil = None # date-time
        
        
        self.reportingEntityAddress = None # InetAddress
        
        
        self.eventAlarmDetailsUrl = None # str
        
        
        self.instanceUuid = None # str
        
        
        self.id = None # str
        
