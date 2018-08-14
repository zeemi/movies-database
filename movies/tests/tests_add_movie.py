from unittest.mock import Mock
from unittest import mock

from rest_framework import status

from libs.omdbapi import OpenMovieDatabaseError
from .tests_base import BaseTests
from ..models import Movie
from ..utils import normalize_keys
from .resources import movie_definition

from ..views import OpenMovieDatabase


@mock.patch.object(OpenMovieDatabase, 'get_by_title', Mock(return_value=movie_definition))
class AddMovieTests(BaseTests):

    def test_request_for_not_indexed_movie_returns_201_status(self):
        response = self.client.post(self.MOVIES_URL, data=self.not_indexed_movie_params, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_request_for_not_indexed_movie_creates_new_movie_instance(self):
        movies_count = Movie.objects.count()
        self.client.post(self.MOVIES_URL, data=self.not_indexed_movie_params, format='json')
        self.assertEqual(movies_count + 1, Movie.objects.count())

    def test_response_of_successful_creation_contains_movie_details(self):
        response = self.client.post(self.MOVIES_URL, data=self.not_indexed_movie_params, format='json')
        for property in self.important_properties:
            self.assertEqual(response.data[property], normalize_keys(movie_definition).get(property, None))

        for response_rating, expected_rating in zip(response.data['ratings'], normalize_keys(movie_definition)['ratings']):
            for rating_key in ['source', 'value']:
                self.assertEqual(response_rating[rating_key], normalize_keys(expected_rating)[rating_key])

    def test_creating_movie_without_title_returns_400_with_proper_detail_message(self):
        response = self.client.post(self.MOVIES_URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['title'][0].code, 'required')

    def test_omdb_exception_is_propagated_to_requests_status(self):
        with mock.patch.object(OpenMovieDatabase, 'get_by_title', Mock(side_effect=OpenMovieDatabaseError(status.HTTP_404_NOT_FOUND, 'NotFound'))):
            response = self.client.post(self.MOVIES_URL, data=self.not_indexed_movie_params, format='json')
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
