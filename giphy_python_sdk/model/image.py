# coding: utf-8

"""
    Giphy API

    Giphy API

    The version of the OpenAPI document: 1.0
    Contact: support@giphy.com
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from giphy_python_sdk import schemas  # noqa: F401


class Image(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            frames = schemas.StrSchema
            height = schemas.StrSchema
            mp4 = schemas.StrSchema
            mp4_size = schemas.StrSchema
            size = schemas.StrSchema
            url = schemas.StrSchema
            webp = schemas.StrSchema
            webp_size = schemas.StrSchema
            width = schemas.StrSchema
            __annotations__ = {
                "frames": frames,
                "height": height,
                "mp4": mp4,
                "mp4_size": mp4_size,
                "size": size,
                "url": url,
                "webp": webp,
                "webp_size": webp_size,
                "width": width,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["frames"]) -> MetaOapg.properties.frames: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["height"]) -> MetaOapg.properties.height: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mp4"]) -> MetaOapg.properties.mp4: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mp4_size"]) -> MetaOapg.properties.mp4_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webp"]) -> MetaOapg.properties.webp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webp_size"]) -> MetaOapg.properties.webp_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["width"]) -> MetaOapg.properties.width: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["frames", "height", "mp4", "mp4_size", "size", "url", "webp", "webp_size", "width", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["frames"]) -> typing.Union[MetaOapg.properties.frames, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["height"]) -> typing.Union[MetaOapg.properties.height, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mp4"]) -> typing.Union[MetaOapg.properties.mp4, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mp4_size"]) -> typing.Union[MetaOapg.properties.mp4_size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["size"]) -> typing.Union[MetaOapg.properties.size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webp"]) -> typing.Union[MetaOapg.properties.webp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webp_size"]) -> typing.Union[MetaOapg.properties.webp_size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["width"]) -> typing.Union[MetaOapg.properties.width, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["frames", "height", "mp4", "mp4_size", "size", "url", "webp", "webp_size", "width", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        frames: typing.Union[MetaOapg.properties.frames, str, schemas.Unset] = schemas.unset,
        height: typing.Union[MetaOapg.properties.height, str, schemas.Unset] = schemas.unset,
        mp4: typing.Union[MetaOapg.properties.mp4, str, schemas.Unset] = schemas.unset,
        mp4_size: typing.Union[MetaOapg.properties.mp4_size, str, schemas.Unset] = schemas.unset,
        size: typing.Union[MetaOapg.properties.size, str, schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        webp: typing.Union[MetaOapg.properties.webp, str, schemas.Unset] = schemas.unset,
        webp_size: typing.Union[MetaOapg.properties.webp_size, str, schemas.Unset] = schemas.unset,
        width: typing.Union[MetaOapg.properties.width, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Image':
        return super().__new__(
            cls,
            *args,
            frames=frames,
            height=height,
            mp4=mp4,
            mp4_size=mp4_size,
            size=size,
            url=url,
            webp=webp,
            webp_size=webp_size,
            width=width,
            _configuration=_configuration,
            **kwargs,
        )
