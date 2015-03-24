#!/usr/bin/env python
# encoding: utf-8

from django.contrib import admin
from account.models import User

class AccountAdmin(admin.ModelAdmin):
    fields = ['username','password','email']
    list_display = ('username','email')
    list_display_link = ('username','email')
    #list_editable = ('email',)
    search_fields = ('username','email')
    list_filter = ('username','email')
    date_hierarchy = ()
    ordering = ('username','email')
    #list_per_page = 1
    readonly_fields = ('username',)
    actions_on_top = True
admin.site.register(User,AccountAdmin)
