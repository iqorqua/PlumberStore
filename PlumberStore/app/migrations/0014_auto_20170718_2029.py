# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20170718_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewmodel',
            name='reviewer_date',
            field=models.DateTimeField(),
        ),
    ]
