# coding: utf-8

"""
    Giphy API

    Giphy API

    The version of the OpenAPI document: 1.0
    Contact: support@giphy.com
    Generated by: https://konfigthis.com
"""

from giphy_python_sdk.paths.gifs_gif_id.get import GetById
from giphy_python_sdk.paths.gifs.get import GetByIds
from giphy_python_sdk.paths.gifs_random.get import GetRandomGif
from giphy_python_sdk.paths.gifs_trending.get import GetTrendingGifs
from giphy_python_sdk.paths.gifs_search.get import SearchGifs
from giphy_python_sdk.paths.gifs_translate.get import TranslatePhraseGif
from giphy_python_sdk.apis.tags.gifs_api_raw import GifsApiRaw


class GifsApi(
    GetById,
    GetByIds,
    GetRandomGif,
    GetTrendingGifs,
    SearchGifs,
    TranslatePhraseGif,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: GifsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = GifsApiRaw(api_client)