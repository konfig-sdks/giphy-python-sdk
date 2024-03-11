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


class StickersFindAnimatedStickersResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class data(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Gif']:
                        return Gif
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Gif'], typing.List['Gif']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'data':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Gif':
                    return super().__getitem__(i)
        
            @staticmethod
            def meta() -> typing.Type['Meta']:
                return Meta
        
            @staticmethod
            def pagination() -> typing.Type['Pagination']:
                return Pagination
            __annotations__ = {
                "data": data,
                "meta": meta,
                "pagination": pagination,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> 'Meta': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pagination"]) -> 'Pagination': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", "meta", "pagination", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union[MetaOapg.properties.data, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union['Meta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pagination"]) -> typing.Union['Pagination', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", "meta", "pagination", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        data: typing.Union[MetaOapg.properties.data, list, tuple, schemas.Unset] = schemas.unset,
        meta: typing.Union['Meta', schemas.Unset] = schemas.unset,
        pagination: typing.Union['Pagination', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StickersFindAnimatedStickersResponse':
        return super().__new__(
            cls,
            *args,
            data=data,
            meta=meta,
            pagination=pagination,
            _configuration=_configuration,
            **kwargs,
        )

from giphy_python_sdk.model.gif import Gif
from giphy_python_sdk.model.meta import Meta
from giphy_python_sdk.model.pagination import Pagination
