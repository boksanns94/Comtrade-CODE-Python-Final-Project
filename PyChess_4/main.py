import sys
import pygame
import interface as intf


"""
Postavljanje globalnih promenljivih
"""
BELA = (255, 255, 255)
SIVA = (120, 120, 120)
ZUTA = (200, 200, 0)
PLAVA = (160, 200, 255)
CRNA = (0, 0, 0)
SIRINA_TABLE = 513  # Širina i visina cele table u pikselima
KOLONE = 8  # Broj kolona i redova na tabli
SIRINA_POLJA = SIRINA_TABLE // KOLONE  # Širina jednog polja na tabli u pikselima


"""
Inicijalizacija prozora, postavljanje naslova na prozor, inicijalizacija clock-a, postavljanje tick-ova za clock
"""
WIN = pygame.display.set_mode((SIRINA_TABLE, SIRINA_TABLE))  # Inicijalizuje se prozor
pygame.display.set_caption("PyChess")  # Postavlja se naslov na vrhu prozora
CLOCK = pygame.time.Clock()  # Inicijalizujem objekat za clock-ove
FPS = 5  # Postavljam vrednost za impulse Clock-a


def main():
    CLOCK.tick(FPS)

    igra = True
    tim_na_potezu = "b"  # Promenljiva koja će čuvati "c" ili "b" u zavisnosti koji je tim na redu
    figura_na_potezu = ()  # Promenljiva za čuvanje koordinata figure koja je na potezu
    sahovnica = {}  # Glavni rečnik u kojem se nalaze stanja svih polja i figura
    intf.napravi_sahovnicu(sahovnica)  # Kreiram početno stanje šahovnice

    while igra:
        for event in pygame.event.get():   # Ako se desi da korisnik klikne na crveni X da izadje iz igre
            if event.type == pygame.QUIT:  # pojaviće se pygame.QUIT event
                igra = False  # Tada zatvaramo celu igru
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:  # Ako se desi da korisnik klikne mišem
                pozicija_misa = pygame.mouse.get_pos()  # Dobavljamo poziciju miša u pikselima
                kliknuto_polje = intf.nadji_polje(pozicija_misa)  # Dobavljamo polje u kojem je strelica u momentu klika

                if not intf.ima_obelezeno(sahovnica):  # Pitamo da li je sa svih polja sklonjeno obeležavanje
                    if sahovnica[kliknuto_polje].figura:  # Pitamo da li je kliknuto na figuru
                        if sahovnica[kliknuto_polje].figura.tim == tim_na_potezu:  # Da li je figura iz tima na potezu
                            intf.oznaci_poteze(kliknuto_polje, sahovnica)  # Označavamo potencijalne poteze za tu figuru
                            figura_na_potezu = kliknuto_polje  # Upisujemo poziciju figure koja je na potezu
                else:  # Ako bilo gde na šahovnici ima nešto obeleženo
                    # Pitamo da li je kliknuto polje obeleženo ili može da ima specijalan potez
                    if sahovnica[kliknuto_polje].obelezeno or sahovnica[kliknuto_polje].specijalni_potez:
                        if kliknuto_polje == figura_na_potezu:  # Pitamo da li je kliknuta figura na potezu
                            intf.skini_oznake_poteza(sahovnica)  # Ako jeste čistimo sva obeležavanja sa šahovnice
                        else:  # Ako nije figura na potezu
                            if sahovnica[kliknuto_polje].specijalni_potez:  # Pitamo da li je specijalan potez
                                if sahovnica[kliknuto_polje].figura.tip in ["kralj", "top"]:  # Ako je figura kralj ili top
                                    intf.pomeri_rokadu(figura_na_potezu, kliknuto_polje, sahovnica)  # Radimo rokadu
                                elif sahovnica[kliknuto_polje].figura.tip == "pijun":  # Ako je figura pijun
                                    # promocija
                                    pass
                            else:  # Ako nije specijalan potez
                                intf.pomeri_figuru(figura_na_potezu, kliknuto_polje, sahovnica)  # Pomeramo figuru
                            intf.skini_oznake_poteza(sahovnica)  # Čistimo sva obeležavanja sa šahovnice
                            if tim_na_potezu == "b":  # Menjamo tim koje je na redu
                                tim_na_potezu = "c"
                            else:
                                tim_na_potezu = "b"
                    else:  # Ako je kliknuto neobeleženo polje
                        # Pitamo da li je kliknuto na prijateljsku figuru
                        if sahovnica[kliknuto_polje].figura and intf.isti_tim(kliknuto_polje, figura_na_potezu, sahovnica):
                            intf.skini_oznake_poteza(sahovnica)  # Skidamo sva prethodna obeležavanja sa šahovnice
                            intf.oznaci_poteze(kliknuto_polje, sahovnica)  # Označavamo potencijalne poteze za tu figuru
                            figura_na_potezu = kliknuto_polje  # Upisujemo poziciju figure koja je na potezu
                        else:
                            intf.skini_oznake_poteza(sahovnica)  # Skidamo sva prethodna obeležavanja sa šahovnice

        intf.azuriraj_sliku(WIN, sahovnica)  # Ažuriramo grafičko stanje cele šahovnice


if __name__ == '__main__':
    main()
