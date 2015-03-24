#!/usr/bin/env python
# encoding: utf-8

from django.contrib import admin
from ask.models import Ask,Answer

class AskAdmin(admin.ModelAdmin):
    search_fields = ['content']

admin.site.register(Ask,AskAdmin)
admin.site.register(Answer)
