from __future__ import unicode_literals

import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible
# from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)

    def __str__(self):
        return self.username


class UgovorStruja(models.Model):

    ime = models.CharField(max_length=120, blank=True, null=True)
    prezime = models.CharField(max_length=120, blank=True, null=True)
    oib = models.CharField(max_length=120, blank=True, null=True)
    mbg = models.CharField(max_length=120, blank=True, null=True)
    oi = models.CharField(max_length=120, blank=True, null=True)
    adresa_true = models.BooleanField(default=True)

    tel = models.CharField(max_length=120, blank=True, null=True)
    mob = models.CharField(max_length=120, blank=True, null=True)
    mail = models.CharField(max_length=120, blank=True, null=True)

    adresa = models.CharField(max_length=120, blank=True, null=True)
    adresa_rac = models.CharField(max_length=120, blank=True, null=True)

    mjesto = models.CharField(max_length=120, blank=True, null=True)
    pt_broj = models.CharField(max_length=120, blank=True, null=True)


    # 0 - IDEAL
    # 2 - BONUS
    # 1 - KLASIK
    proizvod = models.IntegerField(null=True, blank=True)

    # IF TRUE
    # Adresa za dostavu racuna ide na drugo mjesto

    omm_broj = models.CharField(max_length=120, blank=True, null=True)
    omm_tarifni_model = models.IntegerField(blank=True, null=True)

    omm_mjesto = models.CharField(max_length=120, blank=True, null=True)
    omm_adresa = models.CharField(max_length=120, blank=True, null=True)
    omm_pt_broj = models.CharField(max_length=120, blank=True, null=True)

    omm_true = models.BooleanField(default=True)

    omm_vt = models.IntegerField(blank=True, null=True)
    omm_nt = models.IntegerField(blank=True, null=True)
    omm_jt = models.IntegerField(blank=True, null=True)

    omm_datum_ocitanja = models.CharField(max_length=120, blank=True, null=True)
    omm_preporucitelj = models.CharField(max_length=120, blank=True, null=True)
    omm_preporucitelj_oib = models.CharField(max_length=120, blank=True, null=True)

    datum = models.CharField(max_length=120, null=True, blank=True)
    datum_epoch = models.CharField(max_length=120, null=True, blank=True)

    id_agent = models.IntegerField(null=True, blank=True)
    id_tvrtka = models.CharField(max_length=120, null=True, blank=True)


class UgovorLed(models.Model):
    ime = models.CharField(max_length=120, blank=True, null=True)
    prezime = models.CharField(max_length=120, blank=True, null=True)
    oib = models.IntegerField(blank=True, null=True)
    mbg = models.IntegerField(blank=True, null=True)
    oi = models.IntegerField(blank=True, null=True)
    adresa_true = models.BooleanField(default=True)

    tel = models.CharField(max_length=120, blank=True, null=True)
    mob = models.CharField(max_length=120, blank=True, null=True)
    mail = models.CharField(max_length=120, blank=True, null=True)

    adresa = models.CharField(max_length=120, blank=True, null=True)
    adresa_rac = models.CharField(max_length=120, blank=True, null=True)

    mjesto = models.CharField(max_length=120, blank=True, null=True)
    pt_broj = models.IntegerField(blank=True, null=True)

    # 1 - jednokratno placanje - JEDNOKRATNO
    # 2 - Na 36 mjesecnih rata uz ugovornu obvezu 36 mjeseci - RATE
    # 3 - Placanjem iznosa mjesecne najamnine sukladno Cjeniku tijekom trajanja najma - NAJAM
    nacin_placanja = models.IntegerField(null=True, blank=True)

    # 1 - Zasebni racun
    # 2- Jedinstveni racun za Usluge i isporucenu elektricnu energiju
    vrsta_racuna = models.IntegerField(null=True, blank=True)

    kolicina = models.IntegerField(null=True, blank=True)

    datum = models.DateField(null=True, blank=True)
    datum_epoch = models.IntegerField(null=True, blank=True)

    id_agent = models.IntegerField()
    id_tvrtka = models.IntegerField()

