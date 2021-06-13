"""
Ovde postavljam početni raspored šahovnice i u rečnik upisujem klase figura
koje se nalaze na odgovarajućim poljima.

Prvi argument definise tim kojem pripada figura. "c" označava crni tim, "b" označava beli tim
Drugi argument definise tip figure.
Treci argument definise putanju do slike figure.

Podržane figure iz modula chesspieces.py su:
cp.Pijun("c", "pijun", pygame.image.load("slike/c_pijun.png")) - crni pijun
cp.Pijun("b", "pijun", pygame.image.load("slike/b_pijun.png")) - beli pijun
cp.Top("c", "top", pygame.image.load("slike/c_top.png")) - crni top
cp.Top("b", "top", pygame.image.load("slike/b_top.png")) - beli top
cp.Kralj("c", "kralj", pygame.image.load("slike/c_kralj.png")) - crni kralj
cp.Kralj("b", "kralj", pygame.image.load("slike/b_kralj.png")) - beli kralj

cp.Figura("c", "konj", pygame.image.load("slike/c_konj.png")) - crni konj
cp.Figura("b", "konj", pygame.image.load("slike/b_konj.png")) - beli konj
cp.Figura("c", "lovac", pygame.image.load("slike/c_lovac.png")) - crni lovac
cp.Figura("b", "lovac", pygame.image.load("slike/b_lovac.png")) - beli lovac
cp.Figura("c", "kraljica", pygame.image.load("slike/c_kraljica.png")) - crna kraljica
cp.Figura("b", "kraljica", pygame.image.load("slike/b_kraljica.png")) - bela kraljica
"""


import pygame
import chesspieces as cp


"""
Kreiram startni raspored table. Ovakav će biti na početku svake partije.
U svakom polju rečnika gde treba da postoji figura pravim novu instancu figure.
"""
pocetni_raspored_figura = {
    (0, 0): cp.Top("c", "top", pygame.image.load("slike/c_top.png")),
    (1, 0): cp.Figura("c", "konj", pygame.image.load("slike/c_konj.png")),
    (2, 0): cp.Figura("c", "lovac", pygame.image.load("slike/c_lovac.png")),
    (3, 0): cp.Figura("c", "kraljica", pygame.image.load("slike/c_kraljica.png")),
    (4, 0): cp.Kralj("c", "kralj", pygame.image.load("slike/c_kralj.png")),
    (5, 0): cp.Figura("c", "lovac", pygame.image.load("slike/c_lovac.png")),
    (6, 0): cp.Figura("c", "konj", pygame.image.load("slike/c_konj.png")),
    (7, 0): cp.Top("c", "top", pygame.image.load("slike/c_top.png")),

    (0, 1): cp.Pijun("c", "pijun", pygame.image.load("slike/c_pijun.png")),
    (1, 1): cp.Pijun("c", "pijun", pygame.image.load("slike/c_pijun.png")),
    (2, 1): cp.Pijun("c", "pijun", pygame.image.load("slike/c_pijun.png")),
    (3, 1): cp.Pijun("c", "pijun", pygame.image.load("slike/c_pijun.png")),
    (4, 1): cp.Pijun("c", "pijun", pygame.image.load("slike/c_pijun.png")),
    (5, 1): cp.Pijun("c", "pijun", pygame.image.load("slike/c_pijun.png")),
    (6, 1): cp.Pijun("c", "pijun", pygame.image.load("slike/c_pijun.png")),
    (7, 1): cp.Pijun("c", "pijun", pygame.image.load("slike/c_pijun.png")),

    (0, 2): None, (1, 2): None, (2, 2): None, (3, 2): None,
    (4, 2): None, (5, 2): None, (6, 2): None, (7, 2): None,

    (0, 3): None, (1, 3): None, (2, 3): None, (3, 3): None,
    (4, 3): None, (5, 3): None, (6, 3): None, (7, 3): None,

    (0, 4): None, (1, 4): None, (2, 4): None, (3, 4): None,
    (4, 4): None, (5, 4): None, (6, 4): None, (7, 4): None,

    (0, 5): None, (1, 5): None, (2, 5): None, (3, 5): None,
    (4, 5): None, (5, 5): None, (6, 5): None, (7, 5): None,

    (0, 6): cp.Pijun("b", "pijun", pygame.image.load("slike/b_pijun.png")),
    (1, 6): cp.Pijun("b", "pijun", pygame.image.load("slike/b_pijun.png")),
    (2, 6): cp.Pijun("b", "pijun", pygame.image.load("slike/b_pijun.png")),
    (3, 6): cp.Pijun("b", "pijun", pygame.image.load("slike/b_pijun.png")),
    (4, 6): cp.Pijun("b", "pijun", pygame.image.load("slike/b_pijun.png")),
    (5, 6): cp.Pijun("b", "pijun", pygame.image.load("slike/b_pijun.png")),
    (6, 6): cp.Pijun("b", "pijun", pygame.image.load("slike/b_pijun.png")),
    (7, 6): cp.Pijun("b", "pijun", pygame.image.load("slike/b_pijun.png")),

    (0, 7): cp.Top("b", "top", pygame.image.load("slike/b_top.png")),
    (1, 7): cp.Figura("b", "konj", pygame.image.load("slike/b_konj.png")),
    (2, 7): cp.Figura("b", "lovac", pygame.image.load("slike/b_lovac.png")),
    (3, 7): cp.Figura("b", "kraljica", pygame.image.load("slike/b_kraljica.png")),
    (4, 7): cp.Kralj("b", "kralj", pygame.image.load("slike/b_kralj.png")),
    (5, 7): cp.Figura("b", "lovac", pygame.image.load("slike/b_lovac.png")),
    (6, 7): cp.Figura("b", "konj", pygame.image.load("slike/b_konj.png")),
    (7, 7): cp.Top("b", "top", pygame.image.load("slike/b_top.png"))
}

