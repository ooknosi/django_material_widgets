"""
DJANGO MATERIAL WIDGETS PRODUCTION SETTINGS
config/settings/production.py
"""
# pylint: disable=wildcard-import, unused-wildcard-import

from .base import *

# THIS IS EXPLICITLY SET. DO NOT CHANGE THIS FOR SECURITY REASONS
DEBUG = False

#ALLOWED_HOSTS = ['###SET TO DOMAIN NAME###',]

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

# Static files (CSS, JavaScript, Images)
#STATIC_URL = '/static/'
#
#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "static"),
#]

# set this to cdn host
#STATIC_URL = ''
#MEDIA_URL = ''
