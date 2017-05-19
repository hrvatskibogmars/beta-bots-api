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


class Korisnik(models.Model):
    ime = models.CharField(max_length=120)
    prezime = models.CharField(max_length=120)
    oib = models.IntegerField(blank=True, null=True)
    mbg = models.IntegerField(blank=True, null=True)
    oi = models.IntegerField(blank=True, null=True)

    tel = models.CharField(max_length=120, blank=True, null=True)
    mob = models.CharField(max_length=120, blank=True, null=True)
    mail = models.CharField(max_length=120, blank=True, null=True)

    adresa = models.CharField(max_length=120, blank=True, null=True)
    mjesto = models.CharField(max_length=120, blank=True, null=True)
    pt_broj = models.IntegerField(blank=True, null=True)


class UgovorStruja(models.Model):

    # IF TRUE
    # Adresa za dostavu racuna ide na drugo mjesto

    omm_broj = models.IntegerField()
    omm_tarifni_model = models.IntegerField()

    omm_mjesto = models.CharField(max_length=120)
    omm_adresa = models.CharField(max_length=120)
    omm_pt_broj = models.IntegerField()

    omm_true = models.BooleanField()

    omm_vt = models.IntegerField(blank=True, null=True)
    omm_nt = models.IntegerField(blank=True, null=True)
    omm_jt = models.IntegerField(blank=True, null=True)

    omm_datum_ocitanja = models.DateField(blank=True, null=True)
    omm_preporucitelj = models.IntegerField(blank=True, null=True)
    omm_preporucitelj_oib = models.IntegerField(blank=True, null=True)

    # 1 - IDEAL
    # 2 - BONUS
    # 3 - KLASIK
    proizvod = models.IntegerField()


class UgovorLed(models.Model):
    # 1 - jednokratno placanje - JEDNOKRATNO
    # 2 - Na 36 mjesecnih rata uz ugovornu obvezu 36 mjeseci - RATE
    # 3 - Placanjem iznosa mjesecne najamnine sukladno Cjeniku tijekom trajanja najma - NAJAM
    nacin_placanja = models.IntegerField()

    # 1 - Zasebni racun
    # 2- Jedinstveni racun za Usluge i isporucenu elektricnu energiju
    vrsta_racuna = models.IntegerField()

    kolicina = models.IntegerField(null=True, blank=True)

    datum = models.DateField()
    datum_epoch = models.IntegerField()

    id_agent = models.IntegerField()
    id_tvrtka = models.IntegerField()

# class Proizvod(models):
