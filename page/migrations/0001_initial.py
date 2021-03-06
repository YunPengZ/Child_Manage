# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 01:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('cla_id', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('cla_name', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('par_id', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('par_nickname', models.CharField(max_length=16)),
                ('par_password', models.CharField(max_length=16)),
                ('par_name', models.CharField(default='Parent0', max_length=4)),
                ('par_sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2)),
                ('par_tel', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stu_id', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('stu_name', models.CharField(max_length=32)),
                ('stu_sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2)),
                ('stu_age', models.IntegerField()),
                ('stu_addr', models.TextField(default='NONE')),
                ('stu_perfer', models.TextField(default='NONE')),
                ('stu_cla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.ClassRoom')),
                ('stu_parent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.Parent')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('tea_id', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('tea_nickname', models.CharField(max_length=16)),
                ('tea_pas', models.CharField(max_length=16)),
                ('tea_name', models.CharField(default='AHU0', max_length=32)),
                ('tea_sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2)),
                ('tea_age', models.IntegerField()),
                ('tea_tel', models.IntegerField()),
                ('tea_intro', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='classroom',
            name='cla_tea',
            field=models.ManyToManyField(related_name='cla_tea', to='page.Teacher'),
        ),
    ]
