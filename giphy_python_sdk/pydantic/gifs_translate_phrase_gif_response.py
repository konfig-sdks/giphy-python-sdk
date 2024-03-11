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
from pydantic import BaseModel, Field, RootModel

from giphy_python_sdk.pydantic.gif import Gif
from giphy_python_sdk.pydantic.meta import Meta

class GifsTranslatePhraseGifResponse(BaseModel):
    data: typing.Optional[Gif] = Field(None, alias='items')

    meta: typing.Optional[Meta] = Field(None, alias='meta')
    class Config:
        arbitrary_types_allowed = True
