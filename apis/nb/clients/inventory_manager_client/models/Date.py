#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class Date(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'time': 'int',
            
            
            'hours': 'int',
            
            
            'minutes': 'int',
            
            
            'seconds': 'int',
            
            
            'year': 'int',
            
            
            'month': 'int',
            
            
            'date': 'int'
            
        }

        self.attributeMap = {
            
            'time': 'time',
            
            'hours': 'hours',
            
            'minutes': 'minutes',
            
            'seconds': 'seconds',
            
            'year': 'year',
            
            'month': 'month',
            
            'date': 'date'
            
        }       

        
        
        self.time = None # int
        
        
        self.hours = None # int
        
        
        self.minutes = None # int
        
        
        self.seconds = None # int
        
        
        self.year = None # int
        
        
        self.month = None # int
        
        
        self.date = None # int
        
