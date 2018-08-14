import requests

from urllib.parse import urlencode

from django.conf import settings
from rest_framework import status

from .errors import OpenMovieDatabaseError


class OpenMovieDatabase(object):
    def __init__(self):
        self.api_key = settings.OMDBAPI_API_KEY
        self.base_url = 'http://www.omdbapi.com/'

    def __make_request(self, url):
        response = requests.get(url)
        data = response.json()
        if response.status_code != status.HTTP_200_OK:
            raise OpenMovieDatabaseError(response.status_code, data.get('Error', 'Something went wrong'))

        if data.get('Response') == 'False':
            error_message = data.get('Error', 'Something went wrong'),
            raise OpenMovieDatabaseError(
                status.HTTP_404_NOT_FOUND if error_message == 'Movie not found!' else status.HTTP_500_INTERNAL_SERVER_ERROR,
                error_message)

        return data

    def __prepare_url(self, query_params):
        return '{}?apikey={}&{}'.format(self.base_url, self.api_key, urlencode(query_params))

    def search(self, searchstring):
        return self.__make_request(self.__prepare_url({'s': searchstring}))

    def get_by_title(self, title):
        return self.__make_request(self.__prepare_url({'t': title}))