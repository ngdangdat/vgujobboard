
import logging.config
from .base import *
from core.utils import merge_dicts

DEBUG = True

LOGGING_DEV = {
    'loggers': {
        'django': {
            'propagate': True,
            'level': 'INFO',
            'handlers': ['console'],
        },
        'project': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
        'request': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    }
}

DATABASES['default'] = env.db()

FACEBOOK_ACCESS_TOKEN=env('FACEBOOK_ACCESS_TOKEN')
FACEBOOK_ALBUM_ID=env('FACEBOOK_ALBUM_ID')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

LOGGING = dict(merge_dicts(LOGGING, LOGGING_DEV))

INSTALLED_APPS_DEV = [
    'corsheaders',
]

INSTALLED_APPS += INSTALLED_APPS_DEV

MIDDLEWARE_DEV = [
    'corsheaders.middleware.CorsMiddleware',
]

MIDDLEWARE += MIDDLEWARE_DEV

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = False

CORS_ORIGIN_WHITELIST = (
    'localhost:8080',
    '*'
)

logging.config.dictConfig(LOGGING)
