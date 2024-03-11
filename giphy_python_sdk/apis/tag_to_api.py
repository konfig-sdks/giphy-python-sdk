import typing_extensions

from giphy_python_sdk.apis.tags import TagValues
from giphy_python_sdk.apis.tags.gifs_api import GifsApi
from giphy_python_sdk.apis.tags.stickers_api import StickersApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.GIFS: GifsApi,
        TagValues.STICKERS: StickersApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.GIFS: GifsApi,
        TagValues.STICKERS: StickersApi,
    }
)
