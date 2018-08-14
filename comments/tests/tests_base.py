
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from comments.models import Comment
from movies.models import Movie


class BaseTests(APITestCase):

    def setUp(self):
        self.COMMENTS_URL = reverse('comments')
        self.first_existing_movie = Movie.objects.create(title="first_movie")
        self.second_existing_movie = Movie.objects.create(title="another_movie")
        self.first_movie_comment = Comment.objects.create(movie=self.first_existing_movie, content="content of the comment")
        self.second_movie_comment = Comment.objects.create(movie=self.second_existing_movie, content="content of the comment")