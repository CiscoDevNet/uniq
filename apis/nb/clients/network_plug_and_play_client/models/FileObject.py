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
            
            'encrypted': 'bool',
            
            
            'id': 'str',
            
            
            'fileSize': 'str',
            
            
            'nameSpace': 'str',
            
            
            'fileFormat': 'str',
            
            
            'sha1Checksum': 'str',
            
            
            'md5Checksum': 'str',
            
            
            'downloadPath': 'str',
            
            
            'name': 'str',
            
            
            'attributeInfo': 'dict'
            
        }

        self.attributeMap = {
            
            'encrypted': 'encrypted',
            
            'id': 'id',
            
            'fileSize': 'fileSize',
            
            'nameSpace': 'nameSpace',
            
            'fileFormat': 'fileFormat',
            
            'sha1Checksum': 'sha1Checksum',
            
            'md5Checksum': 'md5Checksum',
            
            'downloadPath': 'downloadPath',
            
            'name': 'name',
            
            'attributeInfo': 'attributeInfo'
            
        }       

        
        #isEncrypted of the file
        
        self.encrypted = None # bool
        
        #file indentification number
        
        self.id = None # str
        
        #Size of the file in bytes
        
        self.fileSize = None # str
        
        #A group of file IDs contained in a common nameSpace
        
        self.nameSpace = None # str
        
        #MIME Type of the File. e.g. text/plain, application/xml, audio/mpeg
        
        self.fileFormat = None # str
        
        #sha1Checksum of the file
        
        self.sha1Checksum = None # str
        
        #md5Checksum of the file
        
        self.md5Checksum = None # str
        
        #Absolute path of the file
        
        self.downloadPath = None # str
        
        #Name of the file
        
        self.name = None # str
        
        
        self.attributeInfo = None # dict
        
