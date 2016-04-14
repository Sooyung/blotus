# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-24 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stalk', '0007_auto_20160309_0802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invest_id', models.CharField(max_length=50, unique=True)),
                ('bid_id', models.CharField(max_length=20, null=True)),
                ('plat_id', models.CharField(max_length=20)),
                ('plat_name', models.CharField(max_length=50, null=True)),
                ('user_id', models.CharField(max_length=20, null=True)),
                ('username', models.CharField(max_length=20, null=True)),
                ('amount', models.CharField(max_length=20, null=True)),
                ('valid_amount', models.CharField(max_length=20, null=True)),
                ('add_date', models.CharField(max_length=20, null=True)),
                ('status', models.CharField(max_length=20, null=True)),
                ('type', models.CharField(max_length=20, null=True)),
                ('url', models.TextField(null=True)),
            ],
            options={
                'db_table': 'enterprise_invest',
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_id', models.CharField(max_length=20, unique=True)),
                ('plat_id', models.CharField(max_length=20)),
                ('plat_name', models.CharField(max_length=50, null=True)),
                ('title', models.CharField(max_length=50, null=True)),
                ('amount', models.CharField(max_length=20, null=True)),
                ('process', models.CharField(max_length=20, null=True)),
                ('interest_rate', models.CharField(max_length=20, null=True)),
                ('borrow_period', models.CharField(max_length=20, null=True)),
                ('borrow_unit', models.CharField(max_length=20, null=True)),
                ('reward', models.CharField(max_length=20, null=True)),
                ('type', models.CharField(max_length=20, null=True)),
                ('repay_type', models.CharField(max_length=20, null=True)),
                ('username', models.CharField(max_length=20, null=True)),
                ('user_id', models.CharField(max_length=20, null=True)),
                ('user_avatar_url', models.TextField(null=True)),
                ('province', models.CharField(max_length=20, null=True)),
                ('city', models.CharField(max_length=20, null=True)),
                ('borrow_detail', models.TextField(null=True)),
                ('url', models.TextField(null=True)),
                ('success_time', models.CharField(max_length=20, null=True)),
                ('publish_time', models.CharField(max_length=20, null=True)),
                ('invest_count', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'enterprise_loan',
            },
        ),
        migrations.CreateModel(
            name='Overdue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plat_id', models.CharField(max_length=20)),
                ('plat_name', models.CharField(max_length=50, null=True)),
                ('user_id', models.CharField(max_length=20, null=True)),
                ('username', models.CharField(max_length=20, null=True)),
                ('idcard', models.CharField(max_length=20, null=True)),
                ('overdue_count', models.CharField(max_length=20, null=True)),
                ('overdue_total', models.CharField(max_length=20, null=True)),
                ('overdue_principal', models.CharField(max_length=20, null=True)),
                ('payment_total', models.CharField(max_length=20, null=True)),
                ('payment_count', models.CharField(max_length=20, null=True)),
                ('payment_period', models.CharField(max_length=20, null=True)),
                ('repay_amount', models.CharField(max_length=20, null=True)),
                ('wait_amount', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'enterprise_overdue',
            },
        ),
        migrations.AlterUniqueTogether(
            name='overdue',
            unique_together=set([('plat_id', 'user_id')]),
        ),
    ]
