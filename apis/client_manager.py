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

import json

try:
    from uniq.common import logger
except:
    import logging
    logger = logging.getLogger("uniq")
from .exceptions import ApiClientException
from .exceptions import ConnectionException

import requests


class ClientManager(object):
    """ Client manager to interact with API Clients of various services. """

    def __init__(self, server, username, password, base_url, protocol="https", port=None):
        """ Object initializer

        Initializer also authenticates using the credentials, and stores the generated
        authentication ticket/token.

        Args:
            server (str): cluster server name (routable DNS addess or ip)
            username (str): user name to authenticate with
            password (str): password to authenticate with
            port (str): port number
            service (str): service to which the api calls are to be made
            connect (bool): flag to authenticate and establish api client
        """

        self.log = logger

        self.server = server
        self.username = username
        self.password = password

        self.port = str(port)
        if port:
            self.server = self.server + ":" + self.port

        if protocol not in ["http", "https"]:
            self.log.error("Not supported protocol {}.".format(protocol))
            raise ApiClientException("Not supported protocol {}.".format(protocol))

        self.base_url = "{}://{}{}".format(protocol, self.server, base_url)

        self._default_headers = {}
        self._common_headers = {}

    def __repr__(self):
        """ Overrides the default object representation to display the object attributes. """

        return "[API Client: <server:{}> <username:{}> <password:{}>]".format(self.server,
                                                                             self.username,
                                                                             self.password)

    def add_api(self, name, obj):
        """ Add an api client to client manager.

        Args:
            name (str): name you want to set to the api client, has to follow python variable naming
                        rule.
            obj (object): api client which actually calling call_api method.
        """

        setattr(self, name, obj)

    def connect(self):
        """ Generates a new ticket/token. """

        self.log.info("Connecting to the API client.")
        self.authenticate()

    def disconnect(self):
        """ Disconnect from API client"""

        self.log.info("Disconnecting from the API client.")

    def authenticate(self):
        """ Generates a new authentication ticket or token. """

        raise NotImplementedError

    @property
    def default_headers(self):
        return self._default_headers

    @default_headers.setter
    def default_headers(self, headers):
        """ Set default headers of client.

        Args:
            headers (dict): headers to set.
        """

        self._default_headers.update(headers)

    @property
    def common_headers(self):
        return self._common_headers

    @common_headers.setter
    def common_headers(self, headers):
        """ Set common headers of client.

        Args:
            headers (dict): headers to set.
        """

        self._common_headers.update(headers)

    def call_api(self, method, resource_path, raise_exception=True, response_dict=True, **kwargs):
        """ Handles the requests and response.

        Args:
            method (str): type of request.
            resource_path (str): URL in the request object.
            raise_exception (boolean): If True, http exceptions will be raised.
            response_dict (boolean): If True, response dict is returned, else response object
            url (optional): URL for the new Request object.
            params (optional): Dictionary or bytes to be sent in the query string for the Request.
            data (optional): Dictionary, bytes, or file-like object to send in the body of the
                             Request.
            json (optional): json data to send in the body of the Request.
            headers (optional): Dictionary of HTTP Headers to send with the Request.
            cookies (optional): Dict or CookieJar object to send with the Request.
            files (optional): Dictionary of 'name': file-like-objects
                              (or {'name': ('filename', fileobj)}) for multipart encoding upload.
            auth (optional): Auth tuple to enable Basic/Digest/Custom HTTP Auth.
            timeout (float or tuple) (optional): How long to wait for the server to send data
                                                 before giving up, as a float, or a (connect
                                                 timeout, read timeout) tuple.
            allow_redirects (bool) (optional): Boolean. Set to True if POST/PUT/DELETE redirect
                                               following is allowed.
            proxies (optional): Dictionary mapping protocol to the URL of the proxy.
            verify (optional): if True, the SSL cert will be verified. A CA_BUNDLE path can also
                               be provided.
            stream (optional): if False, the response content will be immediately downloaded.
            cert (optional): if String, path to ssl client cert file (.pem). If Tuple,
                             (‘cert’, ‘key’) pair
        Returns:
            response object or response dict depending on boolean variable - response_dict.
        """

        url = self.base_url + resource_path

        if "/api/v1/v2/" in url:
            url = url.replace("/api/v1/v2/", "/api/v2/")

        if "headers" in kwargs:
            headers = kwargs.pop("headers")
        else:
            headers = self.default_headers

        headers.update(self.common_headers)

        if "verify" in kwargs:
            verify = kwargs.pop("verify")
        else:
            verify = False
            requests.packages.urllib3.disable_warnings()

        self.log.debug("Request:\nmethod:\n{}\nurl: {}\nheaders: {}\nParameters: {}".format(
                method, url, headers, kwargs))
        response = requests.request(method, url, headers=headers, verify=verify, **kwargs)
        self.log.debug("Response: {}".format(response.text))

        if raise_exception:
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                self.log.exception("Error Code: {} URL:{} Data:{} Headers:{} Message:{}"
                                   .format(e.response.status_code, url, kwargs, headers,
                                           e.response.text))
                raise e

        if response_dict:
            return json.loads(response.text)
        else:
            return response
