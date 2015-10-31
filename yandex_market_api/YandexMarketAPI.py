# coding: utf-8

__title__ = 'YandexMarketAPI'
__version__ = '0.0.1'
__author__ = 'Bulat Khasanov'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2015 Bulat Khasanov'

import requests

API_VERSION = 1


class YandexMarketApi(object):
    def __init__(self, authorization_key):
        self.authorization_key = authorization_key
        self.http = requests.Session()
        self.http.headers = {
            'Host': 'api.content.market.yandex.ru',
            'Accept': '*/*',
            'Authorization': authorization_key,
        }
