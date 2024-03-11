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


class Gif(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def tags() -> typing.Type['GifTags']:
                return GifTags
            bitly_url = schemas.StrSchema
            content_url = schemas.StrSchema
            create_datetime = schemas.DateTimeSchema
            embded_url = schemas.StrSchema
        
            @staticmethod
            def featured_tags() -> typing.Type['GifFeaturedTags']:
                return GifFeaturedTags
            id = schemas.StrSchema
        
            @staticmethod
            def images() -> typing.Type['GifImages']:
                return GifImages
            import_datetime = schemas.DateTimeSchema
            rating = schemas.StrSchema
            slug = schemas.StrSchema
            source = schemas.StrSchema
            source_post_url = schemas.StrSchema
            source_tld = schemas.StrSchema
            trending_datetime = schemas.DateTimeSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "gif": "GIF",
                    }
                
                @schemas.classproperty
                def GIF(cls):
                    return cls("gif")
            update_datetime = schemas.DateTimeSchema
            url = schemas.StrSchema
        
            @staticmethod
            def user() -> typing.Type['User']:
                return User
            username = schemas.StrSchema
            __annotations__ = {
                "tags": tags,
                "bitly_url": bitly_url,
                "content_url": content_url,
                "create_datetime": create_datetime,
                "embded_url": embded_url,
                "featured_tags": featured_tags,
                "id": id,
                "images": images,
                "import_datetime": import_datetime,
                "rating": rating,
                "slug": slug,
                "source": source,
                "source_post_url": source_post_url,
                "source_tld": source_tld,
                "trending_datetime": trending_datetime,
                "type": type,
                "update_datetime": update_datetime,
                "url": url,
                "user": user,
                "username": username,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> 'GifTags': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bitly_url"]) -> MetaOapg.properties.bitly_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["content_url"]) -> MetaOapg.properties.content_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["create_datetime"]) -> MetaOapg.properties.create_datetime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["embded_url"]) -> MetaOapg.properties.embded_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["featured_tags"]) -> 'GifFeaturedTags': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["images"]) -> 'GifImages': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["import_datetime"]) -> MetaOapg.properties.import_datetime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rating"]) -> MetaOapg.properties.rating: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["slug"]) -> MetaOapg.properties.slug: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source_post_url"]) -> MetaOapg.properties.source_post_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source_tld"]) -> MetaOapg.properties.source_tld: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trending_datetime"]) -> MetaOapg.properties.trending_datetime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["update_datetime"]) -> MetaOapg.properties.update_datetime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'User': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tags", "bitly_url", "content_url", "create_datetime", "embded_url", "featured_tags", "id", "images", "import_datetime", "rating", "slug", "source", "source_post_url", "source_tld", "trending_datetime", "type", "update_datetime", "url", "user", "username", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union['GifTags', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bitly_url"]) -> typing.Union[MetaOapg.properties.bitly_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["content_url"]) -> typing.Union[MetaOapg.properties.content_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["create_datetime"]) -> typing.Union[MetaOapg.properties.create_datetime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["embded_url"]) -> typing.Union[MetaOapg.properties.embded_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["featured_tags"]) -> typing.Union['GifFeaturedTags', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["images"]) -> typing.Union['GifImages', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["import_datetime"]) -> typing.Union[MetaOapg.properties.import_datetime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rating"]) -> typing.Union[MetaOapg.properties.rating, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["slug"]) -> typing.Union[MetaOapg.properties.slug, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union[MetaOapg.properties.source, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source_post_url"]) -> typing.Union[MetaOapg.properties.source_post_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source_tld"]) -> typing.Union[MetaOapg.properties.source_tld, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trending_datetime"]) -> typing.Union[MetaOapg.properties.trending_datetime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["update_datetime"]) -> typing.Union[MetaOapg.properties.update_datetime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> typing.Union['User', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> typing.Union[MetaOapg.properties.username, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tags", "bitly_url", "content_url", "create_datetime", "embded_url", "featured_tags", "id", "images", "import_datetime", "rating", "slug", "source", "source_post_url", "source_tld", "trending_datetime", "type", "update_datetime", "url", "user", "username", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        tags: typing.Union['GifTags', schemas.Unset] = schemas.unset,
        bitly_url: typing.Union[MetaOapg.properties.bitly_url, str, schemas.Unset] = schemas.unset,
        content_url: typing.Union[MetaOapg.properties.content_url, str, schemas.Unset] = schemas.unset,
        create_datetime: typing.Union[MetaOapg.properties.create_datetime, str, datetime, schemas.Unset] = schemas.unset,
        embded_url: typing.Union[MetaOapg.properties.embded_url, str, schemas.Unset] = schemas.unset,
        featured_tags: typing.Union['GifFeaturedTags', schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        images: typing.Union['GifImages', schemas.Unset] = schemas.unset,
        import_datetime: typing.Union[MetaOapg.properties.import_datetime, str, datetime, schemas.Unset] = schemas.unset,
        rating: typing.Union[MetaOapg.properties.rating, str, schemas.Unset] = schemas.unset,
        slug: typing.Union[MetaOapg.properties.slug, str, schemas.Unset] = schemas.unset,
        source: typing.Union[MetaOapg.properties.source, str, schemas.Unset] = schemas.unset,
        source_post_url: typing.Union[MetaOapg.properties.source_post_url, str, schemas.Unset] = schemas.unset,
        source_tld: typing.Union[MetaOapg.properties.source_tld, str, schemas.Unset] = schemas.unset,
        trending_datetime: typing.Union[MetaOapg.properties.trending_datetime, str, datetime, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        update_datetime: typing.Union[MetaOapg.properties.update_datetime, str, datetime, schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        user: typing.Union['User', schemas.Unset] = schemas.unset,
        username: typing.Union[MetaOapg.properties.username, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Gif':
        return super().__new__(
            cls,
            *args,
            tags=tags,
            bitly_url=bitly_url,
            content_url=content_url,
            create_datetime=create_datetime,
            embded_url=embded_url,
            featured_tags=featured_tags,
            id=id,
            images=images,
            import_datetime=import_datetime,
            rating=rating,
            slug=slug,
            source=source,
            source_post_url=source_post_url,
            source_tld=source_tld,
            trending_datetime=trending_datetime,
            type=type,
            update_datetime=update_datetime,
            url=url,
            user=user,
            username=username,
            _configuration=_configuration,
            **kwargs,
        )

from giphy_python_sdk.model.gif_featured_tags import GifFeaturedTags
from giphy_python_sdk.model.gif_images import GifImages
from giphy_python_sdk.model.gif_tags import GifTags
from giphy_python_sdk.model.user import User
