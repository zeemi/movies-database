from unittest.mock import Mock
from unittest import mock

from rest_framework import status

from .tests_base import BaseTests
from ..models import Movie
from ..utils import normalize_keys
from .resources import movie_definition

from ..views import OpenMovieDatabase


@mock.patch.object(OpenMovieDatabase, 'get_by_title', Mock(return_value=movie_definition))
class ListMoviesTests(BaseTests):

    def test_listing_movies_returns_status_200(self):
        response = self.client.get(self.MOVIES_URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_listing_movies_returns_all_existing_movies(self):
        response = self.client.get(self.MOVIES_URL, format='json')
        self.assertEqual(Movie.objects.count(), len(response.data))
