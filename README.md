![uniq](uniq.png?raw=true "uniq")

uniq is a Python API client library for Cisco's Application Policy Infrastructure Controller Enterprise Module (APIC-EM) Northbound APIs.

# Description

The APIC-EM Northbound Interface is the only API that you will need to control your network programmatically. The API is function rich and provides you with an easy-to-use, programmatic control of your network elements, interfaces, and hosts.

The APIC-EM API provides you with the ability to think about your network at a higher policy level rather than how to implement that policy. When you use the APIC-EM API, your applications will make network policy decisions, which will then be implemented by the APIC-EM Controller through its Southbound Interfaces. Thus you tell the network what you want (i.e., the policy) and the controller figures out how to implement that policy for you.

The APIC-EM API is REST based and thus you will discover and control your network using HTTP protocol with HTTP verbs (i.e., GET, POST, PUT, and DELETE) with JSON syntax.

This package provides a handle to this rich API library in an easy to consume fashion.

# Getting Started


### Download
Clone this repository:

``` bash
git clone https://github.com/CiscoDevNet/uniq.git
```

### Install
Then install the package locally.

``` bash
cd uniq
python setup.py install
```

### Use
Import the package and make an API call.

``` python
from uniq.apis.nb.client_manager import NbClientManager

client = NbClientManager(
    server="1.1.1.1",
    username="username",
    password="password",
    connect=True)

# NorthBound API call to get all users
user_list_result = client.user.getUsers()

# Serialize the model object to a python dictionary
users = client.serialize(user_list_result)

print(users)
```

### Running Tests

The tests are located in the [tests](tests/) directory.
After installing the package, they can be run by executing the below command:

```
python setup.py test
```

### Sample Scripts

For sample scripts check out the [sample_scripts](sample_scripts/) directory.

# Python

This project has been tested and working on Python 3.0+

#### Installation Issues

*   Issue due to ```setuptools```

    If you see an error message like so:
    ```
    error: can't copy 'opyright': doesn't exist or not a regular file
    ```
    please update the ```setuptools``` package by running the below command, and trying again.
    ```
    pip3 install -U setuptools
    ```