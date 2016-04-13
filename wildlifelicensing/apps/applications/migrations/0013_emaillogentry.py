# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-12 08:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0012_auto_20160411_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailLogEntry',
            fields=[
                ('applicationlogentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='applications.ApplicationLogEntry')),
            ],
            options={
                'abstract': False,
            },
            bases=('applications.applicationlogentry',),
        ),
    ]
