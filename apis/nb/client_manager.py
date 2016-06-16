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

import os
import importlib
import json
import ssl
import sys
import datetime
import re
import itertools

from uniq.apis.client_manager import ClientManager
from uniq.apis.nb.clients.api_client import ApiClient
from uniq.apis.exceptions import UniqException
from uniq.apis.nb.services.task.task import Task

# Python would use the system provided certificate database on all platforms.
# Failure to locate such a database would be an error, and users would need to explicitly
# specify a location to fix it. This will be achieved by adding a new
# ssl._create_default_https_context function. http.client can then replace its usage of
# ssl._create_stdlib_context with the ssl._create_default_https_context.
# Reference: https://www.python.org/dev/peps/pep-0476/#technical-details
try:
    ssl._create_default_https_context = ssl._create_unverified_context
except Exception:
    pass


class NbClientManager(ClientManager):
    """ Northbound Client manager to interact with Swagger's API Client. """

    CLIENTS_PATH = os.path.join(os.path.split(os.path.realpath(__file__))[0], "clients")
    IMPORT_PATH = "uniq.apis.nb.clients"
    MODELS_DIR = "models"
    CLIENT_DIR_PATTERN = "_client"
    API_FILE_PATTERN = "Api.py"
    NULLABLE_TYPES = ['str', 'bool'] # 'None', False

    VERSION_V2 = "V2"

    def __init__(self, server, username, password, version="v1", connect=True):
        """ Object initializer

        Initializer also aunthenticates using the credentials, and stores the generated
        authentication ticket.

        Args:
            server (str): cluster server name (routable DNS addess or ip)
            username (str): user name to authenticate with
            password (str): password to authenticate with
            version (str): version of the API to be used
            connect (bool): flag to authenticate and establish swagger client
        """

        self.version = version
        base_url = "/api/" + self.version
        protocol = "https"

        super(NbClientManager, self).__init__(server, username, password, base_url,
                                              protocol=protocol)

        self.default_headers = {"Content-Type": "application/json"}

        self.api_dict = self.__load_apis(self.CLIENTS_PATH, self.IMPORT_PATH)
        self.duplicate_models = {}
        self.conflicting_models = {}
        self.model_dict = self.__load_models(self.CLIENTS_PATH, self.IMPORT_PATH)
        self.custom_api_client_path = []
        self.similar_api_dict = {}

        if connect:
            self.connect()
        self.setup_api()
        self.cookie = None

    def __repr__(self):
        """ Overrides the default object representation to display the object attributes. """

        return "[APIC: <server:{}> <username:{}> <password:{}> <version:{}>]".format(self.server,
                                                                                     self.username,
                                                                                     self.password,
                                                                                     self.version)

    def connect(self):
        """ Generates a new ticket and establishes a fresh swagger client. """

        self.log.info("Connecting to the Apic-em north bound API client.")
        self.authenticate()

    def disconnect(self):
        """ Deletes the generated ticket and effectively disconneting the user. """

        self.log.info("Disconnecting the Apic-em north bound API client.")

    def __load_models(self, clients_path, import_path=None, model_dict=None):
        """ Find all models files and their import path.

        Args:
            clients_path (str): path to all api clients.
            import_path (str): prefix of import path.

        Returns:
            A dict of model's name and its import path.
            Example:
            model_dict = {
                'Timestamp':
                    'uniq.apis.nb.clients.inventory_manager_client.client.models.Timestamp'
            }
        """

        if model_dict is None:
            model_dict = {}

        clients_dirs = os.listdir(clients_path)
        for client_dir in clients_dirs:
            if client_dir.endswith(self.CLIENT_DIR_PATTERN):
                models_dir = os.path.join(clients_path, client_dir, self.MODELS_DIR)
                model_files = os.listdir(models_dir)
                for model_file in model_files:
                    if model_file != "__init__.py" and model_file != "__pycache__":
                        model_file = model_file.replace(".py", "")
                        if import_path:
                            import_str = ".".join([self.IMPORT_PATH, client_dir, "models",
                                                   model_file])
                        else:
                            import_str = ".".join([client_dir, "models", model_file])

                        # Identify if the model name already exists.
                        if model_file in model_dict:
                            if model_file not in self.duplicate_models:
                                self.duplicate_models[model_file] = [model_dict[model_file]]
                            self.duplicate_models[model_file].append(import_str)
                        else:
                            model_dict[model_file] = import_str
        return model_dict

    def __load_apis(self, clients_path, import_path=None):
        """ Find all api files and their import path.

        Args:
            clients_path (str): path to all api clients.
            import_path (str): prefix of import path.

        Returns:
            A dict of api's name and its import path.
            Example:
            api_dict = {
                'DiscoveryApi':
                    'uniq.apis.nb.clients.inventory_manager_client.client.DiscoveryApi'
            }
        """

        api_dict = {}

        clients_dirs = os.listdir(clients_path)
        for client_dir in clients_dirs:
            if client_dir.endswith(self.CLIENT_DIR_PATTERN):
                api_files_dir = os.path.join(clients_path, client_dir)
                api_files = os.listdir(api_files_dir)
                for api_file in api_files:
                    if api_file.endswith(self.API_FILE_PATTERN):
                        api_file = api_file.replace(".py", "")
                        if import_path:
                            import_str = ".".join([self.IMPORT_PATH, client_dir, api_file])
                        else:
                            import_str = ".".join([client_dir, api_file])
                        api_dict[api_file] = import_str
        return api_dict

    def __get_api_instance(self, api_name):
        """ Get api instance by its name.

        Note:
            Only be able to get swagger auto-generated api client instance.

        Args:
            api_name (str): api name.

        Returns:
            An instance of api_name class
        """

        if api_name not in self.api_dict:
            raise Exception("Can't find api \"{}\"".format(api_name))
        if isinstance(self.api_dict[api_name], ApiClient):
            return self.api_dict[api_name]

        # Convert all api clients to uniq.nb.apis.clients.ApiClient.
        api_module = importlib.import_module(self.api_dict[api_name])
        api_class = getattr(api_module, api_name)

        if api_name.startswith(self.VERSION_V2):
            default_version = 'v2'
            version_client_map = {
                'v2': api_class
            }
        else:
            default_version = 'v1'
            version_client_map = {
                'v1': api_class
            }

        return ApiClient(self, version_client_map, default_version=default_version)

    def __deal_with_multiple_version(self):
        """ Create ApiClient object to deal with multiple version.

        If an endpoint has both v1 and v2 version of apis, this method will create an instance
        of ApiClient to handle multiple versions.
        If an endpoint has only v1 or v2 version of api, this method won't do anything.
        """

        for api in list(self.api_dict.keys()):
            if api.startswith(self.VERSION_V2):
                v1_api_name = api.replace(self.VERSION_V2, "")
                if v1_api_name in self.api_dict:
                    v2_module = importlib.import_module(self.api_dict[api])
                    v1_module = importlib.import_module(self.api_dict[v1_api_name])
                    self.__update_similar_api_dict(v1_api_name, api)
                    self.api_dict.pop(api)
                    self.api_dict.pop(v1_api_name)
                    version_client_map = {
                        'v1': getattr(v1_module, v1_api_name),
                        'v2': getattr(v2_module, api)
                    }
                    self.log.debug("Found similar apis: {}".format(self.similar_api_dict))
                    if v1_api_name in self.similar_api_dict:
                        self.api_dict[v1_api_name] = ApiClient(
                            self, version_client_map,
                            default_version='v1',
                            similar_api_map_list=self.similar_api_dict[v1_api_name])
                    else:
                        self.api_dict[v1_api_name] = ApiClient(self, version_client_map,
                                                               default_version='v1')

    def __deal_with_duplicate_models(self):
        """ Use most compatible models if duplicate models exist. """

        for model, imports in self.duplicate_models.items():
            self.model_dict[model] = self.__get_most_compatible_model(model, imports)

    def __dicts_are_compatible(self, dict_a, dict_b):
        """ Check if two dicts are compatible.

        Args:
            dict_a (dict): first dict
            dict_b (dict): second dict

        Note:
            Compatible means dict_a and dict_b must obey:
            1. dict_a and dict_b are identical. (All key value pairs are same.)
            2. dict_a contains dict_b (All key value pairs in dict_b also in dict_a)
            3. dict_b contains dict_a (All key value pairs in dict_a also in dict_b)

        Examples:
            >>> a = {1:1, 2:2}
            >>> b = {1:1, 2:3}
            >>> c = {1:1}

            >>> # a[2] != b[2]
            >>> dicts_are_compatible(a, b)
            False

            >>> # a contains c, which can be checked by a.items() > c.items()
            >>> dicts_are_compatible(a, c)
            True

        Returns True if two dicts are compatible.
        """

        dict_a_contains_b = dict_a.items() >= dict_b.items()
        dict_b_contains_a = dict_a.items() <= dict_b.items()

        return dict_a_contains_b or dict_b_contains_a

    def __get_most_compatible_model(self, model_name, import_paths):
        """ Get the most compatible model for a model name.

        Args:
            model_name (str): name of model.
            import_paths (list[str]): list of model paths for same model name.

        Note:
            What is most compatible?
            Attribute 'swaggerTypes' and 'attributeMap' are two attributes which decide the model.
            If those two dicts are compatible in two models(see definition of compatible in method
            '__dicts_are_compatible'), we say these two models are compatible. And if one's
            swaggerTypes contains more keys than another, we say the model is more compatible than
            another.

        Returns:
            Import path (str) of the most compatible model.
        """

        model_objs = [getattr(importlib.import_module(import_path), model_name)()
                      for import_path in import_paths]

        for obj_a, obj_b in itertools.combinations(model_objs, 2):
            if (self.__dicts_are_compatible(obj_a.swaggerTypes, obj_b.swaggerTypes) and
                self.__dicts_are_compatible(obj_a.attributeMap, obj_b.attributeMap)):
                continue
            else:
                self.log.info("Model {} and {} are not compatible."
                                  .format(obj_a.__class__, obj_b.__class__))
                if model_name not in self.conflicting_models:
                    self.conflicting_models[model_name] = set()
                self.conflicting_models[model_name].add(obj_a.__class__)
                self.conflicting_models[model_name].add(obj_b.__class__)

        if model_name in self.conflicting_models:
            return None
        else:
            index = model_objs.index(max(model_objs, key=lambda obj: obj.swaggerTypes.items()))
            return import_paths[index]

    def __update_similar_api_dict(self, v1_api_name, v2_api_name):
        """ Find similar api in different version apis and update similar api dict.

        Args:
            v1_api_name (str): version 1 api name.
            v2_api_name (str): version 2 api name.
        """

        v1_api_detail = self.read_json_by_module_path(self.api_dict[v1_api_name], "v1")
        v2_api_detail = self.read_json_by_module_path(self.api_dict[v2_api_name], "v2")
        if v1_api_detail and v2_api_detail:
            for v1_api in v1_api_detail["apis"]:
                for v2_api in v2_api_detail["apis"]:
                    if (v1_api["path"] == v2_api["path"].replace("/v2", "") and
                        v1_api["operations"][0]["method"] == v2_api["operations"][0]["method"] and
                        v1_api["operations"][0]["nickname"] != v2_api["operations"][0]["nickname"]):
                        if v1_api_name not in self.similar_api_dict:
                            self.similar_api_dict[v1_api_name] = []
                        self.similar_api_dict[v1_api_name].append(
                            {
                                "v1": v1_api["operations"][0]["nickname"],
                                "v2": v2_api["operations"][0]["nickname"]}
                            )

    @staticmethod
    def convert_module_name_to_json_file_name(name):
        """ Convert module name to json file name.

        Example:
            'PolicyApi' -> 'policy.json'
            'V2PolicyApi' -> 'v2-policy.json'

        Args:
            name (str): module name

        Returns:
            converted name (str).
        """

        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1-\2', s1).lower().replace("-api", ".json")

    def read_json_by_module_path(self, module_path, version):
        """ Read api json file.

        Args:
            module_path (str): module path of api.
            version (str): version of api.

        Returns:
            content (dict) of json file.
        """

        for sys_path in self.custom_api_client_path + sys.path:
            module_name = module_path.split(".")[-1]
            json_file_name = NbClientManager.convert_module_name_to_json_file_name(module_name)
            path = os.path.join(os.path.join(sys_path, *module_path.split(".")[:-1]),
                                json_file_name)
            if os.path.isfile(path):
                with open(path) as json_file:
                    content = json.load(json_file)
                return content
        return None

    def setup_api(self):
        """ Creates a swagger api client

            For swagger auto-generated api client, the naming rule is all lower case without ending
            with "api" of its classname.
            For example:
                self.user is an instance of UserApi.

        Args:
            ticket (str): session ticket
        """

        self.log.debug("Initializing the swagger north bound api client and endpoints.")

        self.__deal_with_multiple_version()
        self.__deal_with_duplicate_models()

        for api in self.api_dict:
            if api.endswith("Api"):
                attr_name = api[:-3]
            # If a service has only v2 api, get rid of prefix in client name.
            # For ex: V2ContractApi becomes ContractApi
            if attr_name.startswith(self.VERSION_V2):
                attr_name = attr_name.replace(self.VERSION_V2, "")

            self.add_api(attr_name.lower(), self.__get_api_instance(api))

        # Task Wrapper Library
        self.task_util = Task(self)

    def add_new_apis(self, nb_client_path):
        """ Finds and loads NB clients(their models, api files) from user-defined location.

        Args:
            nb_client_path (str): path to new clients, inside it should contain folders naming
                as apiname_client.

        Notes:
            If there is api file having the same filename and classname as in default api client
            folder, it will override the default one. Same for models.
        """

        nb_client_path = os.path.expanduser(nb_client_path)
        if not os.path.isdir(nb_client_path):
            self.log.error("{} is not a valid directory.".format(nb_client_path))
            raise Exception("{} is not a valid directory.".format(nb_client_path))
        sys.path.append(nb_client_path)
        self.custom_api_client_path.append(nb_client_path)

        self.api_dict.update(self.__load_apis(nb_client_path))
        self.__load_models(nb_client_path, model_dict=self.model_dict)

        self.setup_api()

    def serialize(self, model):
        """ Returns the serialized model

        Args:
            model (model object): Model object that needs to be serialized

        Returns:
            serialized model dict
        """

        return NbClientManager.sanitize_for_serialization(model)

    def authenticate(self):
        """ Generates a new authentication cas_ticket. """

        resource_path = "/ticket"
        data = json.dumps({"username": self.username, "password": self.password})
        response = self.call_api("POST", resource_path, data=data, raise_exception=True,
                                 response_dict=False)
        result_json = json.loads(response.text)
        if 'serviceTicket' in result_json['response'].keys():
            ticket = result_json["response"]["serviceTicket"]
        else:
            #TODO (hikoppu): Handle missing service ticket scenario more gracefully
            ticket = ""
        headers = {"X-Auth-Token": ticket, "X-CSRF-Token": "soon-enabled"}
        self.common_headers = headers
        self.cas_ticket = ticket

    def callAPI(self, resource_path, method, query_params, post_data,
                header_params={}, files=None, stream=False, api_version=None):
        """ Wrapper of call_api to support swagger auto generated code.

        Args:
            resource_path (str): resource_path
            method (str): http method, support "GET", "POST", "PUT", "DELETE"
            query_params (dict): query parameters
            post_data (dict or list): body to post.
            header_params (dict): custom headers.
            files (str): path to file
            stream (bool): return stream object.

        Returns:
            data (str): response of request.

        Raises:
            requests.exceptions.HTTPError if any http error happens.
        """

        headers = self.default_headers.copy()
        if header_params:
            for param, value in header_params.items():
                headers[param] = NbClientManager.sanitize_for_serialization(value)
        if self.cookie:
            headers['Cookie'] = NbClientManager.sanitize_for_serialization(self.cookie)

        data = None
        kwargs = {}

        if query_params:
            kwargs["params"] = query_params

        if method in ['GET']:
            if 'Content-Type' in headers:
                if (headers['Content-Type'] == 'multipart/form-data'
                    or headers['Accept'] == 'application/octet-stream'
                    or headers['Content-Type'] == 'application/octet-stream'):
                    return self.getFile(resource_path=resource_path,
                                        params=query_params,
                                        stream=stream,
                                        headers=headers)
            else:
                pass
        elif method in ['POST', 'PUT', 'DELETE']:
            if post_data or post_data == [] or files:

                if post_data:
                    post_data = NbClientManager.sanitize_for_serialization(post_data)
                if files:
                    files = NbClientManager.sanitize_for_serialization(files)
                    post_data = files

                if 'Content-Type' in headers and headers['Content-Type'] == 'application/json':
                    data = json.dumps(post_data)
                    kwargs["data"] = data.encode('utf-8')
                elif headers['Content-Type'] == 'multipart/form-data':
                    return self.postFile(method=method,
                                         files=post_data,
                                         resource_path=resource_path,
                                         params=query_params,
                                         headers=headers)
                else:
                    kwargs["data"] = post_data

        if method not in ["GET", "POST", "PUT", "DELETE"]:
            raise Exception('Method ' + method + ' is not recognized.')

        response = self.call_api(method, resource_path, headers=headers,
                                 response_dict=False, **kwargs)

        if 'Set-Cookie' in response.headers:
            self.cookie = response.headers['Set-Cookie']
        string = response.text

        if type(string) is bytes:
            string = string.decode()

        try:
            data = json.loads(string)
        except ValueError:  # PUT requests don't return anything
            data = None

        return data

    def postFile(self, method, files, resource_path, headers, params=None):
        """ Posts the files

        Args:
            method (str): http method, support "POST", "PUT"
            files (str or dict): File(s) in the request object
            resource_path (str): URL in the request object
            headers (str): Headers in the request object
            params (dict): key/value pairs in the URL after a '?', Ex: httpbin.org/get?key=val

        Returns:
            data (response): JSON form of the response of the post method

        Raises:
            RequestException if invalid data is posted
            ValueError if the response of the post method cannot be converted to JSON.
        """

        headers.pop('Content-Type')
        files_to_post = {}
        if type(files) == dict:
            for name, filepath in files.items():
                fileobj = open(filepath, 'rb')
                files_to_post[name] = fileobj

        if type(files) == str:
            fileobj = open(files, 'rb')
            files_to_post['fileUpload'] = fileobj

        response = self.call_api(method=method,
                                 resource_path=resource_path,
                                 params=params,
                                 files=files_to_post,
                                 verify=False,
                                 headers=headers,
                                 response_dict=False)

        try:
            data = json.loads(response.text)
        except ValueError as err:
            data = None
            raise err

        return data

    def getFile(self, resource_path, headers, stream, params=None):
        """ Gets the files

        Args:
            resource_path (str): URL in the request object
            headers (str): Headers in the request object
            params (dict): key/value pairs in the URL after a '?', Ex: httpbin.org/get?key=val
            stream (bool): return stream object

        Returns:
            Response of the get method

        Raises:
            RequestException if invalid data is being requested
        """

        response = self.call_api("GET",
                                 resource_path=resource_path,
                                 params=params,
                                 verify=False,
                                 headers=headers,
                                 response_dict=False,
                                 stream=stream)
        return response

    def toPathValue(self, obj):
        """Convert a string or object to a path-friendly value
        Args:
            obj -- object or string value
        Returns:
            string -- quoted value
        """
        if type(obj) == list:
            return ','.join(obj)
        else:
            return str(obj)

    @staticmethod
    def sanitize_for_serialization(obj):
        """
        Sanitize an object for Request.

        If obj is None, return None.
        If obj is str, int, float, bool, return directly.
        If obj is datetime.datetime, datetime.date convert to string in iso8601 format.
        If obj is list, santize each element in the list.
        If obj is dict, return the dict.
        If obj is swagger model, return the properties dict.
        """
        if isinstance(obj, type(None)):
            return None
        elif isinstance(obj, (str, int, float, bool)):
            return obj
        elif isinstance(obj, list):
            return [NbClientManager.sanitize_for_serialization(sub_obj) for sub_obj in obj]
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        else:
            if isinstance(obj, dict):
                obj_dict = obj
            else:
                # Convert model obj to dict except attributes `swaggerTypes`, `attributeMap`
                # and attributes which value is not None.
                # Convert attribute name to json key in model definition for
                # request.
                obj_dict = {obj.attributeMap[key]: val
                            for key, val in obj.__dict__.items()
                            if key != 'swaggerTypes' and key != 'attributeMap' and val is not None}
            return {key: NbClientManager.sanitize_for_serialization(val)
                    for (key, val) in obj_dict.items()}

    def deserialize(self, obj, objClass):
        """Derialize a JSON string into an object.

        Args:
            obj -- string or object to be deserialized
            objClass -- class literal for deserialzied object, or string
                of class name
        Returns:
            object -- deserialized object"""

        # Have to accept objClass as string or actual type. Type could be a
        # native Python type, or one of the model classes.
        if type(objClass) == str:
            if 'list[' in objClass:
                match = re.match('list\[(.*)\]', objClass)
                subClass = match.group(1)
                return [self.deserialize(subObj, subClass) for subObj in obj]

            if (objClass in ['int', 'float', 'dict', 'list', 'str', 'bool', 'datetime']):
                objClass = eval(objClass)
            elif objClass in self.conflicting_models:
                raise UniqException(
                    "Multiple conflicting models {} exist {}, please check those models and make "
                    "sure they are compatible.".format(objClass, self.conflicting_models[objClass]))
            elif objClass in self.model_dict: # in auto-generated models
                api_module = importlib.import_module(self.model_dict[objClass])
                objClass = getattr(api_module, objClass)
            else:  # not a native type, must be model class
                objClass = eval(objClass + '.' + objClass)

        if objClass in [int, int, float, dict, list, str, bool]:
            if obj is not None:
                return objClass(obj)
            elif objClass in NbClientManager.NULLABLE_TYPES:
                return objClass(obj)
            else:
                return None
        elif objClass == datetime:
            return self.__parse_string_to_datetime(obj)

        instance = objClass()

        for attr, attrType in instance.swaggerTypes.items():
            if obj is not None and instance.attributeMap[attr] in obj and type(obj) in [list, dict]:
                value = obj[instance.attributeMap[attr]]
                if attrType in ['unicode', 'str', 'int', 'float', 'bool']:
                    attrType = eval(attrType)
                    # print "value_orig: '%s'. Type: %s" % (value, type(value))
                    if (value is None):
                        setattr(instance, attr, None)
                    else:
                        try:
                            value = attrType(value)
                        except UnicodeEncodeError:
                            value = str(value)
                        except TypeError:
                            value = value
                        setattr(instance, attr, value)
                    # print "value: '%s'. Type: %s" % (value, type(value))
                elif (attrType == 'datetime'):
                    setattr(
                        instance, attr, self.__parse_string_to_datetime(value))
                elif (attrType == 'date-time'):
                    # Java TimeStamp
                    setattr(instance, attr, self.deserialize(value, int))
                elif 'list[' in attrType:
                    match = re.match('list\[(.*)\]', attrType)
                    subClass = match.group(1)
                    subValues = []
                    if not value:
                        setattr(instance, attr, None)
                    else:
                        for subValue in value:
                            subValues.append(
                                self.deserialize(subValue, subClass))
                    setattr(instance, attr, subValues)
                elif 'simple_dict' in attrType: #TODO DELETE
                    if not value:
                        setattr(instance, attr, None)
                    else:
                        new_dict = {}
                        for key in list(value.keys()):
                            dicValue = value[key]
                            if ((type(dicValue) is not str) and (type(dicValue) is not str)):
                                assert False, "wrong type for key %s: %s" % (key, type(dicValue))
                            new_dict[key] = dicValue
                        setattr(instance, attr, new_dict)
                else:
                    setattr(instance, attr, self.deserialize(value, attrType))

        return instance

    def __parse_string_to_datetime(self, string):
        """
        Parse datetime in string to datetime.

        The string should be in iso8601 datetime format.
        """
        try:
            from dateutil.parser import parse
            return parse(string)
        except ImportError:
            return string
