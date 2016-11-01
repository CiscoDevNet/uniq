#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ScheduleInfoOutput(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'description': 'str',
            
            
            'startTime': 'date-time',
            
            
            'endTime': 'date-time',
            
            
            'origin': 'str',
            
            
            'operation': 'str',
            
            
            'taskId': 'str',
            
            
            'groupName': 'str',
            
            
            'scheduledWorkSpecId': 'str',
            
            
            'prevTime': 'date-time',
            
            
            'nextTime': 'date-time'
            
        }

        self.attributeMap = {
            
            'description': 'description',
            
            'startTime': 'startTime',
            
            'endTime': 'endTime',
            
            'origin': 'origin',
            
            'operation': 'operation',
            
            'taskId': 'taskId',
            
            'groupName': 'groupName',
            
            'scheduledWorkSpecId': 'scheduledWorkSpecId',
            
            'prevTime': 'prevTime',
            
            'nextTime': 'nextTime'
            
        }       

        
        #Simple description to be shown to end-users
        
        self.description = None # str
        
        #The time at which the trigger should first fire. If the schedule has fired and will not fire again, this value will be null
        
        self.startTime = None # date-time
        
        #The time at which the trigger should quit repeating
        
        self.endTime = None # date-time
        
        #Contextual field used to identify work spcifications originating from the same source
        
        self.origin = None # str
        
        #Contextual field used by the service to identify an operation
        
        self.operation = None # str
        
        #UUID of the Task
        
        self.taskId = None # str
        
        #A grouping name that can be specified by the service to allow for filtered work spec retrieval
        
        self.groupName = None # str
        
        #UUID of the ScheduledWorkSpec associated with the scheduled task
        
        self.scheduledWorkSpecId = None # str
        
        #The previous time at which the trigger fired. If the trigger has not yet fired, null will be returned
        
        self.prevTime = None # date-time
        
        #The next time at which the trigger should fire
        
        self.nextTime = None # date-time
        
