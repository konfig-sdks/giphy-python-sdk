# coding: utf-8

"""
    Giphy API

    Giphy API

    The version of the OpenAPI document: 1.0
    Contact: support@giphy.com
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from giphy_python_sdk.type.gif import Gif
from giphy_python_sdk.type.meta import Meta
from giphy_python_sdk.type.pagination import Pagination

class RequiredGifsSearchGifsResponse(TypedDict):
    pass

class OptionalGifsSearchGifsResponse(TypedDict, total=False):
    data: typing.List[Gif]

    meta: Meta

    pagination: Pagination

class GifsSearchGifsResponse(RequiredGifsSearchGifsResponse, OptionalGifsSearchGifsResponse):
    pass
