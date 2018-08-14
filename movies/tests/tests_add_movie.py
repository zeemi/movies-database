from unittest.mock import Mock
from unittest import mock

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Movie
from ..utils import convert, convert_dict_keys
from .resources import movie_definition

from ..views import OpenMovieDatabase


@mock.patch.object(OpenMovieDatabase, 'get_by_title', Mock(return_value=movie_definition))
class AddMovieTests(APITestCase):
    def setUp(self):
        self.API = reverse('add-movie')
        self.not_indexed_movie_title = 'blade'
        self.not_indexed_movie_params = {'title': self.not_indexed_movie_title}

    def test_request_for_not_indexed_movie_returns_201_status(self):
        response = self.client.post(self.API, data=self.not_indexed_movie_params, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_request_for_not_indexed_movie_creates_new_movie_instance(self):
        movies_count = Movie.objects.count()
        self.client.post(self.API, data=self.not_indexed_movie_params, format='json')
        self.assertEqual(movies_count + 1, Movie.objects.count())

    def test_response_of_successful_creation_contains_movie_details(self):
        response = self.client.post(self.API, data=self.not_indexed_movie_params, format='json')
        self.assertDictEqual(response.data, convert_dict_keys(movie_definition))

    def test_creating_movie_without_title_returns_400_with_proper_detail_message(self):
        response = self.client.post(self.API, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['title'][0].code, 'required')
