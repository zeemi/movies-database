from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'MOVIE_DB_{}'.format(BASE_DIR),
        'USER': 'MOVIE_DB_ADMIN',
        'PASSWORD': os.environ.get('MOVIE_DB_ADMIN__MYSQL_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}

DEBUG = False

OMDBAPI_API_KEY = os.environ.get('MOVIE_DB__OMDBAPI_API_KEY')

CORS_ORIGIN_REGEX_WHITELIST = (r'^(https?://)?localhost:\d+$',)

# ALLOWED_HOSTS = ['localhost']