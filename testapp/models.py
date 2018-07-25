#coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class headInfo(models.Model):
    id = models.AutoField(primary_key=True)
    images = models.CharField(max_length=50,null=True)
    lianjie = models.CharField(max_length=50,null=True)
    artice = models.CharField(max_length=50,null=True)


class tenchology(models.Model):
    uid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)

class content(models.Model):#文章表
    title = models.CharField(max_length=100)
    #分类创建数据路关联字段，关联tenchology，自增uid
    fenlei = models.ForeignKey("tenchology",to_field="uid",default=1)
    article = models.TextField(null=True)
    zan_num = models.IntegerField()
    pinglun = models.IntegerField()
    start_time = models.DateTimeField(auto_now=True,null=True)
    content_images = models.CharField(max_length=50)
    see_sum = models.IntegerField()
    views = models.PositiveIntegerField(default=0)    #记录阅读数量，此字段默认是正整数，设置初始值为0

    def increase_views(self):
        #此方法用于浏览数增加
        self.views += 1
        self.save(update_fields=["views"])

