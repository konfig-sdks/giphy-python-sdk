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


class RequiredPagination(TypedDict):
    pass

class OptionalPagination(TypedDict, total=False):
    # Total number of items returned.
    count: int

    # Position in pagination.
    offset: int

    # Total number of items available.
    total_count: int

class Pagination(RequiredPagination, OptionalPagination):
    pass
