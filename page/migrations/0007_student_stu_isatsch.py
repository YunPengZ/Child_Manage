# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='stu_isAtSch',
            field=models.BooleanField(default=False),
        ),
    ]