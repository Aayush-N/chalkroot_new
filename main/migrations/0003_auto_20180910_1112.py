# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-10 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180906_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='id',
        ),
        migrations.AddField(
            model_name='school',
            name='sid',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
