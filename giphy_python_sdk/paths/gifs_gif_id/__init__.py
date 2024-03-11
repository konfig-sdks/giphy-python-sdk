# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from giphy_python_sdk.paths.gifs_gif_id import Api

from giphy_python_sdk.paths import PathValues

path = PathValues.GIFS_GIF_ID