# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-20 00:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170519_2036'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Korisnik',
        ),
        migrations.AddField(
            model_name='ugovorled',
            name='adresa',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='ugovorled',
            name='adresa_rac',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='ugovorled',
            name='adresa_true',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='ugovorled',
            name='ime',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='ugovorled',
            name='mail',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='ugovorled',
            name='mbg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ugovorled',
            name='mjesto',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='ugovorled',
            name='mob',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='ugovorled',
            name='oi',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ugovorled',
            name='oib',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ugovorled',
            name='prezime',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='ugovorled',
            name='pt_broj',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ugovorled',
            name='tel',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='ugovorstruja',
            name='adresa',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='ugovorstruja',
            name='adresa_rac',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='ugovorstruja',
            name='adresa_true',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='ugovorstruja',
            name='datum',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ugovorstruja',
            name='datum_epoch',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ugovorstruja',
            name='id_agent',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ugovorstruja',
            name='id_tvrtka',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ugovorstruja',
            name='ime',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='ugovorstruja',
            name='mail',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='ugovorstruja',
            name='mbg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ugovorstruja',
            name='mjesto',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='ugovorstruja',
            name='mob',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='ugovorstruja',
            name='oi',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ugovorstruja',
            name='oib',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ugovorstruja',
            name='prezime',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='ugovorstruja',
            name='pt_broj',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ugovorstruja',
            name='tel',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='ugovorled',
            name='datum',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ugovorled',
            name='datum_epoch',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ugovorled',
            name='nacin_placanja',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ugovorled',
            name='vrsta_racuna',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ugovorstruja',
            name='omm_adresa',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='ugovorstruja',
            name='omm_broj',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ugovorstruja',
            name='omm_mjesto',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='ugovorstruja',
            name='omm_pt_broj',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ugovorstruja',
            name='omm_tarifni_model',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ugovorstruja',
            name='omm_true',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='ugovorstruja',
            name='proizvod',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
