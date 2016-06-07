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

import inspect

from uniq.apis.exceptions import UniqException


class ApiClient(object):
    """ Api client class to handle multiple version of apis. """

    def __init__(self, api_client, version_client_class_map, default_version,
                 similar_api_map_list=None):
        """ Initializer of ApiClient.

        Args:
            api_client (ClientManager): ClientManager instance.
            version_client_class_map (dict): key is version number, value is class of api client.
            default_version (str): default version.
            similar_api_map_list (list): list of map of apis with different name but same feature.
                                         Example: [{'v1': 'get', 'v2': 'getById'}]
        """

        self.version_client_class_map = version_client_class_map
        self.api_client = api_client
        self.apiClient = api_client # Depreciated, used for backward compatible.
        self.version_clients_map = {}
        self.versioned_apis = {}
        self.all_apis = {}
        self.default_version = default_version

        self._collect_apis(similar_api_map_list)

    def __getattr__(self, name):
        """ Get attribute based on name.

        Args:
            name (str): name of attribute.

        Returns:
            Wrapped api method(function) with additional argument api_verion.
        """

        if name in self.versioned_apis:
            return self.versioned_apis[name]
        raise AttributeError

    def _collect_apis(self, similar_api_map_list=None):
        """ Collect all apis and make them accessible by name and version.

        This method will collect all apis from clients of different versions, deal with apis
        with different name but same feature, and wrap all api methods so that we can choose
        different version api call with argument 'api_version'.

        Args:
            similar_api_map_list (dict): list of map of apis with different name but same feature.
                                         Example: [{'v1': 'get', 'v2': 'getById'}]
        """

        self.all_apis = {}
        for version, client_class in self.version_client_class_map.items():
            self.version_clients_map[version] = client_class(self.api_client)

        for version, client in self.version_clients_map.items():
            # Get all methods (api definition) in the api client
            apis = inspect.getmembers(client, predicate=inspect.ismethod)
            for name, method in apis:
                if name != '__init__':
                    if name not in self.all_apis:
                        self.all_apis[name] = {}
                    self.all_apis[name][version] = method

        if similar_api_map_list:
            for similar_api_map in similar_api_map_list:
                for version_1, name_1 in similar_api_map.items():
                    for version_2, name_2 in similar_api_map.items():
                        if name_1 != name_2 and version_2 not in self.all_apis[name_1]:
                            self.all_apis[name_1][version_2] = self.all_apis[name_2][version_2]

        for api_name, version_function_map in self.all_apis.items():
            self.versioned_apis[api_name] = self._add_api_version_as_argument(version_function_map)

    def _add_api_version_as_argument(self, version_function_map):
        """ Add api_version as an argument to all api method.

        Args:
            version_function_map (dict): key is version and value is function object.

        Returns:
            wrapper function which will decide which api to be call according to the version.
        """

        def wrapper(*args, **kwargs):
            """ Wrapper function.

                If api_version is set, return corresponding method.
                If not, and if there is only one method, return that method.
                if there are more than one method, return the default version one.
            """

            if 'api_version' in kwargs:
                api_version = kwargs.pop('api_version')
                if api_version in version_function_map:
                    return version_function_map[api_version](*args, **kwargs)
                else:
                    raise UniqException("endpoint '{}' doesn't support version '{}'"
                                        .format(list(version_function_map.values())[0].__name__,
                                                api_version))

            elif len(version_function_map) == 1:
                return list(version_function_map.values())[0](*args, **kwargs)
            else:
                return version_function_map[self.default_version](*args, **kwargs)
        return wrapper

