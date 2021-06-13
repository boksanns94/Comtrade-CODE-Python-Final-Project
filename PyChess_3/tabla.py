"""
Ovde će biti definisan dizajn table.
Ovde će se iscrtavati polja u kojima će se nalaziti figure, kao i slike samih figura.
Takođe će se ovde izvršavati bojenje ćelija za potencijalne poteze.
"""


import pygame
from figure import raspored_figura


BELA = (255, 255, 255)
SIVA = (120, 120, 120)
ZUTA = (200, 200, 0)
PLAVA = (160, 200, 255)
CRNA = (0, 0, 0)
KOLONE = 8  # Broj kolona i redova na tabli
SIRINA_TABLE = 512  # Širina i visina cele table u pikselima
SIRINA_POLJA = SIRINA_TABLE // KOLONE  # Širina jednog polja na tabli u pikselima


class Polje:
    """
    Opšti opis polja na kojima stoje figure.
    Sadrži svoje koordinate na polju, svoju veličinu na polju, trenutno boju kao i da li postoji figura na polju ili ne.
    """
    def __init__(self, red, kolona, sirina=SIRINA_POLJA, boja=BELA):
        """
        :param red: int: 0-7
        :param kolona: int: 0-7
        :param sirina: int: sirina i visina jednog polja u pikselima, podrazumevana vrednost je globalna sirina polja
        :param boja: str: boja polja, podrazumevana vrednost je bela
        """
        self.red = red
        self.kolona = kolona
        self.sirina = sirina
        self.x = int(red * sirina)
        self.y = int(kolona * sirina)
        self.boja = boja
        self.obelezeno = False  # Opisuje da li se nad poljem išta radi (kao npr osvetljavanje potencijalnog poteza)
        self.rect = (self.x, self.y, self.sirina, self.sirina)
        self.figura = raspored_figura[(self.red, self.kolona)]

    def crtaj(self, win):
        """
        Metoda za iscrtavanje polja. Boji polja svojom bojom ako nisu obelezena, a ako jesu boji ih u plavo.
        :param win: win: Prozor u kojem ce se crtati polje.
        :return: None
        """
        if self.obelezeno == False:
            pygame.draw.rect(win, self.boja, self.rect)
        else:
            pygame.draw.rect(win, PLAVA, self.rect)

    def postavi(self, win):
        """
        Metoda za iscrtavanje figure koja je na polju.
        :param win: win: Prozor u kojem ce se crtati polje.
        :return: None
        """
        if self.figura:
            win.blit(self.figura.slika, (self.x, self.y))


def napravi_tablu(tabla):
    """
    Funkcija za generisanje pocetnog stanja sahovske table. Postavljanje naizmenicnih sivih i belih polja.
    :param tabla: Dict: Rečnik sa klasama Polje koji sadrži stanja svih polja na tabli.
    :return: None
    """
    for i in range(KOLONE):
        for j in range(KOLONE):
            tabla[(i, j)] = Polje(i, j)
            if (i+j) % 2 == 1:
                tabla[(i, j)].boja = SIVA


def azuriraj_sliku(tabla, win, kolone=KOLONE):
    """
    Funkcija za azuriranje izgleda polja šahovske table ispod figura.
    :param tabla: Dict: Rečnik sa klasama Polje koji sadrži stanja svih polja na tabli.
    :param win: win: Prozor u kojem ce se azurirati polja.
    :param kolone: int: Broj kolona i redova u tabli.
    :return:
    """
    for i in range(kolone):
        for j in range(kolone):
            tabla[(i, j)].crtaj(win)
            tabla[(i, j)].postavi(win)
    pygame.display.update()


def nadji_polje(pozicija_misa):
    red = pozicija_misa[0] // SIRINA_POLJA
    kolona = pozicija_misa[1] // SIRINA_POLJA
    return red, kolona


def deselektuj_sve(sahovnica):
    for polje in sahovnica.keys():
        sahovnica[polje].obelezeno = False
