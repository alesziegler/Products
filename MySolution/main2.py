
from collections import namedtuple

class NamedTuple:
    pass

class Produkt(NamedTuple):
    pass
    ...
Produkt = namedtuple("Produkt",["nazev","kategorie", "cena","mnozstvi"])
# Seznam produktů
produkty = [
    Produkt(nazev="Notebook", kategorie="Elektronika", cena=15000.0, mnozstvi=5),
    Produkt(nazev="Mobilní telefon", kategorie="Elektronika", cena=8000.0, mnozstvi=10),
    Produkt(nazev="Kniha", kategorie="Knihy", cena=300.0, mnozstvi=10),
    Produkt(nazev="Tablet", kategorie="Elektronika", cena=8000.0, mnozstvi=0)
]

print("Katalog:")

for produkt in produkty:
    print(f"{produkt.nazev}, {produkt.kategorie}, cena {produkt.cena}, množství {produkt.mnozstvi}")

print("Dostupné produkty jsou:",end=" ")

result = []

count = 0

for produkt in produkty:
    if produkt.kategorie == "Elektronika" and produkt.mnozstvi > 0:
        result.append(produkt.nazev)

for x in result:
    if count < 1:
        x += ","
    print(x, end = " ")
    count += 1

