# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-20 00:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20170520_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ugovorstruja',
            name='id_tvrtka',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
