# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-20 00:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20170520_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ugovorstruja',
            name='datum',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
