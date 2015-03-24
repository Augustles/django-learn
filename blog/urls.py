#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import patterns, url

from blog import views
urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^(?P<blog_id>\d+)/$', views.detail),
    url(r'^(?P<blog_id>\d+)/comment/$', views.comment),
    url(r'^(?P<blog_id>\d+)/thanks/$',views.thanks)
)
