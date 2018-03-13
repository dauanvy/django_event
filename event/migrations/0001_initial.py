# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-13 03:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'categorys',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=256)),
                ('title', models.TextField(blank=True, default='', null=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('organizer', models.CharField(default='', max_length=256)),
                ('phone', models.CharField(default='', max_length=256)),
                ('slug', models.SlugField(default='')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='event.Category')),
            ],
            options={
                'db_table': 'event',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='EventGroups',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=256)),
            ],
            options={
                'db_table': 'eventgroups',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='EventUsers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=256)),
                ('password', models.CharField(default='', max_length=256)),
                ('repassword', models.CharField(default='', max_length=256)),
                ('email', models.CharField(default='', max_length=256)),
                ('group', models.ManyToManyField(blank=True, default=False, related_name='group_ids', to='event.EventGroups')),
            ],
            options={
                'db_table': 'eventusers',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('street', models.CharField(default='', max_length=30)),
                ('city', models.CharField(default='', max_length=30)),
                ('country', models.CharField(default='', max_length=30)),
            ],
            options={
                'db_table': 'locations',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='event.Location'),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='event.EventUsers'),
        ),
    ]
