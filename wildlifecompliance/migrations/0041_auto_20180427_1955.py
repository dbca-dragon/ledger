# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-27 11:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0040_application_licence_type_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='licence_activity',
        ),
        migrations.RemoveField(
            model_name='application',
            name='licence_activity_type',
        ),
    ]