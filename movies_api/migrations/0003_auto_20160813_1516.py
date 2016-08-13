# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_api', '0002_movie_plot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdbrating',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterUniqueTogether(
            name='movie',
            unique_together=set([('title', 'year')]),
        ),
    ]
