import unittest

import requests_mock
from django.conf import settings

from . import OpenMovieDatabase


@requests_mock.mock()
class TestOMDBAPIWrapper(unittest.TestCase):

    def setUp(self):
        self.omdb = OpenMovieDatabase()
        self.title = 'blade'

    def test_omdb_requests_pass_api_token(self, request_mock_adapter):
        request_mock_adapter.register_uri(
            'GET',
            '?apikey={}'.format(settings.OMDBAPI_API_KEY),
            text='{"Response": true}'
        )
        self.omdb.get_by_title(self.title)
        self.assertEqual(request_mock_adapter.call_count, 1)
