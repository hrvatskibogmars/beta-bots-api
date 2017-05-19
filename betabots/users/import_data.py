import csv
from models import Korisnik


def import_data():
    all_prezime = set()
    with open('data/baza.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            obj, created = Korisnik.objects.get_or_create(
                ime=row['Ime'],
                prezime=row['Prezime'],
                defaults={
                    'oib': row["OIB"],
                    'mbg': row["MBG"],
                    'oib': row["OI"],
                    'oib': row["Adresa"],
                    'oib': row["Mjesto"],
                    'oib': row["Pbroj"],
                    'oib': row["Adr_rac"],
                    'oib': row["Tel"],
                    'oib': row["Mob"],
                    'oib': row["Mail"],
                    'oib': row["OMM"],
                    'oib': row["OMM"],

                }

            )
    print len(all_prezime)
