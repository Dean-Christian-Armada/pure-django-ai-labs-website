# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 07:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0015_remove_blog_photo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPhotos',
            new_name='BlogPhoto',
        ),
    ]
