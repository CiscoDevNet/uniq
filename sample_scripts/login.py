""" Helper module to build interactive sample python script.

Usage:
    import login
    client = login.login()
"""

import getpass
import argparse

import requests.exceptions

from uniq.apis.nb.client_manager import NbClientManager


def argparser():
    """ Returns an argparser instance (argparse.ArgumentParser) to support command line options."""

    parser = argparse.ArgumentParser(description='Arguments for logging in APIC-EM cluster.')
    parser.add_argument('-c', '--cluster',
                        required=False,
                        action='store',
                        help='cluster ip/name of APIC-EM.')
    parser.add_argument('-u', '--username',
                        required=False,
                        action='store',
                        help='Username to login.')
    parser.add_argument('-p', '--password',
                        required=False,
                        action='store',
                        help='Password to login.')
    return parser

def login():
    """ Login to APIC-EM northbound APIs in shell.

    Returns:
        Client (NbClientManager) which is already logged in.
    """

    parser = argparser()
    args = parser.parse_args()

    using_parser = False
    if args.cluster or args.username or args.password:
        using_parser = True

    host = args.cluster or None
    username = args.username or None
    password = args.password or None
    client = None

    while not client:
        host_prompt = 'Host Address[{}]: '.format(host) if host else 'Host Address: '
        username_prompt = 'Username[{}]: '.format(username) if username else 'Username: '

        if not using_parser or not host:
            host = input(host_prompt) or host
        if not using_parser or not username:
            username = input(username_prompt) or username
        if not using_parser or not password:
            password = getpass.getpass('Password: ') or password
        using_parser = False

        try:
            client = NbClientManager(
                server=host,
                username=username,
                password=password,
                connect=True)
        except requests.exceptions.HTTPError as exc_info:
            if exc_info.response.status_code == 401:
                print('Authentication Failed. Please provide valid username/password.')
                continue
            else:
                print('HTTP Status Code {code}. Reason: {reason}'.format(
                    code=exc_info.response.status_code,
                    reason=exc_info.response.reason))
                exit(1)
        except requests.exceptions.ConnectionError:
            print('Connection aborted. Please check if the host {} is available.'.format(host))
            exit(1)
    return client
