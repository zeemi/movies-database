from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AddMovieTests(APITestCase):
    def setUp(self):
        self.API = reverse('add-movie')

    def test_post_request_returns_201_status(self):
        print(self.API)
        response = self.client.post(self.API, data={'title': 'something'}, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_request_returns_201_status_data(self):
        response = self.client.post(self.API, data={'title': 'something'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_creating_movie_without_title_returns_400_with_proper_detail_message(self):
        response = self.client.post(self.API, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['title'][0].code, 'required')
