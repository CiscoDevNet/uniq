#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class PnpfileApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def getConfigs(self, **kwargs):
        """Retrieves a list of config records

        Args:
            
            offset, int: Starting index of the response. Minimum value is 1 (required)
            
            
            limit, int: Limit the number of responses. Maximum value supported is 500. Minimum value is 1 (required)
            
            
            name, str: File name pattern (required)
            
            
            extension, str: Ext. txt, json, gen, vm. Use \&quot;\&quot; for no extension.  Accepts a list of extensions. (required)
            
            
            matchExtension, bool: Match extension. Boolean to match the given extension (true) or not (false) (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: FileObjectListResult
        """

        allParams = ['offset', 'limit', 'name', 'extension', 'matchExtension', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getConfigs" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-file/config'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])
        
        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])
        
        if ('name' in params):
            queryParams['name'] = self.apiClient.toPathValue(params['name'])
        
        if ('extension' in params):
            queryParams['extension'] = self.apiClient.toPathValue(params['extension'])
        
        if ('matchExtension' in params):
            queryParams['matchExtension'] = self.apiClient.toPathValue(params['matchExtension'])
        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'FileObjectListResult')
        return responseObject
        
        
        
    
    def getConfigCount(self, **kwargs):
        """Returns number of CLI config files

        Args:
            
            name, str: File name pattern (required)
            
            
            extension, str: Ext. txt, json, gen, vm. Use \&quot;\&quot; for no extension.  Accepts a list of extensions. (required)
            
            
            matchExtension, bool: Match extension. Boolean to match the given extension (true) or not (false) (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: str
        """

        allParams = ['name', 'extension', 'matchExtension', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getConfigCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-file/config/count'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('name' in params):
            queryParams['name'] = self.apiClient.toPathValue(params['name'])
        
        if ('extension' in params):
            queryParams['extension'] = self.apiClient.toPathValue(params['extension'])
        
        if ('matchExtension' in params):
            queryParams['matchExtension'] = self.apiClient.toPathValue(params['matchExtension'])
        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    
    def deleteConfigById(self, **kwargs):
        """Deletes a configuration with its ID

        Args:
            
            configId, str: Config ID (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['configId', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteConfigById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-file/config/{configId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        
        if ('configId' in params):
            replacement = str(self.apiClient.toPathValue(params['configId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'configId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getPnpImageBySearch(self, **kwargs):
        """Retrieves a list of images and the platforms for which they are a default

        Args:
            
            name, str: Image name (required)
            
            
            platform, str: Platform name (required)
            
            
            productId, str: Product ID (required)
            
            
            match, str: Match all or any parameters (required)
            
            
            order, str: Order response in ascending (asc) or descending (des) order of image name. (required)
            
            
            offset, int: Starting index of the response. Minimum value is 1 (required)
            
            
            limit, int: Limit the number of responses. Maximum value supported is 500. Minimum value is 1 (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: ZtdPlatformImageListResult
        """

        allParams = ['name', 'platform', 'productId', 'match', 'order', 'offset', 'limit', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPnpImageBySearch" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-file/image'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('name' in params):
            queryParams['name'] = self.apiClient.toPathValue(params['name'])
        
        if ('platform' in params):
            queryParams['platform'] = self.apiClient.toPathValue(params['platform'])
        
        if ('productId' in params):
            queryParams['productId'] = self.apiClient.toPathValue(params['productId'])
        
        if ('match' in params):
            queryParams['match'] = self.apiClient.toPathValue(params['match'])
        
        if ('order' in params):
            queryParams['order'] = self.apiClient.toPathValue(params['order'])
        
        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])
        
        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])
        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ZtdPlatformImageListResult')
        return responseObject
        
        
        
    
    def updatePnpImageDetails(self, **kwargs):
        """Updates an image and the platforms for which it is default with its ID

        Args:
            
            image, list[ZtdPlatformImage]: PnP Image (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['image', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updatePnpImageDetails" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-file/image'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        

        

        
        if ('image' in params):
            bodyParam = params['image']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getPnpImageBySearchCount(self, **kwargs):
        """Retrieves a count of images

        Args:
            
            name, str: Image name (required)
            
            
            platform, str: Platform name (required)
            
            
            productId, str: Product ID (required)
            
            
            match, str: Match all or any parameters (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: str
        """

        allParams = ['name', 'platform', 'productId', 'match', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPnpImageBySearchCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-file/image/count'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('name' in params):
            queryParams['name'] = self.apiClient.toPathValue(params['name'])
        
        if ('platform' in params):
            queryParams['platform'] = self.apiClient.toPathValue(params['platform'])
        
        if ('productId' in params):
            queryParams['productId'] = self.apiClient.toPathValue(params['productId'])
        
        if ('match' in params):
            queryParams['match'] = self.apiClient.toPathValue(params['match'])
        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    
    def getPnpDefaultImages(self, **kwargs):
        """Retrieves the default image for a given platform or product ID

        Args:
            
            platform, str: Platform name. Provide either platform name or product ID (required)
            
            
            productId, str: Product ID. Provide either platform name or product ID (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: ZtdDefaultImageListResult
        """

        allParams = ['platform', 'productId', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPnpDefaultImages" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-file/image/default'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('platform' in params):
            queryParams['platform'] = self.apiClient.toPathValue(params['platform'])
        
        if ('productId' in params):
            queryParams['productId'] = self.apiClient.toPathValue(params['productId'])
        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ZtdDefaultImageListResult')
        return responseObject
        
        
        
    
    def getPnpValidImageExtensions(self, **kwargs):
        """Retrieves the valid image extensions supported

        Args:
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: ZtdValidExtensionsResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPnpValidImageExtensions" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-file/image/valid-extension'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ZtdValidExtensionsResult')
        return responseObject
        
        
        
    
    def getPnpImageById(self, **kwargs):
        """Retrieves an image and the platforms for which it is a default with its ID

        Args:
            
            imageId, str: Image ID (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: ZtdPlatformImageResult
        """

        allParams = ['imageId', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPnpImageById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-file/image/{imageId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        
        if ('imageId' in params):
            replacement = str(self.apiClient.toPathValue(params['imageId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'imageId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ZtdPlatformImageResult')
        return responseObject
        
        
        
    
    def deletePnpImageById(self, **kwargs):
        """Deletes an image and default platform assiciations with its ID

        Args:
            
            imageId, str: Image ID (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['imageId', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deletePnpImageById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-file/image/{imageId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        
        if ('imageId' in params):
            replacement = str(self.apiClient.toPathValue(params['imageId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'imageId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    
    def getPnpRecommendedPlatform(self, **kwargs):
        """Retrieves the recommended platforms for a given image

        Args:
            
            imageId, str: Image ID (required)
            
            
            productId, str: Product ID (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: ZtdPlatformListResult
        """

        allParams = ['imageId', 'productId', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPnpRecommendedPlatform" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-file/image/{imageId}/recommended-platform'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('productId' in params):
            queryParams['productId'] = self.apiClient.toPathValue(params['productId'])
        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        
        if ('imageId' in params):
            replacement = str(self.apiClient.toPathValue(params['imageId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'imageId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ZtdPlatformListResult')
        return responseObject
        
        
        
    
    def getPnpPlatforms(self, **kwargs):
        """Retrieves a list of platforms

        Args:
            
            platformName, str: Platform name (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: ZtdPlatformListResult
        """

        allParams = ['platformName', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPnpPlatforms" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-file/platform'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('platformName' in params):
            queryParams['platformName'] = self.apiClient.toPathValue(params['platformName'])
        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ZtdPlatformListResult')
        return responseObject
        
        
        
    
    def getTemplates(self, **kwargs):
        """Retrieves a list of template records

        Args:
            
            offset, int: Starting index of the response. Minimum value is 1 (required)
            
            
            limit, int: Limit the number of responses. Maximum value supported is 500. Minimum value is 1 (required)
            
            
            name, str: File name pattern (required)
            
            
            extension, str: Ext. txt, json, vm. Use \&quot;\&quot; for no extension.  Accepts a list of extensions. (required)
            
            
            matchExtension, bool: Match extension. Boolean to match the given extension (true) or not (false) (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: FileObjectListResult
        """

        allParams = ['offset', 'limit', 'name', 'extension', 'matchExtension', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getTemplates" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-file/template'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])
        
        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])
        
        if ('name' in params):
            queryParams['name'] = self.apiClient.toPathValue(params['name'])
        
        if ('extension' in params):
            queryParams['extension'] = self.apiClient.toPathValue(params['extension'])
        
        if ('matchExtension' in params):
            queryParams['matchExtension'] = self.apiClient.toPathValue(params['matchExtension'])
        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'FileObjectListResult')
        return responseObject
        
        
        
    
    def getTemplateCount(self, **kwargs):
        """Returns number of CLI template files

        Args:
            
            name, str: File name pattern (required)
            
            
            extension, str: Ext. txt, json, vm. Use \&quot;\&quot; for no extension.  Accepts a list of extensions. (required)
            
            
            matchExtension, bool: Match extension. Boolean to match the given extension (true) or not (false) (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: str
        """

        allParams = ['name', 'extension', 'matchExtension', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getTemplateCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-file/template/count'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        
        if ('name' in params):
            queryParams['name'] = self.apiClient.toPathValue(params['name'])
        
        if ('extension' in params):
            queryParams['extension'] = self.apiClient.toPathValue(params['extension'])
        
        if ('matchExtension' in params):
            queryParams['matchExtension'] = self.apiClient.toPathValue(params['matchExtension'])
        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    
    def deleteTemplateById(self, **kwargs):
        """Deletes a template with its ID

        Args:
            
            templateFileId, str: Template File ID (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['templateFileId', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteTemplateById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pnp-file/template/{templateFileId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        

        
        if ('scope' in params):
            headerParams['scope'] = params['scope']
        

        
        if ('templateFileId' in params):
            replacement = str(self.apiClient.toPathValue(params['templateFileId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'templateFileId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject
        
        
        
    


