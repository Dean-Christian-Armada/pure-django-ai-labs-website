# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 02:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20160402_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
