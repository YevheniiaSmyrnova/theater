# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actor', '0002_auto_20171111_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('duration', models.TimeField()),
                ('sort_description', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=50)),
                ('producer', models.ManyToManyField(to='actor.Actor')),
            ],
        ),
    ]
