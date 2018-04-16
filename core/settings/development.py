
import logging.config
from .base import *
from core.utils import merge_dicts

DEBUG = True

LOGGING_DEV = {
    'loggers': {
        'django': {
            'propagate': True,
            'level': 'DEBUG',
        },
        'project': {
            'level': 'DEBUG',
        },
        'request': {
            'level': 'DEBUG',
        }
    }
}

DATABASES['default'] = env.db()

FACEBOOK_ACCESS_TOKEN=env('FACEBOOK_ACCESS_TOKEN')
FACEBOOK_ALBUM_ID=env('FACEBOOK_ALBUM_ID')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

LOGGING = dict(merge_dicts(LOGGING, LOGGING_DEV))

logging.config.dictConfig(LOGGING)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [join(BASE_DIR, 'static')]
