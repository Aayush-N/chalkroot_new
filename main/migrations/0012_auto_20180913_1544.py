# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-13 15:44
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20180913_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='photos',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
