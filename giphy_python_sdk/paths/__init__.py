# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from giphy_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    GIFS = "/gifs"
    GIFS_RANDOM = "/gifs/random"
    GIFS_SEARCH = "/gifs/search"
    GIFS_TRANSLATE = "/gifs/translate"
    GIFS_TRENDING = "/gifs/trending"
    GIFS_GIF_ID = "/gifs/{gifId}"
    STICKERS_RANDOM = "/stickers/random"
    STICKERS_SEARCH = "/stickers/search"
    STICKERS_TRANSLATE = "/stickers/translate"
    STICKERS_TRENDING = "/stickers/trending"