"""
pocetni_raspored_figura = {
    (0, 0): cp.Top("c", "top", pygame.image.load("slike/c_top.png")),
    (1, 0): cp.Figura("c", "konj", pygame.image.load("slike/c_konj.png")),
    (2, 0): cp.Figura("c", "lovac", pygame.image.load("slike/c_lovac.png")),
    (3, 0): cp.Figura("c", "kraljica", pygame.image.load("slike/c_kraljica.png")),
    (4, 0): cp.Kralj("c", "kralj", pygame.image.load("slike/c_kralj.png")),
    (5, 0): cp.Figura("c", "lovac", pygame.image.load("slike/c_lovac.png")),
    (6, 0): cp.Figura("c", "konj", pygame.image.load("slike/c_konj.png")),
    (7, 0): cp.Top("c", "top", pygame.image.load("slike/c_top.png")),

    (0, 1): cp.Pijun("c", "pijun", pygame.image.load("slike/c_pijun.png")),
    (1, 1): cp.Pijun("c", "pijun", pygame.image.load("slike/c_pijun.png")),
    (2, 1): cp.Pijun("c", "pijun", pygame.image.load("slike/c_pijun.png")),
    (3, 1): cp.Pijun("c", "pijun", pygame.image.load("slike/c_pijun.png")),
    (4, 1): cp.Pijun("c", "pijun", pygame.image.load("slike/c_pijun.png")),
    (5, 1): cp.Pijun("c", "pijun", pygame.image.load("slike/c_pijun.png")),
    (6, 1): cp.Pijun("c", "pijun", pygame.image.load("slike/c_pijun.png")),
    (7, 1): cp.Pijun("c", "pijun", pygame.image.load("slike/c_pijun.png")),

    (0, 2): None, (1, 2): None, (2, 2): None, (3, 2): None,
    (4, 2): None, (5, 2): None, (6, 2): None, (7, 2): None,

    (0, 3): None, (1, 3): None, (2, 3): None, (3, 3): None,
    (4, 3): None, (5, 3): None, (6, 3): None, (7, 3): None,

    (0, 4): None, (1, 4): None, (2, 4): None, (3, 4): None,
    (4, 4): None, (5, 4): None, (6, 4): None, (7, 4): None,

    (0, 5): None, (1, 5): None, (2, 5): None, (3, 5): None,
    (4, 5): None, (5, 5): None, (6, 5): None, (7, 5): None,

    (0, 6): cp.Pijun("b", "pijun", pygame.image.load("slike/b_pijun.png")),
    (1, 6): cp.Pijun("b", "pijun", pygame.image.load("slike/b_pijun.png")),
    (2, 6): cp.Pijun("b", "pijun", pygame.image.load("slike/b_pijun.png")),
    (3, 6): cp.Pijun("b", "pijun", pygame.image.load("slike/b_pijun.png")),
    (4, 6): cp.Pijun("b", "pijun", pygame.image.load("slike/b_pijun.png")),
    (5, 6): cp.Pijun("b", "pijun", pygame.image.load("slike/b_pijun.png")),
    (6, 6): cp.Pijun("b", "pijun", pygame.image.load("slike/b_pijun.png")),
    (7, 6): cp.Pijun("b", "pijun", pygame.image.load("slike/b_pijun.png")),

    (0, 7): cp.Top("b", "top", pygame.image.load("slike/b_top.png")),
    (1, 7): cp.Figura("b", "konj", pygame.image.load("slike/b_konj.png")),
    (2, 7): cp.Figura("b", "lovac", pygame.image.load("slike/b_lovac.png")),
    (3, 7): cp.Figura("b", "kraljica", pygame.image.load("slike/b_kraljica.png")),
    (4, 7): cp.Kralj("b", "kralj", pygame.image.load("slike/b_kralj.png")),
    (5, 7): cp.Figura("b", "lovac", pygame.image.load("slike/b_lovac.png")),
    (6, 7): cp.Figura("b", "konj", pygame.image.load("slike/b_konj.png")),
    (7, 7): cp.Top("b", "top", pygame.image.load("slike/b_top.png"))
}
"""

