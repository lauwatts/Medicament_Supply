# -*- coding: utf-8 -*-

from django.conf.urls import include, url, patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *

urlpatterns = patterns('client.views',
                       url(r'^add/$', 'add', name='add'),
                       url(r'^$', 'list', name='list'),
                       url(r'^edit/(?P<pk>[0-9]+)$', 'edit', name='edit'),
                       url(r'^remove/(?P<pk>[0-9]+)$', 'remove', name='remove'),
                       )
