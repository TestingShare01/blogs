# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from testapp.models import *
# Register your models here.

admin.site.register(headInfo)
admin.site.register(tenchology)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']
    class Media:
        js = ('/static/js/kindeditor/kindeditor-all-min.js',
              '/static/js/kindeditor/lang/zh-CN.js',
              '/static/js/kindeditor/config.js')

admin.site.register(content,ArticleAdmin)