# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-05 07:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20180205_0731'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventGroupUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_group_user_id', to='event.EventGroups')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_group_user_id', to='event.EventUsers')),
            ],
            options={
                'db_table': 'eventgroupuser',
            },
        ),
        migrations.AddField(
            model_name='eventgroups',
            name='user',
            field=models.ManyToManyField(related_name='user_ids', through='event.EventGroupUser', to='event.EventUsers'),
        ),
    ]
