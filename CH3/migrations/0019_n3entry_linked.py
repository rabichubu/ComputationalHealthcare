# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-13 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CH3', '0018_n3group'),
    ]

    operations = [
        migrations.AddField(
            model_name='n3entry',
            name='linked',
            field=models.BooleanField(default=True),
        ),
    ]
