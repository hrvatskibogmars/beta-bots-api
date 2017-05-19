# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-19 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170516_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Korisnik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=120)),
                ('prezime', models.CharField(max_length=120)),
                ('oib', models.IntegerField()),
                ('mbg', models.IntegerField()),
                ('oi', models.IntegerField()),
                ('tel', models.CharField(max_length=120)),
                ('mob', models.CharField(max_length=120)),
                ('mail', models.CharField(max_length=120)),
                ('adresa', models.CharField(max_length=120)),
                ('mjesto', models.CharField(max_length=120)),
                ('pt_broj', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UgovorLed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nacin_placanja', models.IntegerField()),
                ('vrsta_racuna', models.IntegerField()),
                ('kolicina', models.IntegerField(blank=True, null=True)),
                ('datum', models.DateField()),
                ('datum_epoch', models.IntegerField()),
                ('id_agent', models.IntegerField()),
                ('id_tvrtka', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UgovorStruja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('omm_broj', models.IntegerField()),
                ('omm_tarifni_model', models.IntegerField()),
                ('omm_mjesto', models.CharField(max_length=120)),
                ('omm_adresa', models.CharField(max_length=120)),
                ('omm_pt_broj', models.IntegerField()),
                ('omm_true', models.BooleanField()),
                ('omm_vt', models.IntegerField(blank=True, null=True)),
                ('omm_nt', models.IntegerField(blank=True, null=True)),
                ('omm_jt', models.IntegerField(blank=True, null=True)),
                ('omm_datum_ocitanja', models.DateField(blank=True, null=True)),
                ('omm_preporucitelj', models.IntegerField(blank=True, null=True)),
                ('omm_preporucitelj_oib', models.IntegerField(blank=True, null=True)),
                ('proizvod', models.IntegerField()),
            ],
        ),
    ]