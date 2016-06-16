# -*- coding: utf-8 -*-

from django.conf.urls import include, url, patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .site import home

urlpatterns = patterns('core.site',
                       url(r'^$', 'home', name='home'),
                       )
