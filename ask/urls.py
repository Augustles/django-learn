#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url,patterns # import url,patterns
from ask import views # import views

urlpatterns = patterns('',
        url(r'^$', views.index), # url函数两个必选项
        url(r'^answer/$',views.answer,name='answer'),
        url(r'^(?P<ask_id>\d+)/$',views.detail, name='detail'), # ?P<ask_id>为ask
        url(r'^add/$', views.ask_add),
        url(r'^add_done/$', views.add_done),
        )
