# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20170303_0848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='photo',
        ),
        migrations.AddField(
            model_name='photo',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
