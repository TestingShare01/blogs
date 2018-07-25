# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
cursor = connection.cursor()
# Create your views here.
from django.db import models
import models,os,uuid,json
import datetime as dt
from mysite import settings
from django.core.paginator import Paginator

def index(request):
    head = models.headInfo.objects.all()
    con = models.content.objects.order_by("-start_time")
    cons = []
    for i in range(4):
        cons.append(con[i])
    see = models.content.objects.order_by("-views")
    fenlei = models.tenchology.objects.all()
    return render(request,"index.html",{"headd":head,"con":cons,"see_sum":see,"fenlei":fenlei})

def addinfo(request):
    contents = request.POST.get("content")
    phones = request.POST.get("phone")
    lianjies = request.POST.get("lianjie")
    print "contents-{},phones-{},lianjie--{}".format(contents,phones,lianjies)
    models.headInfo.objects.create(artice=contents,lianjie=lianjies,images=phones).save()
    return render(request,"addinfo.html")

def detail(request,nid):
    cons = models.content.objects.get(id=nid)
    cons.increase_views()
    see = models.content.objects.order_by("-views")

    return render(request,"listview.html",{"cons":cons,"see":see})

def tupian(request):
    return render(request,"tupian.html")


def tupians(request):
    # 测试上传图片
    if request.method == "POST":
        f1 = request.FILES['testimg']
        fname = '%s/%s' % (settings.MEDIA_ROOT, f1.name)
        print "图片地址--》{}".format(fname)
        with open(fname, 'wb') as pic:
            for c in f1.chunks():
                pic.write(c)
        return render(request, "tupian.html")
    else:
        return redirect(request,"tupian.html")


def fenleilist(request,nid,page):
    fenleilist = models.content.objects.filter(fenlei_id=nid)
    pagel = Paginator(fenleilist,3)
    sheet_num = pagel.page_range #返回页数，数组的形式（1，5），1到5页
    print "sheet-->{}".format(sheet_num)
    see = models.content.objects.order_by("-views")
    list_conent = pagel.page(page)
    #page = request.GET.get("page",1)
    return render(request,"list.html",locals())


def paglist(request):
    lenss = models.content.object.filter(fenlei_id = 1)
    print len(lenss)
    list1 = [i for i in range(0,lenss)]
    pagel = Paginator(list1,5)
    sheet = pagel.num_pages
    print "总页数--》{}".format(pagel.num_pages) #打印总的页数,即总记录数除以每页显示的条目数
    print "一页显示数据--》{}".format(pagel.page(1).object_list)


