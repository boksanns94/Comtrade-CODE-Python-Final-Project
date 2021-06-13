"""
Ovde će biti definisane figure, njihovi tipovi, timovi i slike.
Biće inicijalizovani objekti za svaku figuru i učitana slika za svaku figuru.
"""


import pygame


class Figura:
    """
    Opšti opis figure. Sadrži tim figure (crni ili beli), tip figure (kralj, kraljica
    top, lovac, konj ili pijun) i sliku figure.
    """
    def __init__(self, tim, tip, slika):
        """
        :param tim: str: "c", "b" tim figure
        :param tip: str: "pijun", "top", "konj", "lovac", "kraljica", "kralj" tip figure
        :param slika: slika figure formata ".png"
        """
        self.tim = tim
        self.tip = tip
        self.slika = slika


class Kralj(Figura):
    """
    Opis figure kralja. Implementirano da bi se uvela funkcionalnost rokade.
    """
    def __init__(self, tim, tip, slika, pomeren=False):
        """
        :param tim: str: "c", "b" tim figure
        :param tip: str: "pijun", "top", "konj", "lovac", "kraljica", "kralj" tip figure
        :param slika: slika figure formata ".png"
        :param pomeren: Bool: Opisuje da li je kralj jednom pomeren ili ne, zbog implementacije rokade
        """
        super().__init__(tim, tip, slika)
        self.pomeren = pomeren


class Top(Figura):
    """
    Opis figure topa. Implementirano da bi se uvela funkcionalnost rokade.
    """
    def __init__(self, tim, tip, slika, pomeren=False):
        """
        :param tim: str: "c", "b" tim figure
        :param tip: str: "pijun", "top", "konj", "lovac", "kraljica", "kralj" tip figure
        :param slika: slika figure formata ".png"
        :param pomeren: Bool: Opisuje da li je top jednom pomeren ili ne, zbog implementacije rokade
        """
        super().__init__(tim, tip, slika)
        self.pomeren = pomeren


class Pijun(Figura):
    """
    Opis figure pijuna. Implementirano kako bi se uvele funkcionalnosti "En-Passant" i "Promocija".
    """

    def __init__(self, tim, tip, slika, enpassant=False):
        """
        :param tim: str: "c", "b" tim figure
        :param tip: str: "pijun", "top", "konj", "lovac", "kraljica", "kralj" tip figure
        :param slika: slika figure formata ".png"
        :param enpassant: Bool: Opisuje da li je pijunu dozvoljen potez enpassant
        """
        super().__init__(tim, tip, slika)
        self.enpassant = enpassant

    def promovisi(self, tip, slika):
        """
        Menja figuru iz pijuna u drugu koju izabere igrač. Ne može biti promovisan u pijuna ili u kralja.
        :param tip: str: "top", "konj", "lovac", "kraljica"
        :param slika: slika formata ".png"
        :return:
        """
        try:
            self.tip = tip
            self.slika = pygame.image.load(slika)
            return True
        except Exception as e:
            print(f"{e} u klasi Pijun u metodi promovisi")
            return False
