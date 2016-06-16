# -*- coding: utf-8 -*-

from django.conf.urls import include, url, patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *

urlpatterns = patterns('stock.views',
                       url(r'^medicament/add/$', 'add_medicament', name='add_medicament'),
                       url(r'^medicament/$', 'list_medicament', name='list_medicament'),
                       url(r'^medicament/edit/(?P<pk>[0-9]+)$', 'edit_medicament', name='edit_medicament'),
                       url(r'^medicament/remove/(?P<pk>[0-9]+)$', 'remove_medicament', name='remove_medicament'),
                       url(r'^bill/add/$', 'add_bill', name='add_bill'),
                       url(r'^bill/$', 'list_bill', name='list_bill'),
                       url(r'^bill/edit/(?P<pk>[0-9]+)$', 'edit_bill', name='edit_bill'),
                       url(r'^bill/remove/(?P<pk>[0-9]+)$', 'remove_bill', name='remove_bill'),
                       )
