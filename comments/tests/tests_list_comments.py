from rest_framework import status

from .tests_base import BaseTests
from ..models import Comment


class ListCommentsTests(BaseTests):

    def test_listing_comments_returns_status_200(self):
        response = self.client.get(self.COMMENTS_URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_listing_movies_returns_all_existing_comments(self):
        response = self.client.get(self.COMMENTS_URL, format='json')
        self.assertEqual(Comment.objects.count(), len(response.data))
