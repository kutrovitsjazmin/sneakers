import csv


def fajl_beolvasasa(cipo_fajl_eleresi_utvonal):
    cipo_lista = []

    with open(cipo_fajl_eleresi_utvonal, newline='', encoding='utf-8') as csvfile:
        olvaso = csv.DictReader(csvfile)
        for sor in olvaso:
            cipo_adatok = {
                'cim': sor['title'],
                'szin_roviden': sor['color_breif'],
                'teljes_ar': float(sor['fullPrice']),
                'jelenlegi_ar': float(sor['currentPrice']),
                'kiadas_datuma': sor['publish_date']
            }
            cipo_lista.append(cipo_adatok)

    return cipo_lista


def rendez_es_megjelenit(cipo_lista, rendezes_kulcs):
    rendezett_cipok = sorted(cipo_lista, key=lambda x: x[rendezes_kulcs])

    for idx, cipo_adatok in enumerate(rendezett_cipok, start=1):
        print(f"Cipo #{idx}:")
        print(f"  Cim: {cipo_adatok['cim']}")
        print(f"  Szin : {cipo_adatok['szin_roviden']}")
        print(f"  Teljes ar: ${cipo_adatok['teljes_ar']}")
        print(f"  Jelenlegi ar: ${cipo_adatok['jelenlegi_ar']}")
        print(f"  Kiadas datuma: {cipo_adatok['kiadas_datuma']}")
        print("\n")


def main():
    cipo_fajl_eleresi_utvonal = 'sneakers.csv'
    cipo_lista = fajl_beolvasasa(cipo_fajl_eleresi_utvonal)

    felhasznalo_valasztas = int(
        input("Valassz rendezesi szempontot!! (1=cim, 2=szin, 3=teljes ar, 4=jelenlegi ar, 5=kiadas datuma): "))

    rendezes_kulcs_mapping = {
        1: 'cim',
        2: 'szin',
        3: 'teljes_ar',
        4: 'jelenlegi_ar',
        5: 'kiadas_datuma'
    }

    if felhasznalo_valasztas in rendezes_kulcs_mapping:
        rendezes_kulcs = rendezes_kulcs_mapping[felhasznalo_valasztas]
        rendez_es_megjelenit(cipo_lista, rendezes_kulcs)
    else:
        print("Ervenytelen valasztas.")


main()
