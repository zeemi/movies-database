from unittest.mock import Mock
from unittest import mock

from django.urls import reverse
from rest_framework.test import APITestCase

from ..models import Movie
from .resources import movie_definition

from ..views import OpenMovieDatabase


@mock.patch.object(OpenMovieDatabase, 'get_by_title', Mock(return_value=movie_definition))
class BaseTests(APITestCase):

    def setUp(self):
        self.MOVIES_URL = reverse('movies')
        self.not_indexed_movie_title = 'blade'
        self.not_indexed_movie_params = {'title': self.not_indexed_movie_title}
        self.important_properties = ['actors', 'awards', 'box_office', 'country', 'director', 'dvd', 'genre', 'imdb_id',
                                     'imdb_rating', 'imdb_votes', 'language', 'metascore', 'plot', 'poster',
                                     'production', 'rated', 'released', 'runtime', 'title', 'total_seasons', 'type',
                                     'website', 'writer', 'year']

        self.existing_movie = Movie.objects.create(title="SomeMovie")
