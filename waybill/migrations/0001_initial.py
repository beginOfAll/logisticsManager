# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-24 09:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_name', models.CharField(max_length=30)),
                ('company', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('store', models.CharField(max_length=50)),
                ('client_channel', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Waybill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waybill_number', models.CharField(max_length=50)),
                ('create_time', models.DateTimeField()),
                ('order_number', models.CharField(max_length=50)),
                ('store', models.CharField(max_length=50)),
                ('client_channel', models.CharField(max_length=50)),
                ('from_person_name', models.CharField(default='', max_length=100)),
                ('from_company', models.CharField(default='', max_length=100)),
                ('from_phone_num', models.CharField(default='', max_length=100)),
                ('from_country', models.CharField(default='', max_length=50)),
                ('from_province', models.CharField(default='', max_length=50)),
                ('from_city', models.CharField(default='', max_length=50)),
                ('from_street', models.CharField(default='', max_length=100)),
                ('to_person_name', models.CharField(max_length=100)),
                ('to_company', models.CharField(max_length=100)),
                ('to_phone_num', models.CharField(max_length=100)),
                ('to_country', models.CharField(max_length=50)),
                ('to_province', models.CharField(max_length=50)),
                ('to_city', models.CharField(max_length=50)),
                ('to_street', models.CharField(max_length=100)),
                ('goods_detail', models.CharField(max_length=100)),
                ('goods_numbers', models.IntegerField()),
                ('currency', models.CharField(choices=[('CNY', '人民币'), ('USD', '美元'), ('GBP', '英镑'), ('JPY', '日元'), ('AUD', '澳元'), ('EUR', '欧元')], max_length=10)),
                ('single_price', models.FloatField()),
                ('total_price', models.FloatField()),
                ('package_numbers', models.IntegerField()),
                ('weight', models.FloatField()),
                ('remark', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]