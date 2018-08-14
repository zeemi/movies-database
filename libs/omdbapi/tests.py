import json
import unittest

import requests_mock
from django.conf import settings

from .errors import OpenMovieDatabaseError
from .tests_resources import successful_response, failing_response__movie_not_found, failing_response__unknown_error
from . import OpenMovieDatabase


@requests_mock.mock()
class TestOMDBAPIWrapper(unittest.TestCase):

    def setUp(self):
        self.omdb = OpenMovieDatabase()
        self.title = 'blade'
        self.omdb_base_url = 'http://www.omdbapi.com/'

    def test_omdb_requests_pass_api_token(self, request_mock_adapter):
        request_mock_adapter.register_uri(
            'GET',
            '?apikey={}'.format(settings.OMDBAPI_API_KEY),
            text='{"Response": true}'
        )
        self.omdb.get_by_title(self.title)
        self.assertEqual(request_mock_adapter.call_count, 1)

    def test_omdb_get_by_title_sends_proper_get_request(self, request_mock_adapter):
        request_mock_adapter.register_uri(
            'GET',
            '{}?apikey={}&t={}'.format(self.omdb_base_url, settings.OMDBAPI_API_KEY, self.title),
            text='{"Response": true}'
        )
        self.omdb.get_by_title(self.title)
        self.assertEqual(request_mock_adapter.call_count, 1)

    def test_omdb_request_returns_proper_data_on_success(self, request_mock_adapter):
        request_mock_adapter.register_uri(
            'GET',
            '?t={}'.format(self.title),
            text=successful_response
        )
        movie = self.omdb.get_by_title(self.title)
        self.assertEqual(movie, json.loads(successful_response))

    def test_omdb_request_propagate_http_errors_by_raising_proper_exception(self, request_mock_adapter):
        request_mock_adapter.register_uri(
            'GET',
            '?t={}'.format(self.title),
            text=successful_response,
            status_code=429
        )
        with self.assertRaises(OpenMovieDatabaseError) as exp:
            self.omdb.get_by_title(self.title)
            self.assertEqual(exp.status_code, 429)
            self.assertEqual(exp.message, 'Something went wrong')

    def test_omdb_request_raises_exception_on_data_not_found(self, request_mock_adapter):
        request_mock_adapter.register_uri(
            'GET',
            '?t={}'.format(self.title),
            text=failing_response__movie_not_found
        )
        with self.assertRaises(OpenMovieDatabaseError) as exp:
            self.omdb.get_by_title(self.title)
            self.assertEqual(exp.status_code, 404)
            self.assertEqual(exp.message, 'Movie not found!')

    def test_omdb_request_raises_exception_with_status_500_on_failure_other_then_404(self, request_mock_adapter):
        request_mock_adapter.register_uri(
            'GET',
            '?t={}'.format(self.title),
            text=failing_response__unknown_error
        )
        with self.assertRaises(OpenMovieDatabaseError) as exp:
            self.omdb.get_by_title(self.title)
            self.assertEqual(exp.status_code, 500)
            self.assertEqual(exp.message, 'Something went wrong')

    def test_omdb_search_sends_proper_get_request(self, request_mock_adapter):
        request_mock_adapter.register_uri(
            'GET',
            '{}?apikey={}&s={}'.format(self.omdb_base_url, settings.OMDBAPI_API_KEY, self.title),
            text='{"Response": true}'
        )
        self.omdb.search(self.title)
        self.assertEqual(request_mock_adapter.call_count, 1)
