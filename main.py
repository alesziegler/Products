
from collections import namedtuple
class NamedTuple:
    pass

class Produkt(NamedTuple):
    """
    ok, this class is clearly a child class of another class called
    NamedTuple. It is not sufficient to import named tuple package, we probably
    need to define that class.
    Also, what is supposed to be the tuple? Whole 'produkty'? Probably yes.
    Every Produkt clearly function as something like a dictionary.
    Dictionary is similar to named tuple, so Produkt is probably to be that.


    """
    def __init__(self,nazev,
                 kategorie,cena,mnozstvi
                 ):
        #self.nazev = nazev
        #self.kategorie = kategorie
        #self.cena = cena
        #self.mnozstvi = mnozstvi
        self.name = 'whatever'
        self.produkt = namedtuple(self.name,['kategorie','cena','mnozstvi'
                                              ])
        # ok, it wants to use strings and integer as something like index names?
        # so we maybe know how to create indexes, now, how to add values?
        # maybe that is what two classes are for? Use super?
        # it appears that name, here equivalent to "self.nazev", is used for a declaration?
        # ok, now it sort of works, at least on first glance, except that
        # we probably do need to ensure that nazev corresponds with name.
        # so, translate to US format, and then use replace to replace bad characters?

# Seznam produktů
produkty = [
    Produkt(nazev="Notebook", kategorie="Elektronika", cena=15000.0, mnozstvi=5),
    Produkt(nazev="Mobilní telefon", kategorie="Elektronika", cena=8000.0, mnozstvi=10),
    Produkt(nazev="Kniha", kategorie="Knihy", cena=300.0, mnozstvi=10),
    Produkt(nazev="Tablet", kategorie="Elektronika", cena=8000.0, mnozstvi=0)
]

