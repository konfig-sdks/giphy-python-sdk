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

from giphy_python_sdk.pydantic.gif_featured_tags import GifFeaturedTags
from giphy_python_sdk.pydantic.gif_images import GifImages
from giphy_python_sdk.pydantic.gif_tags import GifTags
from giphy_python_sdk.pydantic.user import User

class Gif(BaseModel):
    tags: typing.Optional[GifTags] = Field(None, alias='tags')

    # The unique bit.ly URL for this GIF
    bitly_url: typing.Optional[str] = Field(None, alias='bitly_url')

    # Currently unused
    content_url: typing.Optional[str] = Field(None, alias='content_url')

    # The date this GIF was added to the GIPHY database.
    create_datetime: typing.Optional[datetime] = Field(None, alias='create_datetime')

    # A URL used for embedding this GIF
    embded_url: typing.Optional[str] = Field(None, alias='embded_url')

    featured_tags: typing.Optional[GifFeaturedTags] = Field(None, alias='featured_tags')

    # This GIF's unique ID
    id: typing.Optional[str] = Field(None, alias='id')

    images: typing.Optional[GifImages] = Field(None, alias='images')

    # The creation or upload date from this GIF's source.
    import_datetime: typing.Optional[datetime] = Field(None, alias='import_datetime')

    # The MPAA-style rating for this content. Examples include Y, G, PG, PG-13 and R
    rating: typing.Optional[str] = Field(None, alias='rating')

    # The unique slug used in this GIF's URL
    slug: typing.Optional[str] = Field(None, alias='slug')

    # The page on which this GIF was found
    source: typing.Optional[str] = Field(None, alias='source')

    # The URL of the webpage on which this GIF was found.
    source_post_url: typing.Optional[str] = Field(None, alias='source_post_url')

    # The top level domain of the source URL.
    source_tld: typing.Optional[str] = Field(None, alias='source_tld')

    # The date on which this gif was marked trending, if applicable.
    trending_datetime: typing.Optional[datetime] = Field(None, alias='trending_datetime')

    # Type of the gif. By default, this is almost always gif
    type: typing.Optional[Literal["gif"]] = Field(None, alias='type')

    # The date on which this GIF was last updated.
    update_datetime: typing.Optional[datetime] = Field(None, alias='update_datetime')

    # The unique URL for this GIF
    url: typing.Optional[str] = Field(None, alias='url')

    user: typing.Optional[User] = Field(None, alias='user')

    # The username this GIF is attached to, if applicable
    username: typing.Optional[str] = Field(None, alias='username')
    class Config:
        arbitrary_types_allowed = True
