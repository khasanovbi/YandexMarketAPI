# coding: utf-8
__author__ = 'Bulat Khasanov'
__license__ = 'Apache 2.0'

API_VERSION = 1

USER_AGENT = 'python-YandexMarketAPI'

PROTOCOL = 'https'

DOMAIN = 'api.content.market.yandex.ru'

RESOURCES = [
    # Категории
    'category',
    'category/{category_id}',
    'category/{category_id}/children',
    'category/{category_id}/models',
    'category/{category_id}/filters',

    # Модели товаров
    'model/{model_id}',
    'model/{model_id}/info',
    'model/{model_id}/offers',
    'model/{model_id}/outlets',
    'model/{model_id}/reviews',

    # Популярные модели
    'popular',
    'popular/{category_id}',

    # Товарные предложения
    'offer/{offer_id}',

    # Отзывы
    'shop/{shop_id}/opinion'
    'model/{model_id}/opinion'

    # Магазины
    'shop/{shop_id}',
    'shop/{shop_id}/outlets',

    # Регионы
    'georegion',
    'georegion/{geo_id}',
    'georegion/{geo_id}/children',
    'georegion/suggest',

    # Производители
    'vendor',
    'vendor/{vendor_id}',

    # Сервисы
    'search',
    'model/match',
    'vendor/match',
    'filter/{category_id}',
]
