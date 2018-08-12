# In production set the environment variable like this:
#    DJANGO_SETTINGS_MODULE=core.settings.production
from .base import *             # NOQA
import logging.config
import dj_database_url

# For security and performance reasons, DEBUG is turned off
DEBUG = False
TEMPLATE_DEBUG = False

INSTALLED_APPS = INSTALLED_APPS + ['whitenoise.runserver_nostatic',]

MIDDLEWARE = MIDDLEWARE + ['whitenoise.middleware.WhiteNoiseMiddleware',]

# Must mention ALLOWED_HOSTS in production!
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', 'vgualumni-test.herokuapp.com', 'vgu-alumni.herokuapp.com']

logging.config.dictConfig(LOGGING)

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'dist/static'),
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

FACEBOOK_ACCESS_TOKEN=os.environ.get('FACEBOOK_ACCESS_TOKEN')
FACEBOOK_ALBUM_ID=os.environ.get('FACEBOOK_ALBUM_ID')
