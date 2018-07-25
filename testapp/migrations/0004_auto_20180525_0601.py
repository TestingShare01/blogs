# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-25 06:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20180511_0327'),
    ]

    operations = [
        migrations.CreateModel(
            name='content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('article', models.TextField(null=True)),
                ('zan_num', models.IntegerField()),
                ('pinglun', models.IntegerField()),
                ('start_time', models.DateTimeField(auto_now=True, null=True)),
                ('content_images', models.CharField(max_length=50)),
                ('see_sum', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tenchology',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='fenlei',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='testapp.tenchology'),
        ),
    ]