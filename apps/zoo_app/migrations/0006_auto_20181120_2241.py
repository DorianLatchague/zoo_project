# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-21 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo_app', '0005_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='habitat',
        ),
        migrations.AddField(
            model_name='animal',
            name='habitat',
            field=models.ManyToManyField(related_name='inhabitants', to='zoo_app.Habitat'),
        ),
    ]