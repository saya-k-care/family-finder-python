
import sys
from openai.types.chat.chat_completion import ChatCompletion
import requests
from urllib.parse import unquote

def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)

import base64


import base64
import functools
import re

# Ref: https://stackoverflow.com/a/59023463/

_ENCODED_URL_PREFIX = "https://news.google.com/__i/rss/rd/articles/"
_ENCODED_URL_RE = re.compile(fr"^{re.escape(_ENCODED_URL_PREFIX)}(?P<encoded_url>[^?]+)")
_DECODED_URL_RE = re.compile(rb'^\x08\x13".+?(?P<primary_url>http[^\xd2]+)\xd2\x01')


@functools.lru_cache(2048)
def _decode_google_news_url(url: str) -> str:
    match = _ENCODED_URL_RE.match(url)
    encoded_text = match.groupdict()["encoded_url"]  # type: ignore
    encoded_text += "==="  # Fix incorrect padding. Ref: https://stackoverflow.com/a/49459036/
    decoded_text = base64.urlsafe_b64decode(encoded_text)

    match = _DECODED_URL_RE.match(decoded_text)
    primary_url = match.groupdict()["primary_url"]  # type: ignore
    primary_url = primary_url.decode()
    return primary_url


def decode_google_news_url(url: str) -> str:  # Not cached because not all Google News URLs are encoded.
    """Return Google News entry URLs after decoding their encoding as applicable."""
    return _decode_google_news_url(url) if url.startswith(_ENCODED_URL_PREFIX) else url

import requests

def expand_short_url(url):
    r = requests.head(url, allow_redirects=False)
    r.raise_for_status()
    if 300 < r.status_code < 400:
        url = r.headers.get('Location', url)
    return url

decoded = decode_google_news_url('https://news.google.com/rss/articles/CBMiWmh0dHBzOi8vd3d3Lm5zdC5jb20ubXkvbmV3cy9uYXRpb24vMjAyNC8wNy8xMDgyODM3L21hbGF5c2lhLWhhcy1hcHBsaWVkLWpvaW4tYnJpY3Mtc2F5cy1wbdIBXmh0dHBzOi8vd3d3Lm5zdC5jb20ubXkvYW1wL25ld3MvbmF0aW9uLzIwMjQvMDcvMTA4MjgzNy9tYWxheXNpYS1oYXMtYXBwbGllZC1qb2luLWJyaWNzLXNheXMtcG0?oc=5')
print(decoded)
sourceURL = "https://news.google.com/rss/articles/CBMiWmh0dHBzOi8vd3d3Lm5zdC5jb20ubXkvbmV3cy9uYXRpb24vMjAyNC8wNy8xMDgyODM3L21hbGF5c2lhLWhhcy1hcHBsaWVkLWpvaW4tYnJpY3Mtc2F5cy1wbdIBXmh0dHBzOi8vd3d3Lm5zdC5jb20ubXkvYW1wL25ld3MvbmF0aW9uLzIwMjQvMDcvMTA4MjgzNy9tYWxheXNpYS1oYXMtYXBwbGllZC1qb2luLWJyaWNzLXNheXMtcG0?oc=5"

import requests
getdata = requests.get(sourceURL)
print(getdata.status_code)
print(getdata.history) 


    