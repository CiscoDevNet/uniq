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

class ManualLinkDTO(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'isAManaged': 'bool',


            'isBManaged': 'bool',


            'type': 'str',


            'category': 'str',


            'linkStatus': 'str',


            'compositeType': 'str',


            'isManuallyAdded': 'bool',


            'linkCapacity': 'LongQuantity',


            'virSwitchUuid': 'str',


            'aggregatedLinks': 'list[IdRef]',


            'aggregatingLink': 'IdRef',


            'composingNetworkClouds': 'list[IdRef]',


            'forwardingRelationships': 'list[IdRef]',


            'linkTerminationPoints': 'list[IdRef]',


            'aggregatedLinksUrl': 'str',


            'aggregatingLinkUrl': 'str',


            'composingNetworkCloudsUrl': 'str',


            'forwardingRelationshipsUrl': 'str',


            'linkTerminationPointsUrl': 'str',


            'name': 'str',


            'description': 'str',


            'owningEntityId': 'str',


            'instanceUuid': 'str'

        }

        self.attributeMap = {

            'isAManaged': 'isAManaged',

            'isBManaged': 'isBManaged',

            'type': 'type',

            'category': 'category',

            'linkStatus': 'linkStatus',

            'compositeType': 'compositeType',

            'isManuallyAdded': 'isManuallyAdded',

            'linkCapacity': 'linkCapacity',

            'virSwitchUuid': 'virSwitchUuid',

            'aggregatedLinks': 'aggregatedLinks',

            'aggregatingLink': 'aggregatingLink',

            'composingNetworkClouds': 'composingNetworkClouds',

            'forwardingRelationships': 'forwardingRelationships',

            'linkTerminationPoints': 'linkTerminationPoints',

            'aggregatedLinksUrl': 'aggregatedLinksUrl',

            'aggregatingLinkUrl': 'aggregatingLinkUrl',

            'composingNetworkCloudsUrl': 'composingNetworkCloudsUrl',

            'forwardingRelationshipsUrl': 'forwardingRelationshipsUrl',

            'linkTerminationPointsUrl': 'linkTerminationPointsUrl',

            'name': 'name',

            'description': 'description',

            'owningEntityId': 'owningEntityId',

            'instanceUuid': 'instanceUuid'

        }



        self.isAManaged = None # bool


        self.isBManaged = None # bool


        self.type = None # str


        self.category = None # str


        self.linkStatus = None # str


        self.compositeType = None # str


        self.isManuallyAdded = None # bool


        self.linkCapacity = None # LongQuantity


        self.virSwitchUuid = None # str


        self.aggregatedLinks = None # list[IdRef]


        self.aggregatingLink = None # IdRef


        self.composingNetworkClouds = None # list[IdRef]


        self.forwardingRelationships = None # list[IdRef]


        self.linkTerminationPoints = None # list[IdRef]


        self.aggregatedLinksUrl = None # str


        self.aggregatingLinkUrl = None # str


        self.composingNetworkCloudsUrl = None # str


        self.forwardingRelationshipsUrl = None # str


        self.linkTerminationPointsUrl = None # str


        self.name = None # str


        self.description = None # str


        self.owningEntityId = None # str


        self.instanceUuid = None # str

