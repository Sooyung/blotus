# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-27 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stalk', '0003_feature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exposure',
            name='thread',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='thread',
            field=models.IntegerField(),
        ),
    ]
