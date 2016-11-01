#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class FileObject(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'id': 'str',
            
            
            'nameSpace': 'str',
            
            
            'encrypted': 'bool',
            
            
            'downloadPath': 'str',
            
            
            'fileFormat': 'str',
            
            
            'sha1Checksum': 'str',
            
            
            'fileSize': 'str',
            
            
            'md5Checksum': 'str',
            
            
            'name': 'str',
            
            
            'attributeInfo': 'dict'
            
        }

        self.attributeMap = {
            
            'id': 'id',
            
            'nameSpace': 'nameSpace',
            
            'encrypted': 'encrypted',
            
            'downloadPath': 'downloadPath',
            
            'fileFormat': 'fileFormat',
            
            'sha1Checksum': 'sha1Checksum',
            
            'fileSize': 'fileSize',
            
            'md5Checksum': 'md5Checksum',
            
            'name': 'name',
            
            'attributeInfo': 'attributeInfo'
            
        }       

        
        #file indentification number
        
        self.id = None # str
        
        #A group of file IDs contained in a common nameSpace
        
        self.nameSpace = None # str
        
        #isEncrypted of the file
        
        self.encrypted = None # bool
        
        #Absolute path of the file
        
        self.downloadPath = None # str
        
        #MIME Type of the File. e.g. text/plain, application/xml, audio/mpeg
        
        self.fileFormat = None # str
        
        #sha1Checksum of the file
        
        self.sha1Checksum = None # str
        
        #Size of the file in bytes
        
        self.fileSize = None # str
        
        #md5Checksum of the file
        
        self.md5Checksum = None # str
        
        #Name of the file
        
        self.name = None # str
        
        
        self.attributeInfo = None # dict
        
