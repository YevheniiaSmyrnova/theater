# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0002_auto_20171111_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='description',
            field=models.TextField(),
        ),
    ]