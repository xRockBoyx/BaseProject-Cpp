# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-04 02:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omniscient', '0003_auto_20181120_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='Photo',
            field=models.ImageField(upload_to='./'),
        ),
    ]
