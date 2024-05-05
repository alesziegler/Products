

class NamedTuple:
    from collections import namedtuple

class Produkt(NamedTuple):
    """
    ok, this class is clearly a child class of another class called
    NamedTuple. It is not sufficient to import named tuple package, we probably
    need to define that class.
    Also, what is supposed to be the tuple? Whole 'produkty'?

    """
    def __init__(self,nazev,kategorie,cena,mnozstvi):
        pass
        #self.produkt = produkt
        #self.produkt.namedtuple(produkt,['nazev','kategorie','cena','mnozstvi'])

# Seznam produktů
produkty = [
    Produkt(nazev="Notebook", kategorie="Elektronika", cena=15000.0, mnozstvi=5),
    Produkt(nazev="Mobilní telefon", kategorie="Elektronika", cena=8000.0, mnozstvi=10),
    Produkt(nazev="Kniha", kategorie="Knihy", cena=300.0, mnozstvi=10),
    Produkt(nazev="Tablet", kategorie="Elektronika", cena=8000.0, mnozstvi=0)
]

