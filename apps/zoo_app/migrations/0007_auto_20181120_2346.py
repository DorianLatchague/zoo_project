# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-21 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo_app', '0006_auto_20181120_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(choices=[('animal_escape', 'animal escape'), ('sick_animals', 'sick animals'), ('fieldtrip', 'local school fieldtrip'), ('donation', 'anonymous donation'), ('birth', 'animal birth'), ('fish_sale', 'fish are on sale'), ('animal_attack', 'animal attack')], max_length=255),
        ),
    ]