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

class FlowDTO(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'id': 'str',


            'protocol': 'str',


            'status': 'str',


            'codec': 'str',


            'sourcePort': 'str',


            'destPort': 'str',


            'flowType': 'str',


            'sourceIP': 'str',


            'destIP': 'str',


            'detailedFlowType': 'str',


            'averageBandwidth': 'str',


            'peakBandwidth': 'str',


            'clientReference': 'str',


            'networkDeviceId': 'str',


            'networkDeviceName': 'str',


            'interfaceId': 'str',


            'interfaceName': 'str',


            'failureReason': 'str'

        }

        self.attributeMap = {

            'id': 'id',

            'protocol': 'protocol',

            'status': 'status',

            'codec': 'codec',

            'sourcePort': 'sourcePort',

            'destPort': 'destPort',

            'flowType': 'flowType',

            'sourceIP': 'sourceIP',

            'destIP': 'destIP',

            'detailedFlowType': 'detailedFlowType',

            'averageBandwidth': 'averageBandwidth',

            'peakBandwidth': 'peakBandwidth',

            'clientReference': 'clientReference',

            'networkDeviceId': 'networkDeviceId',

            'networkDeviceName': 'networkDeviceName',

            'interfaceId': 'interfaceId',

            'interfaceName': 'interfaceName',

            'failureReason': 'failureReason'

        }


        #id

        self.id = None # str

        #protocol

        self.protocol = None # str


        self.status = None # str

        #codec

        self.codec = None # str

        #sourcePort

        self.sourcePort = None # str

        #destPort

        self.destPort = None # str

        #flowType

        self.flowType = None # str

        #sourceIP

        self.sourceIP = None # str

        #destIP

        self.destIP = None # str

        #detailedFlowType (more detailed classification than flowType)

        self.detailedFlowType = None # str

        #averageBandwidth in kbps (min: 0, max: 2147483647 kbps)

        self.averageBandwidth = None # str

        #peakBandwidth in kbps (min: 0, max: 2147483647 kbps)

        self.peakBandwidth = None # str

        #clientReference (can be used by the client as a reference to this resource

        self.clientReference = None # str

        #networkDeviceId

        self.networkDeviceId = None # str

        #networkDeviceName

        self.networkDeviceName = None # str

        #interfaceId

        self.interfaceId = None # str

        #interfaceName

        self.interfaceName = None # str


        self.failureReason = None # str

