# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_blog_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, default=None, editable=False, null=True, unique=True),
        ),
    ]
