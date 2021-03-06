# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=30)),
                ('director', models.CharField(max_length=200)),
                ('imdbrating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('poster', models.CharField(max_length=2000)),
            ],
        ),
    ]
