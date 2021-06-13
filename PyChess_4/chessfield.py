"""
Ovde će biti definisan dizajn polja na tabli.
U poljima će se čuvati i figura koja je trenutno na polju.
Posedovaće metode za iscrtavanje polja u kojima će se nalaziti figure,
kao i samih figura, kao i za bojenje ćelija za potencijalne poteze.
"""


import pygame


BOJA_OZNACAVANJA = (160, 200, 255)  # Boja za obeležavanje polja koje je validan potez
BOJA_SPECIJALNOG_POTEZA = (170, 220, 170)  # Boja za obeležavanje polja za rokadu, enpassant ili promociju
BELA = (255, 255, 255)
SIRINA_TABLE = 513  # Širina i visina cele table u pikselima
KOLONE = 8  # Broj kolona i redova na tabli
SIRINA_POLJA = SIRINA_TABLE // KOLONE  # Širina jednog polja na tabli u pikselima


class Polje:
    """
    Opšti opis polja na kojima stoje figure.
    Sadrži svoje koordinate na sahovnici, veličinu polja, koordinate u prozoru,
    trenutnu boju kao i da li postoji figura na polju ili ne.
    """
    def __init__(self, red, kolona, figura, sirina=SIRINA_POLJA, boja=BELA):
        """
        :param red: int: 0-7
        :param kolona: int: 0-7
        :param figura: Figura: Opis pojedinačne šahovske figure koja se nalazi na trenutnom polju, ili None ako
                                nema ni jedne figure na polju
        :param sirina: int: sirina i visina jednog polja u pikselima, podrazumevana vrednost je globalna sirina polja
        :param boja: str: boja polja, podrazumevana vrednost je bela
        """
        self.red = red
        self.kolona = kolona
        self.figura = figura
        self.sirina = sirina
        self.x = red * sirina
        self.y = kolona * sirina
        self.boja = boja
        self.obelezeno = False  # Opisuje da li je polje obelezeno kao validan potencijalni potez
        self.specijalni_potez = False  # Opisuje da li je polje obelezeno za rokadu, enpassant ili promociju
        self.rect = (self.x, self.y, self.sirina, self.sirina)  # Pomocna promenljiva za grafičko iscrtavanje polja

    def crtaj(self, win):
        """
        Metoda za iscrtavanje polja. Boji polja svojom bojom ako nisu obelezena, a ako jesu boji ih u plavo.
        :param win: win: Prozor u kojem ce se crtati polje.
        :return: None
        """
        if self.specijalni_potez:
            pygame.draw.rect(win, BOJA_SPECIJALNOG_POTEZA, self.rect)
        elif self.obelezeno:
            pygame.draw.rect(win, BOJA_OZNACAVANJA, self.rect)
        else:
            pygame.draw.rect(win, self.boja, self.rect)

    def postavi(self, win):
        """
        Metoda za iscrtavanje figure koja je na polju.
        :param win: win: Prozor u kojem ce se crtati polje.
        :return: None
        """
        if self.figura:
            win.blit(self.figura.slika, (self.x, self.y))
