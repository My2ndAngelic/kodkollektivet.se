# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kodkollektivet', '0002_auto_20170224_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='in_focus',
            field=models.BooleanField(default=False),
        ),
    ]