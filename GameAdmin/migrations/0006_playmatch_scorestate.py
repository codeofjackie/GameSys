# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-04 06:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameAdmin', '0005_match_matchtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='playmatch',
            name='ScoreState',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
