#!/usr/bin/env python
#pylint: skip-file
"""
TicketApi.py
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
import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class TicketApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient



    def addTicket(self, **kwargs):
        """addTicket

        Args:

            user, User: user (required)



        Returns: TicketRbacResult
        """

        allParams = ['user']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addTicket" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ticket'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'










        if ('user' in params):
            bodyParam = params['user']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TicketRbacResult')
        return responseObject




    def createTicketAttribute(self, **kwargs):
        """createTicketAttribute

        Args:

            ticketAttribute, TicketAttribute: ticketAttribute (required)



        Returns: SuccessResult
        """

        allParams = ['ticketAttribute']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createTicketAttribute" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ticket/attribute'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'










        if ('ticketAttribute' in params):
            bodyParam = params['ticketAttribute']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SuccessResult')
        return responseObject




    def getIdleTimeout(self, **kwargs):
        """getIdleTimeout

        Args:


        Returns: TicketAttributeResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getIdleTimeout" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ticket/attribute/idletimeout'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'











        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TicketAttributeResult')
        return responseObject




    def getSessionTimeout(self, **kwargs):
        """getSessionTimeout

        Args:


        Returns: TicketAttributeResult
        """

        allParams = []

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getSessionTimeout" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ticket/attribute/sessiontimeout'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'











        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TicketAttributeResult')
        return responseObject




    def deleteTicketAttribute(self, **kwargs):
        """deleteTicketAttribute

        Args:

            attribute, str: attribute (required)



        Returns: SuccessResult
        """

        allParams = ['attribute']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteTicketAttribute" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ticket/attribute/{attribute}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('attribute' in params):
            replacement = str(self.apiClient.toPathValue(params['attribute']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'attribute' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SuccessResult')
        return responseObject




    def deleteTicket(self, **kwargs):
        """deleteTicket

        Args:

            ticket, str: ticket (required)



        Returns: SuccessResult
        """

        allParams = ['ticket']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteTicket" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ticket/{ticket}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('ticket' in params):
            replacement = str(self.apiClient.toPathValue(params['ticket']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'ticket' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SuccessResult')
        return responseObject






