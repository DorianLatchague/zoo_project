# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-19 22:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoo_app', '0002_auto_20181119_2225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zoo',
            old_name='current_weather',
            new_name='weather',
        ),
    ]
