# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0010_auto_20160402_0309'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date_unpublished',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
    ]
