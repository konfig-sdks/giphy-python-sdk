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

from giphy_python_sdk.type.image import Image

class RequiredGifImages(TypedDict):
    pass

class OptionalGifImages(TypedDict, total=False):
    downsized: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    downsized_large: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    downsized_medium: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    downsized_small: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    downsized_still: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    fixed_height: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    fixed_height_downsampled: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    fixed_height_small: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    fixed_height_small_still: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    fixed_height_still: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    fixed_width: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    fixed_width_downsampled: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    fixed_width_small: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    fixed_width_small_still: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    fixed_width_still: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    looping: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    original: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    original_still: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    preview: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    preview_gif: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class GifImages(RequiredGifImages, OptionalGifImages):
    pass
