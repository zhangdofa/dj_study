# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortageInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('storeid', models.CharField(max_length=20)),
                ('storename', models.CharField(max_length=100)),
                ('shortquantity', models.IntegerField(default=0)),
                ('rundate', models.DecimalField(max_digits=20, decimal_places=20)),
            ],
            options={
                'db_table': 'shortage',
            },
        ),
    ]
