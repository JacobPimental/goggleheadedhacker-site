# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-26 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180226_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
