"""
Ovde će biti definisane figure, njihove uloge, timovi i slike.
Ovde će se čuvati raspored figura na tabli.
Takođe će biti definisan način na koji svaka figura sme da se pomera.
"""


import pygame


class Figura:
    """
    Opšti opis figure. Sadrži tim figure (crni ili beli), tip figure (kralj, kraljica
    top, lovac, konj ili pijun) i sliku figure.
    """
    def __init__(self, tim, tip, slika):
        """
        :param tim: str: "c", "b"
        :param tip: str: "pijun", "top", "konj", "lovac", "kraljica", "kralj"
        :param slika: slika formata ".png"
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
        :param tim: str: "c", "b"
        :param tip: str: "kralj"
        :param slika: slika formata ".png"
        :param pomeren: Bool
        """
        Figura.__init__(self, tim, tip, slika)
        self.pomeren = pomeren


class Top(Figura):
    """
    Opis figure topa. Implementirano da bi se uvela funkcionalnost rokade.
    """
    def __init__(self, tim, tip, slika, pomeren=False):
        """
        :param tim: str: "c", "b"
        :param tip: str: "top"
        :param slika: slika formata ".png"
        :param pomeren: Bool
        """
        Figura.__init__(self, tim, tip, slika)
        self.pomeren = pomeren


class Pijun(Figura):
    """
    Opis figure pijuna. Implementirano kako bi se uvele funkcionalnosti "En-Passant" i "Promocija".
    """
    def __init__(self, tim, tip, slika, prosao=False, promocija=False):
        """
        :param tim: str: "c", "b"
        :param tip: str: "pijun"
        :param slika: slika formata ".png"
        :param prosao: Bool
        :param promocija: Bool
        """
        Figura.__init__(self, tim, tip, slika)
        self.prosao = prosao
        self.promocija = promocija

    def promovisi(self, tip, slika):
        """
        Menja figuru iz pijuna u drugu koju izabere igrač. Ne može biti promovisan u pijuna ili u kralja.
        :param tip: str: "top", "konj", "lovac", "kraljica"
        :param slika: slika formata ".png"
        :return:
        """
        if tip != "kralj" and tip != "pijun":
            self.tip = tip
        self.slika = pygame.image.load(slika)


"""
Inicijalizujemo sve vrste figura na pоčetne vrednosti: tim, tip i sliku.
Prvi argument definise tim kojem pripada figura.
Drugi argument definise tip figure.
Treci argument definise putanju do slike figure.
"""
c_pijun = Pijun("c", "pijun", pygame.image.load("slike/c_pijun.png"))
b_pijun = Pijun("b", "pijun", pygame.image.load("slike/b_pijun.png"))
c_top = Top("c", "top", pygame.image.load("slike/c_top.png"))
b_top = Top("b", "top", pygame.image.load("slike/b_top.png"))
c_kralj = Kralj("c", "kralj", pygame.image.load("slike/c_kralj.png"))
b_kralj = Kralj("b", "kralj", pygame.image.load("slike/b_kralj.png"))

c_konj = Figura("c", "konj", pygame.image.load("slike/c_konj.png"))
b_konj = Figura("b", "konj", pygame.image.load("slike/b_konj.png"))
c_lovac = Figura("c", "lovac", pygame.image.load("slike/c_lovac.png"))
b_lovac = Figura("b", "lovac", pygame.image.load("slike/b_lovac.png"))
c_kraljica = Figura("c", "kraljica", pygame.image.load("slike/c_kraljica.png"))
b_kraljica = Figura("b", "kraljica", pygame.image.load("slike/b_kraljica.png"))


"""
Kreiram startni raspored table. Ovakav će biti na početku svake partije.
U toku partije ovaj raspored će se menjati, a promene će se čuvati ovde.
"""
raspored_figura = {
    (0, 0): c_top, (1, 0): c_konj, (2, 0): c_lovac, (3, 0): c_kraljica,
    (4, 0): c_kralj, (5, 0): c_lovac, (6, 0): c_konj, (7, 0): c_top,

    (0, 1): c_pijun, (1, 1): c_pijun, (2, 1): c_pijun, (3, 1): c_pijun,
    (4, 1): c_pijun, (5, 1): c_pijun, (6, 1): c_pijun, (7, 1): c_pijun,

    (0, 2): c_pijun, (1, 2): None, (2, 2): c_pijun, (3, 2): None,
    (4, 2): None, (5, 2): None, (6, 2): None, (7, 2): None,

    (0, 3): None, (1, 3): c_top, (2, 3): None, (3, 3): None,
    (4, 3): None, (5, 3): None, (6, 3): c_pijun, (7, 3): b_pijun,

    (0, 4): None, (1, 4): None, (2, 4): None, (3, 4): None,
    (4, 4): None, (5, 4): None, (6, 4): None, (7, 4): None,

    (0, 5): None, (1, 5): None, (2, 5): None, (3, 5): None,
    (4, 5): b_pijun, (5, 5): None, (6, 5): c_pijun, (7, 5): None,

    (0, 6): b_pijun, (1, 6): b_pijun, (2, 6): b_pijun, (3, 6): b_pijun,
    (4, 6): b_pijun, (5, 6): b_pijun, (6, 6): b_pijun, (7, 6): b_pijun,

    (0, 7): b_top, (1, 7): b_konj, (2, 7): b_lovac, (3, 7): b_kraljica,
    (4, 7): b_kralj, (5, 7): b_lovac, (6, 7): b_konj, (7, 7): b_top
}


