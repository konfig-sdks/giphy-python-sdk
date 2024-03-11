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


class RequiredUser(TypedDict):
    pass

class OptionalUser(TypedDict, total=False):
    # The URL for this user's avatar image.
    avatar_url: str

    # The URL for the banner image that appears atop this user's profile page.
    banner_url: str

    # The display name associated with this user (contains formatting the base username might not).
    display_name: str

    # The URL for this user's profile.
    profile_url: str

    # The Twitter username associated with this user, if applicable.
    twitter: str

    # The username associated with this user.
    username: str

class User(RequiredUser, OptionalUser):
    pass