"""
pocetni_raspored_figura = {
    (0, 0): cp.c_top, (1, 0): cp.c_konj, (2, 0): cp.c_lovac, (3, 0): cp.c_kraljica,
    (4, 0): cp.c_kralj, (5, 0): cp.c_lovac, (6, 0): cp.c_konj, (7, 0): cp.c_top,

    (0, 1): cp.c_pijun, (1, 1): cp.c_pijun, (2, 1): cp.c_pijun, (3, 1): cp.c_pijun,
    (4, 1): cp.c_pijun, (5, 1): cp.c_pijun, (6, 1): cp.c_pijun, (7, 1): cp.c_pijun,

    (0, 2): None, (1, 2): None, (2, 2): None, (3, 2): None,
    (4, 2): None, (5, 2): None, (6, 2): None, (7, 2): None,

    (0, 3): None, (1, 3): None, (2, 3): None, (3, 3): None,
    (4, 3): None, (5, 3): None, (6, 3): None, (7, 3): None,

    (0, 4): None, (1, 4): None, (2, 4): None, (3, 4): None,
    (4, 4): None, (5, 4): None, (6, 4): None, (7, 4): None,

    (0, 5): None, (1, 5): None, (2, 5): None, (3, 5): None,
    (4, 5): None, (5, 5): None, (6, 5): None, (7, 5): None,

    (0, 6): cp.b_pijun, (1, 6): cp.b_pijun, (2, 6): cp.b_pijun, (3, 6): cp.b_pijun,
    (4, 6): cp.b_pijun, (5, 6): cp.b_pijun, (6, 6): cp.b_pijun, (7, 6): cp.b_pijun,

    (0, 7): cp.b_top, (1, 7): cp.b_konj, (2, 7): cp.b_lovac, (3, 7): cp.b_kraljica,
    (4, 7): cp.b_kralj, (5, 7): cp.b_lovac, (6, 7): cp.b_konj, (7, 7): cp.b_top
}
"""
