from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'netguru_{}'.format(BASE_DIR),
        'USER': 'netguru',
        'PASSWORD': os.environ.get('NETGURU__MYSQL_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}

DEBUG = False

CORS_ORIGIN_REGEX_WHITELIST = (r'^(https?://)?localhost:\d+$',)

# ALLOWED_HOSTS = ['localhost']