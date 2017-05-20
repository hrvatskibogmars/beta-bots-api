import csv
import datetime, time
from models import UgovorStruja


def import_data():
    all_prezime = set()
    with open('data/baza.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            if row["PROIZVOD"] == "IDEAL":
                proizvod = 0
            elif row["PROIZVOD"] == "KLASIK":
                proizvod = 1
            elif row["PROIZVOD"] == "BONUS":
                proizvod = 2

            if not row["Adr_rac"]:
                adresa_dostava_flag = False
            else:
                adresa_dostava_flag = True

            if not row["OMM_adresa"]:
                omm_adresa = False
            else:
                omm_adresa = True
            m, d, g = row["Dana"].split('/')
            t = datetime.datetime(int(g), int(m), int(d), 0, 0)
            datum = str(time.mktime(t.timetuple()))

            if row["TM"] == "BIJELI":
                tarifa = 1
            elif row["TM"] == "CRVENI":
                tarifa = 2
            elif row["TM"] == "PLAVI":
                tarifa = 0

            UgovorStruja(
                ime=row['Ime'],
                prezime=row['Prezime'],
                oib=row["OIB"],
                mbg=row["MBG"],
                oi=row["OI"],

                adresa=row["Adresa"],
                mjesto=row["Mjesto"],
                pt_broj=row["Pbroj"],
                adresa_rac=row["Adr_rac"],

                tel=row["Tel"],
                mob=row["Mob"],
                mail=row["Mail"],
                adresa_true=adresa_dostava_flag,

                proizvod=proizvod,

                omm_broj=row["OMM"],
                omm_tarifni_model=tarifa,
                omm_adresa=row["OMM_adresa"],
                omm_pt_broj=row["OMM_Pbroj"],
                omm_mjesto=row["OMM_mjesto"],
                omm_true=omm_adresa,
                omm_vt=None,
                omm_nt=None,
                omm_jt=None,
                omm_datum_ocitanja=None,
                omm_preporucitelj=None,
                omm_preporucitelj_oib=None,

                datum=row["Dana"],
                datum_epoch=datum,

                id_agent=row["Agent"],
                id_tvrtka="",
            ).save()
    print len(all_prezime)
