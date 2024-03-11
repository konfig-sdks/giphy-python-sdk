<div align="center">

[![Visit Giphy](./header.png)](https://giphy.com)

# Giphy<a id="giphy"></a>

Giphy API


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`giphy.gifs.get_by_id`](#giphygifsget_by_id)
  * [`giphy.gifs.get_by_ids`](#giphygifsget_by_ids)
  * [`giphy.gifs.get_random_gif`](#giphygifsget_random_gif)
  * [`giphy.gifs.get_trending_gifs`](#giphygifsget_trending_gifs)
  * [`giphy.gifs.search_gifs`](#giphygifssearch_gifs)
  * [`giphy.gifs.translate_phrase_gif`](#giphygifstranslate_phrase_gif)
  * [`giphy.stickers.find_animated_stickers`](#giphystickersfind_animated_stickers)
  * [`giphy.stickers.get_random`](#giphystickersget_random)
  * [`giphy.stickers.get_trending`](#giphystickersget_trending)
  * [`giphy.stickers.translate_phrase_to_sticker`](#giphystickerstranslate_phrase_to_sticker)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Giphy&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from giphy_python_sdk import Giphy, ApiException

giphy = Giphy(
    api_key="YOUR_API_KEY",
)

try:
    # Get GIF by Id
    get_by_id_response = giphy.gifs.get_by_id(
        gif_id=1,
    )
    print(get_by_id_response)
except ApiException as e:
    print("Exception when calling GifsApi.get_by_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from giphy_python_sdk import Giphy, ApiException

giphy = Giphy(
    api_key="YOUR_API_KEY",
)


async def main():
    try:
        # Get GIF by Id
        get_by_id_response = await giphy.gifs.aget_by_id(
            gif_id=1,
        )
        print(get_by_id_response)
    except ApiException as e:
        print("Exception when calling GifsApi.get_by_id: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from giphy_python_sdk import Giphy, ApiException

giphy = Giphy(
    api_key="YOUR_API_KEY",
)

try:
    # Get GIF by Id
    get_by_id_response = giphy.gifs.raw.get_by_id(
        gif_id=1,
    )
    pprint(get_by_id_response.body)
    pprint(get_by_id_response.body["data"])
    pprint(get_by_id_response.body["meta"])
    pprint(get_by_id_response.headers)
    pprint(get_by_id_response.status)
    pprint(get_by_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling GifsApi.get_by_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `giphy.gifs.get_by_id`<a id="giphygifsget_by_id"></a>

Returns a GIF given that GIF's unique ID


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = giphy.gifs.get_by_id(
    gif_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### gif_id: `int`<a id="gif_id-int"></a>

Filters results by specified GIF ID.

#### 🔄 Return<a id="🔄-return"></a>

[`GifsGetByIdResponse`](./giphy_python_sdk/pydantic/gifs_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/gifs/{gifId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `giphy.gifs.get_by_ids`<a id="giphygifsget_by_ids"></a>

A multiget version of the get GIF by ID endpoint.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_ids_response = giphy.gifs.get_by_ids(
    ids="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: `str`<a id="ids-str"></a>

Filters results by specified GIF IDs, separated by commas.

#### 🔄 Return<a id="🔄-return"></a>

[`GifsGetByIdsResponse`](./giphy_python_sdk/pydantic/gifs_get_by_ids_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/gifs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `giphy.gifs.get_random_gif`<a id="giphygifsget_random_gif"></a>

Returns a random GIF, limited by tag. Excluding the tag parameter will return a random GIF from the GIPHY catalog.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_random_gif_response = giphy.gifs.get_random_gif(
    tag="string_example",
    rating="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tag: `str`<a id="tag-str"></a>

Filters results by specified tag.

##### rating: `str`<a id="rating-str"></a>

Filters results by specified rating.

#### 🔄 Return<a id="🔄-return"></a>

[`GifsGetRandomGifResponse`](./giphy_python_sdk/pydantic/gifs_get_random_gif_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/gifs/random` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `giphy.gifs.get_trending_gifs`<a id="giphygifsget_trending_gifs"></a>

Fetch GIFs currently trending online. Hand curated by the GIPHY editorial team.  The data returned mirrors the GIFs showcased on the GIPHY homepage. Returns 25 results by default.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_trending_gifs_response = giphy.gifs.get_trending_gifs(
    limit=25,
    offset=0,
    rating="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of records to return.

##### offset: `int`<a id="offset-int"></a>

An optional results offset.

##### rating: `str`<a id="rating-str"></a>

Filters results by specified rating.

#### 🔄 Return<a id="🔄-return"></a>

[`GifsGetTrendingGifsResponse`](./giphy_python_sdk/pydantic/gifs_get_trending_gifs_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/gifs/trending` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `giphy.gifs.search_gifs`<a id="giphygifssearch_gifs"></a>

Search all GIPHY GIFs for a word or phrase. Punctuation will be stripped and ignored.  Use a plus or url encode for phrases. Example paul+rudd, ryan+gosling or american+psycho.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_gifs_response = giphy.gifs.search_gifs(
    q="q_example",
    limit=25,
    offset=0,
    rating="string_example",
    lang="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

Search query term or prhase.

##### limit: `int`<a id="limit-int"></a>

The maximum number of records to return.

##### offset: `int`<a id="offset-int"></a>

An optional results offset.

##### rating: `str`<a id="rating-str"></a>

Filters results by specified rating.

##### lang: `str`<a id="lang-str"></a>

Specify default language for regional content; use a 2-letter ISO 639-1 language code.

#### 🔄 Return<a id="🔄-return"></a>

[`GifsSearchGifsResponse`](./giphy_python_sdk/pydantic/gifs_search_gifs_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/gifs/search` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `giphy.gifs.translate_phrase_gif`<a id="giphygifstranslate_phrase_gif"></a>

The translate API draws on search, but uses the GIPHY `special sauce` to handle translating from one vocabulary to another. In this case, words and phrases to GIF


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
translate_phrase_gif_response = giphy.gifs.translate_phrase_gif(
    s="s_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### s: `str`<a id="s-str"></a>

Search term.

#### 🔄 Return<a id="🔄-return"></a>

[`GifsTranslatePhraseGifResponse`](./giphy_python_sdk/pydantic/gifs_translate_phrase_gif_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/gifs/translate` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `giphy.stickers.find_animated_stickers`<a id="giphystickersfind_animated_stickers"></a>

Replicates the functionality and requirements of the classic GIPHY search, but returns animated stickers rather than GIFs.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_animated_stickers_response = giphy.stickers.find_animated_stickers(
    q="q_example",
    limit=25,
    offset=0,
    rating="string_example",
    lang="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

Search query term or prhase.

##### limit: `int`<a id="limit-int"></a>

The maximum number of records to return.

##### offset: `int`<a id="offset-int"></a>

An optional results offset.

##### rating: `str`<a id="rating-str"></a>

Filters results by specified rating.

##### lang: `str`<a id="lang-str"></a>

Specify default language for regional content; use a 2-letter ISO 639-1 language code.

#### 🔄 Return<a id="🔄-return"></a>

[`StickersFindAnimatedStickersResponse`](./giphy_python_sdk/pydantic/stickers_find_animated_stickers_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/stickers/search` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `giphy.stickers.get_random`<a id="giphystickersget_random"></a>

Returns a random GIF, limited by tag. Excluding the tag parameter will return a random GIF from the GIPHY catalog.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_random_response = giphy.stickers.get_random(
    tag="string_example",
    rating="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tag: `str`<a id="tag-str"></a>

Filters results by specified tag.

##### rating: `str`<a id="rating-str"></a>

Filters results by specified rating.

#### 🔄 Return<a id="🔄-return"></a>

[`StickersGetRandomResponse`](./giphy_python_sdk/pydantic/stickers_get_random_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/stickers/random` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `giphy.stickers.get_trending`<a id="giphystickersget_trending"></a>

Fetch Stickers currently trending online. Hand curated by the GIPHY editorial team. Returns 25 results by default.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_trending_response = giphy.stickers.get_trending(
    limit=25,
    offset=0,
    rating="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of records to return.

##### offset: `int`<a id="offset-int"></a>

An optional results offset.

##### rating: `str`<a id="rating-str"></a>

Filters results by specified rating.

#### 🔄 Return<a id="🔄-return"></a>

[`StickersGetTrendingResponse`](./giphy_python_sdk/pydantic/stickers_get_trending_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/stickers/trending` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `giphy.stickers.translate_phrase_to_sticker`<a id="giphystickerstranslate_phrase_to_sticker"></a>

The translate API draws on search, but uses the GIPHY `special sauce` to handle translating from one vocabulary to another. In this case, words and phrases to GIFs.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
translate_phrase_to_sticker_response = giphy.stickers.translate_phrase_to_sticker(
    s="s_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### s: `str`<a id="s-str"></a>

Search term.

#### 🔄 Return<a id="🔄-return"></a>

[`StickersTranslatePhraseToStickerResponse`](./giphy_python_sdk/pydantic/stickers_translate_phrase_to_sticker_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/stickers/translate` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
