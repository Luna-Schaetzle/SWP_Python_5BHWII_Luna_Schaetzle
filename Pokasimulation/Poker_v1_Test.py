import random 
import numpy as np

# Wir haben 52 Karten im Deck und 4 Farben (Kreuz, Pik, Herz, Karo) je 13 Karten Typen (2,3,4,5,6,7,8,9,10,B,D,K,A)
# Wir könnten eine Klasse Programmieren das wäre aber zu viel für den Anfang
# Deshalb machen wir es einfach und verwenden eine Liste
# Um dann einfach herauszufinden welche Karte gezogen wurde definieren wir 2 Regeln
# 1. Wenn wir die gezogene Zahl durch 4 teilen mittels floor division (//) erhalten wir die Farbe 
#       0 -> Kreuz
#       1 -> Pik
#       2 -> Herz
#       3 -> Karo
# 2. Wenn wir die gezogene Zahl modulo 13 rechnen erhalten wir den Karten Typ
#       0 -> 2
#       1 -> 3
#       2 -> 4
#       3 -> 5
#       4 -> 6
#       5 -> 7
#       6 -> 8
#       7 -> 9
#       8 -> 10
#       9 -> Bube
#       10 -> Dame
#       11 -> König
#       12 -> Ass

# Testen wir die Regeln:

# Definiere Farben und Kartentypen
farben = ['Kreuz', 'Pik', 'Herz', 'Karo']
karten_typen = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']

# Erstelle ein Deck mit allen Karten
deck = [(farbe, kartentyp) for farbe in farben for kartentyp in karten_typen]

# Funktion, um eine Karte zu ziehen und aus dem Deck zu entfernen
def ziehe_karte(deck):
    if len(deck) == 0:
        raise ValueError("Keine Karten mehr im Deck!")
    
    # Ziehe eine zufällige Karte aus dem Deck
    gezogene_karte = random.choice(deck)
    deck.remove(gezogene_karte)  # Entferne die gezogene Karte aus dem Deck
    
    return gezogene_karte

# Funktion, um alle Karten zu ziehen
def ziehe_alle_karten():
    # Erstelle eine Kopie des Decks, um das Originaldeck nicht zu verändern
    deck_kopie = deck.copy()
    gezogene_karten = []
    
    while len(deck_kopie) > 0:
        gezogene_karten.append(ziehe_karte(deck_kopie))
    
    return gezogene_karten

# Testfunktion, um sicherzustellen, dass alle Karten genau einmal gezogen werden
def test_alle_karten_ziehen():
    gezogene_karten = ziehe_alle_karten()
    
    # Test: Es sollten genau 52 Karten gezogen worden sein
    assert len(gezogene_karten) == 52, f"Es wurden {len(gezogene_karten)} Karten gezogen, erwartet: 52"
    
    # Test: Jede Karte sollte nur einmal gezogen worden sein
    assert len(set(gezogene_karten)) == 52, "Es wurden doppelte Karten gezogen!"
    
    print("Test bestanden: Alle Karten wurden genau einmal gezogen.")
    return gezogene_karten

# Hauptfunktion zum Ausführen des Tests
if __name__ == "__main__":
    # Testweise alle Karten ziehen und ausgeben
    gezogene_karten = test_alle_karten_ziehen()
    
    # Zeige alle gezogenen Karten an
    for i, karte in enumerate(gezogene_karten, start=1):
        print(f"Karte {i}: {karte[0]} {karte[1]}")
    

