# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20170718_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewmodel',
            name='reviewer_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='reviewmodel',
            name='validated',
            field=models.BooleanField(default=False),
        ),
    ]
