# coding: utf-8

"""
    Giphy API

    Giphy API

    The version of the OpenAPI document: 1.0
    Contact: support@giphy.com
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import giphy_python_sdk
from giphy_python_sdk.paths.gifs_random import get
from giphy_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestGifsRandom(ApiTestMixin, unittest.TestCase):
    """
    GifsRandom unit test stubs
        Random GIF
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()