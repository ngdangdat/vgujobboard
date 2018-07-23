import logging.config
import sys

from core.utils import merge_dicts
from .base import *

DEBUG = True
TESTING = True
TEMPLATES[0]['OPTIONS'].update({ 'debug': True })

INSTALLED_APPS += ('django_nose', )

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
  '--cover-package=core,admin,api,user',
  '--nologcapture',
  '--nocapture',
]

if "celery" in sys.argv[0]:
  DEBUG = False

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGFILE_ROOT = join(BASE_DIR, 'logs')

STATIC_URL = join(BASE_DIR, 'static/')

TEST_NON_SERIALIZED_APPS = [
  'api',
]

ROOT_URLCONF = 'core.urls'

DATABASES = {
    'default': {
        'NAME': 'db.sqlite3',
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

TEST_UPLOAD = 'test_upload'
MEDIA_ROOT = join(BASE_DIR, TEST_UPLOAD)
UPLOAD_TEMP_DIR = join(MEDIA_ROOT, 'temp')

LOGGING_TEST = {
    'handlers': {
        'django_log_file': {
            'level': 'DEBUG',
            'filename': join(LOGFILE_ROOT, 'test_django.log'),
        },
        'proj_log_file': {
            'level': 'DEBUG',
            'filename': join(LOGFILE_ROOT, 'test_project.log'),
        },
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
        },
        'request_log_file': {
            'level': 'DEBUG',
            'filename': join(LOGFILE_ROOT, 'test_request.log'),
        },
    },
}

LOGGING = dict(merge_dicts(LOGGING, LOGGING_TEST))

logging.config.dictConfig(LOGGING)
