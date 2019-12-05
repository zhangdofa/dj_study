# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('username', models.CharField(primary_key=True, max_length=20, serialize=False)),
                ('password', models.CharField(max_length=15)),
                ('phone', models.CharField(max_length=11)),
                ('image', models.FileField(upload_to='images')),
            ],
            options={
                'db_table': 'work_userinfo',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('username', models.CharField(max_length=20)),
                ('headimg', models.FileField(upload_to='file')),
                ('classfi', models.CharField(max_length=10)),
                ('uptime', models.DateTimeField(verbose_name='上传日期')),
            ],
            options={
                'db_table': 'work_users',
            },
        ),
    ]
