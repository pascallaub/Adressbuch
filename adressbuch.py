import re

eintraege = open('Kontakte.txt', 'w')

def showall():
    with open('Kontakte.txt', 'r') as file:
        print(eintraege.read())

#def suche():
#    suche = input("Gib den Namen oder die Telefonnummer zum Suchen ein: ")
#    such_ergebenis = any(item in eintraege for item in eintraege)
#    print(such_ergebenis)
    
        
def eintrag():
    name = input("Name: ")
    number = input("Telefonnummer: ")
    neuer_eintrag = (f"'Name': {name}, 'Telefonnummer': {number}")
    eintraege.write(f"{neuer_eintrag}")

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