from typing import NamedTuple, List

from typing import List, NamedTuple

class Produkt(NamedTuple):
    nazev: str
    kategorie: str
    cena: float
    mnozstvi: int

# Seznam produktů
produkty = [
    Produkt(nazev="Notebook", kategorie="Elektronika", cena=15000.0, mnozstvi=5),
    Produkt(nazev="Mobilní telefon", kategorie="Elektronika", cena=8000.0, mnozstvi=10),
    Produkt(nazev="Kniha", kategorie="Knihy", cena=300.0, mnozstvi=10),
    Produkt(nazev="Tablet", kategorie="Elektronika", cena=8000.0, mnozstvi=0)
]

def dostupne_produkty(produkty: List[Produkt], kategorie: str) -> List[str]:
    return [produkt.nazev for produkt in produkty if produkt.kategorie == kategorie and produkt.mnozstvi > 0]

print("Katalog:")
for produkt in produkty:
    print(f"{produkt.nazev}, {produkt.kategorie}, cena {produkt.cena}, množství {produkt.mnozstvi}")

dostupne = dostupne_produkty(produkty, "Elektronika")
print("Dostupné produkty jsou:", ', '.join(dostupne))