def unutar_table(pozicija):
    """
    Funkcija za ispitivanje da li se red i kolona polja u pitanju nalaze unutar dimenzija table
    :param pozicija: Tuple: Koordinate polja koje se ispituje
    :return: Bool: Rezultat ispitivanja da li se koordinata nalazi unutar table
    """
    if 0 <= pozicija[0] < 8 and 0 <= pozicija[1] < 8:
        return True


def iscrtaj_potez(pozicija, sahovnica):
    try:
        if sahovnica[pozicija].figura.tip == "kralj":
            pomeri_kralja(pozicija, sahovnica)
        if sahovnica[pozicija].figura.tip == "top":
            pomeri_topa(pozicija, sahovnica)
        if sahovnica[pozicija].figura.tip == "lovac":
            pomeri_lovca(pozicija, sahovnica)
        if sahovnica[pozicija].figura.tip == "kraljica":
            pomeri_kraljicu(pozicija, sahovnica)
        if sahovnica[pozicija].figura.tip == "konj":
            pomeri_konja(pozicija, sahovnica)
        if sahovnica[pozicija].figura.tip == "pijun":
            pomeri_pijuna(pozicija, sahovnica)
    except Exception as e:
        pass


def proveri_potez(potez, pozicija, sahovnica):
    x = potez[0]
    y = potez[1]
    if unutar_table((x, y)):  # Ako su koordinate potencijalnog poteza u okviru table
        if sahovnica[(x, y)].figura:  # Pitamo da li na tom polju postoji figura
            if sahovnica[(x, y)].figura.tim != sahovnica[pozicija].figura.tim:  # Pitamo da li je suprotnog tima
                sahovnica[(x, y)].obelezeno = True  # Obeležavamo polje
        else:
            sahovnica[(x, y)].obelezeno = True  # Ako je polje prazno odma ga obeležavamo

    sahovnica[pozicija].obelezeno = True


def pomeri_kralja(pozicija, sahovnica):
    """
    Funkcija za definisanje dozvoljenih poteza kralja.
    :param pozicija: Tuple: (kolona, red) Polje u kojem se figura nalazi
    :param sahovnica: Dict: Sadrzi pozicije svih figura i stanja svih polja na celoj tabli
    :return None
    """
    # Popisujemo svih potencijalnih 8 poteza koje kralj može da uradi
    offset = range(-1, 2)
    potencijalni_potezi = [(i, j) for i in offset for j in offset if i != 0 or j != 0]

    for potez in potencijalni_potezi:
        proveri_potez(potez, pozicija, sahovnica)


def pomeri_topa(pozicija, sahovnica):
    """
    Funkcija za definisanje dozvoljenih poteza topa.
    :param pozicija: Tuple: (kolona, red) Polje u kojem se figura nalazi
    :param sahovnica: Dict: Sadrzi pozicije svih figura i stanja svih polja na celoj tabli
    :return None
    """
    potencijalni_potezi = [  # Popisujemo sve poteze topa u 4 smera u kojima može da se kreće
        [(pozicija[0] + i, pozicija[1]) for i in range(1, 8 - pozicija[0])],  # Lista poteza u smeru desno od topa
        [(pozicija[0] - i, pozicija[1]) for i in range(1, pozicija[0] + 1)],  # Lista poteza u smeru levo od topa
        [(pozicija[0], pozicija[1] + i) for i in range(1, 8 - pozicija[1])],  # Lista poteza u smeru dole od topa
        [(pozicija[0], pozicija[1] - i) for i in range(1, pozicija[1] + 1)]  # Lista poteza u smeru gore od topa
    ]

    for smerovi in potencijalni_potezi:
        for potez in smerovi:
            proveri_potez(potez, pozicija, sahovnica)


