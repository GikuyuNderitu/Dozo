# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 22:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_scorecard_challenge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scorecard',
            old_name='duration',
            new_name='act_duration',
        ),
        migrations.AddField(
            model_name='scorecard',
            name='est_duration',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
    ]
