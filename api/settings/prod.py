from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
    }
}

DEBUG = False

OMDBAPI_API_KEY = os.environ.get('MOVIE_DB__OMDBAPI_API_KEY')

CORS_ORIGIN_REGEX_WHITELIST = (r'^(https?://)?localhost:\d+$',)

ALLOWED_HOSTS = ['*']
