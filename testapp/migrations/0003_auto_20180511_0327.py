# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-11 03:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20180511_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headinfo',
            name='artice',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='headinfo',
            name='images',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='headinfo',
            name='lianjie',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
