# coding: utf-8

"""
    Giphy API

    Giphy API

    The version of the OpenAPI document: 1.0
    Contact: support@giphy.com
    Generated by: https://konfigthis.com
"""

from giphy_python_sdk.paths.gifs_gif_id.get import GetByIdRaw
from giphy_python_sdk.paths.gifs.get import GetByIdsRaw
from giphy_python_sdk.paths.gifs_random.get import GetRandomGifRaw
from giphy_python_sdk.paths.gifs_trending.get import GetTrendingGifsRaw
from giphy_python_sdk.paths.gifs_search.get import SearchGifsRaw
from giphy_python_sdk.paths.gifs_translate.get import TranslatePhraseGifRaw


class GifsApiRaw(
    GetByIdRaw,
    GetByIdsRaw,
    GetRandomGifRaw,
    GetTrendingGifsRaw,
    SearchGifsRaw,
    TranslatePhraseGifRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
