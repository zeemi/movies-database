
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from comments.models import Comment
from movies.models import Movie


class BaseTests(APITestCase):

    def setUp(self):
        self.COMMENTS_URL = reverse('comments')
        self.existing_movie = Movie.objects.create(title="SomeMovie")
        self.existing_comment = Comment.objects.create(movie=self.existing_movie, content="content of the comment")