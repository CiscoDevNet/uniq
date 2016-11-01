#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ZtdPlatformImageList(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'images': 'list[ZtdPlatformImage]',


            'attributeInfo': 'object',


            'id': 'str'

        }

        self.attributeMap = {

            'images': 'images',

            'attributeInfo': 'attributeInfo',

            'id': 'id'

        }



        self.images = None # list[ZtdPlatformImage]


        self.attributeInfo = None # object


        self.id = None # str

