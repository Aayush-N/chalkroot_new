# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-12 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20180912_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='overall_rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
