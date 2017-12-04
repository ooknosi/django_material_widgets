"""
DJANGO MATERIAL WIDGETS READTHEDOCS SETTINGS
config/settings/readthedocs.py
"""
# pylint: disable=wildcard-import, unused-wildcard-import

from config.settings.base import *

### SECURITY WARNING: DO NOT USE READTHEDOCS SETTINGS IN PRODUCTION
DEBUG = True

SECRET_KEY = "THIS IS A SECRET KEY"
###

INSTALLED_APPS += ['material_widgets',]

ALLOWED_HOSTS = ['localhost',]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
