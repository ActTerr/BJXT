# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-21 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='unit',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
