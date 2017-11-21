"""
DJANGO MATERIAL WIDGETS TEST ENVIRONMENT SETTINGS
config/settings/test.py
"""
# pylint: disable=wildcard-import, unused-wildcard-import

from .base import *

# Debug explicitly declared False to match production environment
# https://docs.djangoproject.com/en/dev/topics/testing/overview/#other-test-conditions
DEBUG = False

SECRET_KEY = get_env_variable("SECRET_KEY")

INSTALLED_APPS += ['material_widgets', 'material_widgets.tests',]

ALLOWED_HOSTS = ['localhost',]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'test_db.sqlite3'),
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
