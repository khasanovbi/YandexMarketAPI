# coding: utf-8
__author__ = 'Bulat Khasanov'
__license__ = 'Apache 2.0'

from .constants import *
import requests
from requests.exceptions import ConnectionError, ReadTimeout, SSLError
from requests.packages.urllib3.exceptions import ReadTimeoutError, ProtocolError
import socket
import ssl


class YandexMarketAPI(object):

    """Access Yandex REST API resources.

    :param authorization_key: Yandex authorization key
    """

    def __init__(self, authorization_key):
        self.authorization_key = authorization_key

    def _prepare_url(self, resource):
        return '%s://%s/v%s/%s.json' % (PROTOCOL, DOMAIN, API_VERSION, resource)

    def _prepare_resource_path(self, resource_path, params=None):
        return resource_path.format(**params)

    def request(self, resource, params=None):
        if resource not in RESOURCES:
            raise Exception('Resource "%s" unsupported' % resource)
        session = requests.Session()
        session.headers = {
            'Host': DOMAIN,
            'Accept': '*/*',
            'Authorization': self.authorization_key,
            'User-agent': USER_AGENT,
        }
        resource_path = self._prepare_resource_path(resource, params)
        url = self._prepare_url(resource_path)
        try:
            response = session.get(
                url,
                **params
            )
            return response.json()
        except (ConnectionError, ProtocolError, ReadTimeout, ReadTimeoutError, SSLError, ssl.SSLError,
                socket.error) as exception:
            pass
