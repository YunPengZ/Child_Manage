# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0007_student_stu_isatsch'),
    ]

    operations = [
        migrations.CreateModel(
            name='deliverRecord',
            fields=[
                ('deliver_id', models.AutoField(max_length=5, primary_key=True, serialize=False)),
                ('deliver_state', models.BooleanField(default=False)),
                ('deliver_par', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deliver_par_set', to='page.Parent')),
                ('deliver_stu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stu_deliver_set', to='page.Student')),
            ],
        ),
    ]