def pomeri_lovca(pozicija, sahovnica):
    """
    Funkcija za definisanje dozvoljenih poteza lovca.
    :param pozicija: Tuple: (kolona, red) Polje u kojem se figura nalazi
    :param sahovnica: Dict: Sadrzi pozicije svih figura i stanja svih polja na celoj tabli
    :return None
    """
    potencijalni_potezi = [  # Popisujemo sve poteze lovca u 4 smera u kojima može da se kreće
        [(pozicija[0] + i, pozicija[1] - i) for i in range(1, 8)],  # Lista poteza u smeru desno-gore od lovca
        [(pozicija[0] - i, pozicija[1] - i) for i in range(1, 8)],  # Lista poteza u smeru levo-gore od lovca
        [(pozicija[0] + i, pozicija[1] + i) for i in range(1, 8)],  # Lista poteza u smeru desno-dole od lovca
        [(pozicija[0] - i, pozicija[1] - i) for i in range(1, 8)]  # Lista poteza u smeru levo-dole od lovca
    ]

    for smerovi in potencijalni_potezi:
        for potez in smerovi:
            proveri_potez(potez, pozicija, sahovnica)


def pomeri_kraljicu(pozicija, sahovnica):
    """
    Funkcija za definisanje dozvoljenih poteza kraljice. Potencijalni potezi kraljice
    su u suštini kombinovani potencijalni potezi lovca i topa.
    :param pozicija: Tuple: (kolona, red) Polje u kojem se figura nalazi
    :param sahovnica: Dict: Sadrzi pozicije svih figura i stanja svih polja na celoj tabli
    :return None
    """
    pomeri_topa(pozicija, sahovnica)
    pomeri_lovca(pozicija, sahovnica)


def pomeri_konja(pozicija, sahovnica):
    """
    Funkcija za definisanje dozvoljenih poteza konja.
    :param pozicija: Tuple: (kolona, red) Polje u kojem se figura nalazi
    :param sahovnica: Dict: Sadrzi pozicije svih figura i stanja svih polja na celoj tabli
    :return: None
    """
    # Popisujemo svih potencijalnih 8 poteza koje konj može da uradi
    offset = [-1, 1, -2, 2]
    potencijalni_potezi = [(pozicija[0] + a, pozicija[1] + b) for a in offset for b in offset if a+b != 0 and a != b]

    for potez in potencijalni_potezi:
        proveri_potez(potez, pozicija, sahovnica)


def pomeri_pijuna(pozicija, sahovnica):
    """
    Funkcija za definisanje dozvoljenih poteza pijuna.
    Implementirani specijalni potezi pijuna: ukoso jedenje figura, nemogućnost kretanja ako ima figuru ispred sebe
    kao i dupli pomeraj sa startnog mesta.
    :param pozicija: Tuple: (kolona, red) Polje u kojem se figura nalazi
    :param sahovnica: Dict: Sadrzi pozicije svih figura i stanja svih polja na celoj tabli
    :return: None
    """
    if sahovnica[pozicija].figura.tim == "c":  # Y crnog pijuna raste pri pomeranju, postavljam pozitivan modifier
        smer = 1
    elif sahovnica[pozicija].figura.tim == "b":  # Y belog pijuna opada pri pomeranju, postavljam negativan modifier
        smer = -1
    else:
        smer = 0

    # Redovan potez pijuna
    x = pozicija[0]
    y = pozicija[1]+smer
    if unutar_table((x, y)):  # Ako su koordinate potencijalnog poteza u okviru table
        if not sahovnica[(x, y)].figura:  # Pitamo da li na tom polju ne postoji figura
            sahovnica[(x, y)].obelezeno = True  # Obeležavamo polje

    # Dupli potez pijuna sa startne linije
    y2 = y + smer
    if pozicija[1] == 1 or pozicija[1] == 6:  # Ako se pijun nalazi početnoj poziciji (u zavisnosti od tima)
        if not sahovnica[(x, y)].figura:
            if unutar_table((x, y2)):  # Ako su koordinate potencijalnog poteza u okviru table
                if not sahovnica[(x, y2)].figura:  # Pitamo da li na tom polju ne postoji figura
                    sahovnica[(x, y2)].obelezeno = True  # Obeležavamo polje

    # Jedenje pijunom
    # Potencijalni potezi su nam polja dijagonalno ispred i levo i desno od pijuna
    potencijalni_potezi = [(pozicija[0]-1, pozicija[1]+smer), (pozicija[0]+1, pozicija[1]+smer)]
    for potez in potencijalni_potezi:
        if unutar_table(potez):  # Ako su koordinate potencijalnog poteza u okviru table
            if sahovnica[potez].figura:  # Pitamo da li na tom polju postoji figura
                if sahovnica[(x, y)].figura.tim != sahovnica[pozicija].figura.tim:  # Pitamo da li je suprotnog tima
                    sahovnica[potez].obelezeno = True  # Obeležavamo polje

    sahovnica[pozicija].obelezeno = True
