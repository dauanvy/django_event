# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-10 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_auto_20180210_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
