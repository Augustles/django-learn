#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url,patterns

from account import views

urlpatterns = patterns('',
        url(r'^register/$',views.register),
        url(r'^$',views.index),
        url(r'^login',views.login),
        )
