# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-07 19:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(max_length=100, verbose_name='Unique identifier')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified on')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(max_length=100, verbose_name='Unique identifier')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified on')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['name'],
            },
        ),
    ]
