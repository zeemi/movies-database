from rest_framework import status

from .tests_base import BaseTests
from ..models import Comment


class AddCommentTests(BaseTests):

    def test_adding_comment_returns_201_status(self):
        response = self.client.post(self.COMMENTS_URL, data={'movie': self.existing_movie.id, 'content': 'Content'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_adding_comment_created_new_comment_instance(self):
        comments_count = Comment.objects.count()
        self.client.post(self.COMMENTS_URL, data={'movie': self.existing_movie.id, 'content': 'Content'},
                                    format='json')
        self.assertEqual(comments_count + 1, Comment.objects.count())