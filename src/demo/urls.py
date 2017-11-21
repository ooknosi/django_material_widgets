"""
DJANGO MATERIAL WIDGETS DEMO URL CONFIGURATION
demo/urls.py
"""
# pylint: disable=invalid-name

from django.conf.urls import url
from . import views

app_name = 'demo'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^modelform/$', views.DemoModelFormView.as_view(), name='modelform'),
    ]
