#!/usr/bin/env python
#pylint: skip-file
"""
Copyright 2016 Cisco Systems

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

class IPGeoModel(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'latitude': 'str',


            'longitude': 'str',


            'city': 'str',


            'continent': 'str',


            'subDivision': 'str',


            'subDivisionCode': 'str',


            'countryCode': 'str',


            'continentCode': 'str',


            'country': 'str'

        }

        self.attributeMap = {

            'latitude': 'latitude',

            'longitude': 'longitude',

            'city': 'city',

            'continent': 'continent',

            'subDivision': 'subDivision',

            'subDivisionCode': 'subDivisionCode',

            'countryCode': 'countryCode',

            'continentCode': 'continentCode',

            'country': 'country'

        }



        self.latitude = None # str


        self.longitude = None # str


        self.city = None # str


        self.continent = None # str


        self.subDivision = None # str


        self.subDivisionCode = None # str


        self.countryCode = None # str


        self.continentCode = None # str


        self.country = None # str

