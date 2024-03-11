# coding: utf-8
"""
    Giphy API

    Giphy API

    The version of the OpenAPI document: 1.0
    Contact: support@giphy.com
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from giphy_python_sdk.client_custom import ClientCustom
from giphy_python_sdk.configuration import Configuration
from giphy_python_sdk.api_client import ApiClient
from giphy_python_sdk.type_util import copy_signature
from giphy_python_sdk.apis.tags.gifs_api import GifsApi
from giphy_python_sdk.apis.tags.stickers_api import StickersApi



class Giphy(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.gifs: GifsApi = GifsApi(api_client)
        self.stickers: StickersApi = StickersApi(api_client)
