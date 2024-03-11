import typing_extensions

from giphy_python_sdk.paths import PathValues
from giphy_python_sdk.apis.paths.gifs import Gifs
from giphy_python_sdk.apis.paths.gifs_random import GifsRandom
from giphy_python_sdk.apis.paths.gifs_search import GifsSearch
from giphy_python_sdk.apis.paths.gifs_translate import GifsTranslate
from giphy_python_sdk.apis.paths.gifs_trending import GifsTrending
from giphy_python_sdk.apis.paths.gifs_gif_id import GifsGifId
from giphy_python_sdk.apis.paths.stickers_random import StickersRandom
from giphy_python_sdk.apis.paths.stickers_search import StickersSearch
from giphy_python_sdk.apis.paths.stickers_translate import StickersTranslate
from giphy_python_sdk.apis.paths.stickers_trending import StickersTrending

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.GIFS: Gifs,
        PathValues.GIFS_RANDOM: GifsRandom,
        PathValues.GIFS_SEARCH: GifsSearch,
        PathValues.GIFS_TRANSLATE: GifsTranslate,
        PathValues.GIFS_TRENDING: GifsTrending,
        PathValues.GIFS_GIF_ID: GifsGifId,
        PathValues.STICKERS_RANDOM: StickersRandom,
        PathValues.STICKERS_SEARCH: StickersSearch,
        PathValues.STICKERS_TRANSLATE: StickersTranslate,
        PathValues.STICKERS_TRENDING: StickersTrending,
    }
)

path_to_api = PathToApi(
    {
        PathValues.GIFS: Gifs,
        PathValues.GIFS_RANDOM: GifsRandom,
        PathValues.GIFS_SEARCH: GifsSearch,
        PathValues.GIFS_TRANSLATE: GifsTranslate,
        PathValues.GIFS_TRENDING: GifsTrending,
        PathValues.GIFS_GIF_ID: GifsGifId,
        PathValues.STICKERS_RANDOM: StickersRandom,
        PathValues.STICKERS_SEARCH: StickersSearch,
        PathValues.STICKERS_TRANSLATE: StickersTranslate,
        PathValues.STICKERS_TRENDING: StickersTrending,
    }
)
