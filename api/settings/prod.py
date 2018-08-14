from .base import *
import dj_database_url

DATABASES['default'] = dj_database_url.config()
DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'

DEBUG = True

OMDBAPI_API_KEY = os.environ.get('MOVIE_DB__OMDBAPI_API_KEY')

CORS_ORIGIN_REGEX_WHITELIST = (r'^(https?://)?localhost:\d+$',)

ALLOWED_HOSTS = ['movie-database-2018.herokuapp.com']