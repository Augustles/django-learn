#!/usr/bin/env python
# encoding: utf-8

from django.contrib import admin
from blog.models import Blogpost, Post

admin.site.register(Blogpost)
# admin.site.register(Post)
