# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-19 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_profile', '0002_auto_20180418_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='password2',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
