#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import patterns,url

from disk import views
urlpatterns = patterns('',
        url(r'^register/$',views.register),
        )
