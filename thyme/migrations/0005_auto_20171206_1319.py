# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 13:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thyme', '0004_auto_20171130_1016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snapshot',
            options={'ordering': ['-timestamp']},
        ),
    ]