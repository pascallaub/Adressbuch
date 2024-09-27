import re

eintraege = [""]

def showall():
    print(eintraege)

def suche():
    suche = input("Gib den Namen oder die Telefonnummer zum Suchen ein: ")
    suche_ergebnis = re.findall(r'\d+', suche)
    print(suche_ergebnis)

def eintrag():
    name = input("Name: ")
    number = input("Telefonnummer: ")
    combi = name + " " + number
    eintraege.append(combi)

def adressbuch():
    while True:
        print("Welche Aktion möchtest du durchführen?\n 1. Neuen Eintrag erstellen\n 2. Kontakte durchsuchen\n 3. Alle Kontakte anzeigen\n 4. Beenden")
        auswahl = input("1, 2, 3 oder 4: ")
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
                break
        except ValueError:
            print("Falsche Eingabe!")
            continue
                


adressbuch()