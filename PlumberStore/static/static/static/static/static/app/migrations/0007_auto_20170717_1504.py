# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20170717_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='image',
            field=models.ImageField(default='goods_pic_folder/no-img.jpg', upload_to='goods_pic_folder/'),
        ),
    ]
