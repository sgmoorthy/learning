# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-21 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
