# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-21 09:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thyme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snapshot',
            name='owner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
            preserve_default=False,
        ),
    ]
