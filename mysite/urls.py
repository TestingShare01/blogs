"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from django.contrib import admin
from mysite import settings
from testapp import views
from django.views.static import serve
from testapp.upload import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index, name="index"),
    url(r'^tupian/', views.tupian, name="tupian"),
    url(r'^tupians/', views.tupians, name="tupians"),
    url(r'^addinfo/', views.addinfo, name="addinfo"),
    url(r'^detail-(?P<nid>\d+)/', views.detail),
    url(r'^fenlist-(?P<nid>\d+)-(?P<page>\d+)/', views.fenleilist),

    url(r'uploads/(?P<path>.*)$',serve,{'document_root': settings.MEDIA_ROOT, }),
    url(r'^admin/upload/(?P<dir_name>[^/]+)$',upload_image, name='upload_image'),

]
