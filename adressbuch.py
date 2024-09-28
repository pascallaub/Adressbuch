import re
import json
import os

eintraege = 'Kontakte.json'

def kontakte_laden():
    if os.path.exists(eintraege):
        with open(eintraege, 'r') as file:
                return json.load(file)
    return []

def kontakte_speichern(kontakte):
    with open(eintraege, 'w') as file:
        json.dump(kontakte, file, indent=4)

def showall():
    kontakte = kontakte_laden()
    if kontakte:
        for idx, eintrag in enumerate(kontakte, start=1):
            print(f"{idx}. Name: {eintrag['name']}, Telefonnummer: {eintrag['telefonnummer']}")
    else:
        print("Keine Kontakte vorhanden")

def suche():
    suche = input("Gib den Namen oder die Telefonnummer zum Suchen ein: ")
    
    kontakte = kontakte_laden()
    gefundene_kontakte = [
        kontakt for kontakt in kontakte
        if suche.lower() in kontakt['name'].lower() or suche in kontakt['telefonnummer']
    ]

    if gefundene_kontakte:
        for idx, kontakt in enumerate(gefundene_kontakte, start=1):
            print(f"{idx}. Name: {kontakt['name']}, Telefonnummer: {kontakt['telefonnummer']}")
    else:
        print("Keine Kontakte gefunden!")
    
        
def eintrag():
    name = input("Name: ")
    number = input("Telefonnummer: ")
    neuer_eintrag = {'name': name, 'telefonnummer': number}
    kontakte = kontakte_laden()
    kontakte.append(neuer_eintrag)
    kontakte_speichern(kontakte)
    print("Eintrag erfolgreich!")

def change():
    suche = input("Gib den Namen oder die Telefonnummer zum Ändern ein: ")

    kontakte = kontakte_laden()
    gefundene_kontakte = [
        kontakt for kontakt in kontakte
        if suche.lower() in kontakt['name'].lower() or suche in kontakt['telefonnummer']
    ]

    if gefundene_kontakte:
        for idx, kontakt in enumerate(gefundene_kontakte, start=1):
            print(f"{idx}: Name: {kontakt['name']}, Telefonnummer: {kontakt['telefonnummer']}")
        auswahl = int(input(f"Wähle einen Kontakt (1-{len(gefundene_kontakte)}): "))
        ausgewählter_kontakt = gefundene_kontakte[auswahl - 1]

        next = input("Willst du den Namen oder die Telefonnummer ändern? N/T: ").lower()
        if next == 'n':
            name_neu = input("Gib den neuen Namen ein: ")
            for kontakt in kontakte:
                if kontakt == ausgewählter_kontakt:
                    kontakt['name'] = name_neu
                    break
            kontakte_speichern(kontakte)
            print(f"Name geändert zu: {name_neu}")
        elif next == 't':
            nummer_neu = input("Gib die neue Telefonnummer ein: ")
            for kontakt in kontakte:
                if kontakt == kontakte:
                    kontakt['telefonnummer'] = nummer_neu
                    break
            kontakte_speichern(kontakte)
            print(f"Telefonnummer geändert zu: {nummer_neu}")
        else:
            print("Falsche Eingabe!")


def adressbuch():
    while True:
        print("Welche Aktion möchtest du durchführen?\n 1. Neuen Eintrag erstellen\n 2. Kontakte durchsuchen\n 3. Alle Kontakte anzeigen\n 4. Eintrag ändern\n 5. Eintrag löschen\n 6. Einträge alphabetisch anzeigen\n 7. Beenden")
        auswahl = input("1, 2, 3, 4, 5, 6 oder 7: ")
        try:
            if auswahl == '1':
                eintrag()
                continue
            elif auswahl == '2':
                suche()
                continue                
            elif auswahl == '3':
                showall()
                continue
            elif auswahl == '4':
                change()
                continue
            elif auswahl == '5':
                pass
            elif auswahl == '6':
                pass
            elif auswahl == '7':
                break
        except ValueError:
            print("Falsche Eingabe!")
            continue
                


adressbuch()