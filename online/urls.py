#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url, patterns
from online import views

urlpatterns = patterns('',
                       url(r'^$', views.index),
                       url(r'^register/$', views.register),
                       url(r'^login/$', views.login),
                       url(r'^logout/$', views.logout),
                       )
