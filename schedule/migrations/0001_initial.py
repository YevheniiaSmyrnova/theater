# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 16:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('performance', '0002_auto_20171111_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('place', models.CharField(max_length=255)),
                ('ticket', models.URLField()),
                ('performance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performance.Performance')),
            ],
        ),
    ]
