"""
Ovde će biti definisane pomoćne funkcije koje služe za proveru svih potencijalnih poteza,
za proveru ispravnosti tih poteza, za sam pomeraj figura i za ispitivanje uslova za specijane
slučajeve kao što su rokada, promocija i en-passant.
Takođe će biti definisane funkcije za pronalaženje polja na koje je kliknuo korisnik, za
generisanje početnog stanja šahovnice, kao i za iscrtavanje izgleda trenutnog stanja šahovnice.
"""

import pygame
import chessfield as cf
import startboard as sb

BOJA_TAMNOG_POLJA = (120, 120, 120)
BOJA_SVETLOG_POLJA = (255, 255, 255)
CRNA = (0, 0, 0)
SIRINA_TABLE = 513  # Širina i visina cele table u pikselima
KOLONE = 8  # Broj kolona i redova na tabli
SIRINA_POLJA = SIRINA_TABLE // KOLONE  # Širina jednog polja na tabli u pikselima


def napravi_sahovnicu(sahovnica):
    """
    Funkcija za generisanje početnog stanja šahovske table. Postavljanje naizmeničnih sivih i belih polja.
    :param sahovnica: Dict: Rečnik sa klasama Polje koji sadrži stanja svih polja na tabli.
    :return: None
    """
    for i in range(KOLONE):  # Za svaki red (ima ih isto kao i kolona)
        for j in range(KOLONE):  # Za svaku kolonu
            sahovnica[(i, j)] = cf.Polje(i, j, sb.pocetni_raspored_figura[(i, j)])  # Inicijalizujemo polje sa figurom
            if (i + j) % 2 == 1:  # Svako naizmenično polje bojimo u tamniju boju
                sahovnica[(i, j)].boja = BOJA_TAMNOG_POLJA
            else:
                sahovnica[(i, j)].boja = BOJA_SVETLOG_POLJA


def azuriraj_sliku(win, sahovnica):
    """
    Funkcija za ažuriranje izgleda polja šahovske table ispod figura.
    Iscrtava i vertikalne i horizontalne linije koje se nalaze između polja.
    :param win: win: Prozor u kojem će se ažurirati polja.
    :param sahovnica: Dict: Rečnik sa klasama Polje koji sadrži stanja svih polja na tabli.
    :return:
    """
    for i in range(KOLONE):  # Za svaki red (ima ih isto kao i kolona)
        for j in range(KOLONE):  # Za svaku kolonu
            sahovnica[(i, j)].crtaj(win)  # Iscrtaj polje (pravougaonik i boja)
            sahovnica[(i, j)].postavi(win)  # Iscrtaj figuru koja se nalazi na tom polju

    # Iscrtavanje vertikalnih i horizontalnih linija između polja
    for i in range(KOLONE + 1):
        pygame.draw.line(win, CRNA, (0, i * SIRINA_POLJA), (SIRINA_TABLE, i * SIRINA_POLJA))
        for j in range(KOLONE + 1):
            pygame.draw.line(win, CRNA, (j * SIRINA_POLJA, 0), (j * SIRINA_POLJA, SIRINA_TABLE))

    pygame.display.update()  # Iscrtaj sliku na ekranu


def nadji_polje(pozicija_misa):
    """
    Funkcija za ispitivanje na koje je polje šahovnice kliknuto u zavisnosti od koordinata miša.
    :param pozicija_misa: Tuple: (x, y) Pozicija miša u pikselima.
    :return: Tuple: (red, kolona) Koordinate polja šahovnice.
    """
    red = pozicija_misa[0] // SIRINA_POLJA
    kolona = pozicija_misa[1] // SIRINA_POLJA
    return red, kolona


def unutar_table(pozicija):
    """
    Funkcija za ispitivanje da li se red i kolona polja u pitanju nalaze unutar dimenzija table.
    :param pozicija: Tuple: (x, y) koordinate polja koje se ispituje.
    :return: Bool: Rezultat ispitivanja da li se koordinata nalazi unutar table.
    """
    return 0 <= pozicija[0] < 8 and 0 <= pozicija[1] < 8


def isti_tim(potencijalni_potez, trenutna_pozicija, sahovnica):
    """
    Funkcija za ispitivanje da li su figure na dva polja iz istog tima.
    :param potencijalni_potez: Tuple: (x, y) koordinate polja druge figure.
    :param trenutna_pozicija: (x, y) koordinate figure koja je izabrana.
    :param sahovnica: Dict: Sadrži pozicije svih figura i stanja svih polja na celoj tabli.
    :return: Bool: Rezultat ispitivanja da li su figure u istom timu.
    """
    return sahovnica[potencijalni_potez].figura.tim == sahovnica[trenutna_pozicija].figura.tim


def oznaci_potez(potencijalni_potez, trenutna_pozicija, sahovnica):
    """
    Funkcija za označavanje polja za koje se utvrdi da može da bude dozvoljen potez.
    :param potencijalni_potez: Tuple: (x, y) koordinate polja koje se ispituje kao potencijalni potez.
    :param trenutna_pozicija: Tuple: (x, y) koordinate figure koja je izabrana.
    :param sahovnica: Dict: Sadrži pozicije svih figura i stanja svih polja na celoj tabli.
    :return: None
    """
    pp = potencijalni_potez
    tp = trenutna_pozicija
    if unutar_table(potencijalni_potez):  # Ako su koordinate potencijalnog poteza u okviru table
        if sahovnica[(pp[0], pp[1])].figura:  # Pitamo da li na tom polju postoji figura
            if not isti_tim((pp[0], pp[1]), (tp[0], tp[1]), sahovnica):  # Pitamo da li je suprotnog tima
                sahovnica[(pp[0], pp[1])].obelezeno = True  # Obeležavamo polje
            # Proveravamo da li je figura na potezu top ili lovac, i određujemo da li da zaustavimo pretragu
            # potencijalnih poteza u smerovima njihovog kretanja ako smo naišli na figuru
            if sahovnica[(tp[0], tp[1])].figura.tip == "top" or sahovnica[(tp[0], tp[1])].figura.tip == "lovac":
                return False
        else:
            sahovnica[(pp[0], pp[1])].obelezeno = True  # Ako je polje prazno odma ga obeležavamo bez dodatnih provera
            # Dajemo povratnu informaciju ako su u pitanju top ili lovac da se nastavi pretraga u njihovom
            # smeru kretanja
            return True


def skini_oznake_poteza(sahovnica):
    """
    Funkcija za uklanjanje oznaka na poljima koja su služila za prikaz potencijalnih poteza.
    :param sahovnica: Dict: Sadrži pozicije svih figura i stanja svih polja na celoj tabli.
    :return: None
    """
    for polje in sahovnica.keys():
        sahovnica[polje].obelezeno = False
        sahovnica[polje].specijalni_potez = False


def ima_obelezeno(sahovnica):
    """
    Funkcija za ispitivanje da li bilo gde na šahovnici postoji označeno polje.
    :param sahovnica: Dict: Sadrži pozicije svih figura i stanja svih polja na celoj tabli.
    :return: Bool: Rezultat ispitivanja da li postoji označeno polje bilo gde na šahovnici.
    """
    for polje in sahovnica.keys():
        if sahovnica[polje].obelezeno or sahovnica[polje].specijalni_potez:
            return True
    return False


def oznaci_poteze(trenutna_pozicija, sahovnica):
    """
    Funkcija koja prepoznaje koja figura je na potezu i pokreće proveru dozvoljenih poteza za tu figuru.
    :param trenutna_pozicija: Tuple: (x, y) koordinate figure koja je izabrana.
    :param sahovnica: Dict: Sadrži pozicije svih figura i stanja svih polja na celoj tabli.
    :return: None
    """
    try:
        if sahovnica[trenutna_pozicija].figura.tip == "kralj":
            oznaci_poteze_kralja(trenutna_pozicija, sahovnica)
        elif sahovnica[trenutna_pozicija].figura.tip == "top":
            oznaci_poteze_topa(trenutna_pozicija, sahovnica)
        elif sahovnica[trenutna_pozicija].figura.tip == "lovac":
            oznaci_poteze_lovca(trenutna_pozicija, sahovnica)
        elif sahovnica[trenutna_pozicija].figura.tip == "kraljica":
            oznaci_poteze_kraljice(trenutna_pozicija, sahovnica)
        elif sahovnica[trenutna_pozicija].figura.tip == "konj":
            oznaci_poteze_konja(trenutna_pozicija, sahovnica)
        elif sahovnica[trenutna_pozicija].figura.tip == "pijun":
            oznaci_poteze_pijuna(trenutna_pozicija, sahovnica)
    except Exception as e:
        print(f"{e} u funkciji: oznaci_poteze")
        pass


def oznaci_poteze_kralja(trenutna_pozicija, sahovnica):
    """
    Funkcija za ispitivanje dozvoljenih poteza kralja.
    :param trenutna_pozicija: Tuple: (kolona, red) Polje u kojem se kralj nalazi.
    :param sahovnica: Dict: Sadrži pozicije svih figura i stanja svih polja na celoj tabli.
    :return None
    """
    sahovnica[trenutna_pozicija].obelezeno = True  # Obelezavamo poziciju na kojoj se sam kralj nalazi

    # Popisujemo svih potencijalnih 8 poteza koje kralj može da uradi
    offset = range(-1, 2)
    x = trenutna_pozicija[0]
    y = trenutna_pozicija[1]
    potencijalni_potezi = [(i + x, j + y) for i in offset for j in offset if i != 0 or j != 0]

    for potencijalni_potez in potencijalni_potezi:
        oznaci_potez(potencijalni_potez, trenutna_pozicija, sahovnica)

    # Rokada od kralja
    if not sahovnica[(x, y)].figura.pomeren:  # Ako kralj nije pomeren
        koordinate_topova = [0, 7]  # Potencijalna mesta topova levo i desno od kralja
        for x2 in koordinate_topova:  # Za svako potencijalno polje sa topom
            if sahovnica[(x2, y)].figura:  # Da li na polju postoji figura
                if sahovnica[(x2, y)].figura.tip == "top":  # Da li na polju stoji top
                    if sahovnica[(x2, y)].figura.tim == sahovnica[(x, y)].figura.tim:  # Da li je top istog tima
                        if not sahovnica[(x2, y)].figura.pomeren:  # Da li taj top nije pomeren
                            # Ako nije pomeren top popisujemo mesta gde ne sme biti figura da bi rokada bila validna
                            prepreke_rokade = []
                            if x2 == 0:  # Ako je top levo od kralja
                                prepreke_rokade = [(i, y) for i in range(1, 4)]  # (1,0) (2,0) (3,0)
                            elif x2 == 7:  # Ako je top desno od kralja
                                prepreke_rokade = [(i, y) for i in range(5, 7)]  # (5,0) (6,0)
                            nema_prepreka = True  # Pretpostavljamo da nema prepreka
                            for prepreka in prepreke_rokade:  # Ispitujemo da li ima prepreka
                                if sahovnica[prepreka].figura:
                                    nema_prepreka = False
                            if nema_prepreka:
                                sahovnica[(x2, y)].specijalni_potez = True  # Postavljamo topa validnim za rokadu
                                sahovnica[(x, y)].specijalni_potez = True  # Postavljamo kralja validnim za rokadu


def oznaci_poteze_topa(trenutna_pozicija, sahovnica):
    """
    Funkcija za definisanje dozvoljenih poteza topa.
    :param trenutna_pozicija: Tuple: (kolona, red) Polje u kojem se top nalazi.
    :param sahovnica: Dict: Sadrži pozicije svih figura i stanja svih polja na celoj tabli.
    :return None
    """
    sahovnica[trenutna_pozicija].obelezeno = True  # Obelezavamo poziciju na kojoj se sam top nalazi

    # Popisujemo sve poteze topa u 4 smera u kojima može da se kreće
    x = trenutna_pozicija[0]
    y = trenutna_pozicija[1]
    potencijalni_potezi = [
        [(x + i, y) for i in range(1, 8)],  # Lista poteza u smeru desno od topa
        [(x - i, y) for i in range(1, 8)],  # Lista poteza u smeru levo od topa
        [(x, y + i) for i in range(1, 8)],  # Lista poteza u smeru dole od topa
        [(x, y - i) for i in range(1, 8)]  # Lista poteza u smeru gore od topa
    ]

    for smer in potencijalni_potezi:
        for potencijalna_pozicija in smer:
            if not oznaci_potez(potencijalna_pozicija, trenutna_pozicija, sahovnica):
                break

    # Rokada od topa
    # Pošto koristimo ovu celu funkciju i za i za ispitivanje dela poteza kraljice pitamo da li je figura top
    if sahovnica[trenutna_pozicija].figura.tip == "top":
        if not sahovnica[(x, y)].figura.pomeren:  # Ako top nije pomeren
            if sahovnica[(4, y)].figura.tip == "kralj":  # Da li se kralj nalazi na svojoj početnoj poziciji
                if sahovnica[(4, y)].figura.tim == sahovnica[(x, y)].figura.tim:  # Da li je kralj istog tima
                    if not sahovnica[(4, y)].figura.pomeren:  # Da li taj kralj nije pomeren
                        # Ako nije pomeren kralj popisujemo mesta gde ne sme biti figura da bi rokada bila validna
                        prepreke_rokade = []
                        if x == 0:  # Ako top stoji levo od kralja
                            prepreke_rokade = [(i, y) for i in range(1, 4)]
                        elif x == 7:
                            prepreke_rokade = [(i, y) for i in range(5, 7)]
                        nema_prepreka = True  # Pretpostavljamo da nema prepreka
                        for prepreka in prepreke_rokade:  # Ispitujemo da li ima prepreka
                            if sahovnica[prepreka].figura:
                                nema_prepreka = False
                        if nema_prepreka:
                            sahovnica[(4, y)].specijalni_potez = True  # Postavljamo kralja validnim za rokadu
                            sahovnica[(x, y)].specijalni_potez = True  # Postavljamo topa validnim za rokadu


def oznaci_poteze_lovca(trenutna_pozicija, sahovnica):
    """
    Funkcija za definisanje dozvoljenih poteza lovca.
    :param trenutna_pozicija: Tuple: (kolona, red) Polje u kojem se figura nalazi.
    :param sahovnica: Dict: Sadrži pozicije svih figura i stanja svih polja na celoj tabli.
    :return None
    """
    sahovnica[trenutna_pozicija].obelezeno = True  # Obelezavamo poziciju na kojoj se sam lovac nalazi

    # Popisujemo sve poteze lovca u 4 smera u kojima može da se kreće
    x = trenutna_pozicija[0]
    y = trenutna_pozicija[1]
    potencijalni_potezi = [
        [(x + i, y - i) for i in range(1, 8)],  # Lista poteza u smeru desno-gore od lovca
        [(x - i, y - i) for i in range(1, 8)],  # Lista poteza u smeru levo-gore od lovca
        [(x + i, y + i) for i in range(1, 8)],  # Lista poteza u smeru desno-dole od lovca
        [(x - i, y + i) for i in range(1, 8)]  # Lista poteza u smeru levo-dole od lovca
    ]

    for smer in potencijalni_potezi:
        for potencijalna_pozicija in smer:
            if not oznaci_potez(potencijalna_pozicija, trenutna_pozicija, sahovnica):
                break


def oznaci_poteze_kraljice(trenutna_pozicija, sahovnica):
    """
    Funkcija za definisanje dozvoljenih poteza kraljice. Potencijalni potezi kraljice
    su u suštini kombinovani potencijalni potezi lovca i topa.
    :param trenutna_pozicija: Tuple: (kolona, red) Polje u kojem se figura nalazi.
    :param sahovnica: Dict: Sadrži pozicije svih figura i stanja svih polja na celoj tabli.
    :return None
    """
    sahovnica[trenutna_pozicija].obelezeno = True  # Obelezavamo poziciju na kojoj se sama kraljica nalazi

    # Pravila po kojima se kraljica kreće je u suštini sabrano kretanje i lovca i topa
    oznaci_poteze_topa(trenutna_pozicija, sahovnica)
    oznaci_poteze_lovca(trenutna_pozicija, sahovnica)


def oznaci_poteze_konja(trenutna_pozicija, sahovnica):
    """
    Funkcija za definisanje dozvoljenih poteza konja.
    :param trenutna_pozicija: Tuple: (kolona, red) Polje u kojem se figura nalazi.
    :param sahovnica: Dict: Sadrži pozicije svih figura i stanja svih polja na celoj tabli.
    :return: None
    """
    sahovnica[trenutna_pozicija].obelezeno = True  # Obelezavamo poziciju na kojoj se sam konj nalazi

    # Popisujemo svih potencijalnih 8 poteza koje konj može da uradi
    offset = [-1, 1, -2, 2]
    x = trenutna_pozicija[0]
    y = trenutna_pozicija[1]
    potencijalni_potezi = [(x + a, y + b) for a in offset for b in offset if a + b != 0 and a != b]

    for potencijalna_pozicija in potencijalni_potezi:
        oznaci_potez(potencijalna_pozicija, trenutna_pozicija, sahovnica)


def oznaci_poteze_pijuna(trenutna_pozicija, sahovnica):
    """
    Funkcija za definisanje dozvoljenih poteza pijuna.
    Implementirani specijalni potezi pijuna: ukoso jedenje figura, nemogućnost kretanja ako ima figuru ispred sebe
    kao i dupli pomeraj sa startnog mesta.
    :param trenutna_pozicija: Tuple: (kolona, red) Polje u kojem se figura nalazi.
    :param sahovnica: Dict: Sadrži pozicije svih figura i stanja svih polja na celoj tabli.
    :return: None
    """
    sahovnica[trenutna_pozicija].obelezeno = True  # Obelezavamo poziciju na kojoj se sam pijun nalazi

    smer = 0  # Utvrđivanje smera kretanja pijuna u zavisnosti od tima kojem pripada
    if sahovnica[trenutna_pozicija].figura.tim == "c":
        smer = 1  # Y crnog pijuna raste pri pomeranju, postavljam pozitivan modifier
    if sahovnica[trenutna_pozicija].figura.tim == "b":
        smer = -1  # Y belog pijuna opada pri pomeranju, postavljam negativan modifier

    x = trenutna_pozicija[0]
    y = trenutna_pozicija[1]

    # Redovan potez pijuna
    y1 = y + smer
    if unutar_table((x, y1)):  # Ako su koordinate potencijalnog poteza u okviru table
        if not sahovnica[(x, y1)].figura:  # Pitamo da li na tom polju ne postoji figura
            sahovnica[(x, y1)].obelezeno = True  # Obeležavamo polje

    # Dupli potez pijuna sa startne linije
    y2 = y + (2 * smer)
    if y in [1, 6]:  # Ako se crni pijun nalazi u redu 1 ili se beli nalazi u redu 6
        if unutar_table((x, y2)):  # Ako su koordinate potencijalnog poteza u okviru table
            if not sahovnica[(x, y1)].figura:  # Pitamo da li na polju odma ispred pijuna ne postoji figura
                if not sahovnica[(x, y2)].figura:  # Pitamo da li na potencijalnom polju ne postoji figura
                    sahovnica[(x, y2)].obelezeno = True  # Obeležavamo polje

    # Jedenje pijunom
    # Potencijalni potezi su nam polja dijagonalno levo i desno od pijuna u smeru kretanja pijuna
    potencijalni_potezi = [(x - 1, y + smer), (x + 1, y + smer)]
    for potencijalna_pozicija in potencijalni_potezi:
        if unutar_table(potencijalna_pozicija):  # Ako su koordinate potencijalnog poteza u okviru table
            if sahovnica[potencijalna_pozicija].figura:  # Pitamo da li na tom polju postoji figura
                if not isti_tim(potencijalna_pozicija, trenutna_pozicija, sahovnica):  # Pitamo da li je suprotnog tima
                    sahovnica[potencijalna_pozicija].obelezeno = True  # Obeležavamo polje

    # enpassant
    # Potencijalni potezi su nam kao kad jedemo ali samo ako pored postoji pijun koji je ispunio enpassant uslov
    potencijalni_potezi = [(x - 1, y + smer), (x + 1, y + smer)]
    for enpassant in potencijalni_potezi:
        if unutar_table(enpassant):  # Ako su koordinate potencijalnog enpassant-a u okviru table
            if not sahovnica[enpassant].figura:  # Pitamo da li na tom polju ne postoji figura
                if sahovnica[(enpassant[0], enpassant[1] - smer)].figura:  # Ako na polju iza enpassant-a ima figura
                    if sahovnica[(enpassant[0], enpassant[1] - smer)].figura.tip == "pijun":  # Ako je ta figura pijun
                        if sahovnica[(enpassant[0], enpassant[1] - smer)].figura.enpassant:  # Ako ima uslov za enpassant
                            sahovnica[(enpassant[0], enpassant[1] - smer)].specijalni_potez = True  # Obelezavamo pijuna
                            sahovnica[enpassant].obelezeno = True  # Obeležavamo polje za enpassant


def pomeri_figuru(figura_na_potezu, validno_polje, sahovnica):
    """
    Funkcija za pomeranje figure.
    Takođe proverava da li se pomerajem stiču ili gube uslovi za neki od specijalnih pomeraja u
    šahu, naime za rokadu, enpassant i promociju.
    :param figura_na_potezu: Tuple: (x, y) koordinate figure koja pravi pomeraj.
    :param validno_polje: Tuple: (x, y) koordinate polja na koji će se pomeriti figura.
    :param sahovnica: Dict: Sadrži pozicije svih figura i stanja svih polja na celoj tabli.
    :return: None
    """
    # Proveravamo da li se pomera kralj ili top zbog rokade
    if sahovnica[figura_na_potezu].figura.tip in ["kralj", "top"]:
        sahovnica[figura_na_potezu].figura.pomeren = True  # Sprečavamo buduće rokade

    # Proveravamo da li se pomera pijun zbog dodele, ukidanja i izvršavanja enpassant-a i promocije
    if sahovnica[figura_na_potezu].figura.tip == "pijun":
        smer = 0  # Utvrđivanje smera kretanja pijuna u zavisnosti od tima kojem pripada
        if sahovnica[figura_na_potezu].figura.tim == "c":
            smer = 1  # Y crnog pijuna raste pri pomeranju, postavljam pozitivan modifier
        if sahovnica[figura_na_potezu].figura.tim == "b":
            smer = -1  # Y belog pijuna opada pri pomeranju, postavljam negativan modifier

        # Proveravamo da li postoji uslov da se pijunu dodeli ili ukine pravo na enpassant
        if (figura_na_potezu[1] + (smer * 2)) == validno_polje[1]:  # Ako pijun radi pomeraj za dva polja unapred
            # Popisujemo potencijalna polja gde ispitujemo za figuru
            potencijalni_potezi = [(validno_polje[0] + i, validno_polje[1]) for i in [-1, 1]]
            for enpassant in potencijalni_potezi:
                if unutar_table(enpassant):  # Ako su koordinate potencijalnog enpassant-a u okviru table
                    if sahovnica[enpassant].figura:  # Ako na polju postoji figura
                        if sahovnica[enpassant].figura.tip == "pijun":  # Ako je ta figura pijun
                            if sahovnica[enpassant].figura.tim != sahovnica[figura_na_potezu].figura.tim:  # Ako je suprotnog tima
                                sahovnica[figura_na_potezu].figura.enpassant = True  # Dodeljujemo enpassant pijunu na potezu
        elif (figura_na_potezu[1] + smer) == validno_polje[1]:  # Ako pijun radi pomeraj za jedno polje unapred
            if sahovnica[figura_na_potezu].figura.enpassant:  # I ako je njemu ranije dodeljen enpassant
                sahovnica[figura_na_potezu].figura.enpassant = False  # Ukidamo enpassant nad njime
            # Popisujemo potencijalna polja pored gde može biti pijun sa dodeljenim enpassant-om
            potencijalni_potezi = [(figura_na_potezu[0] + i, figura_na_potezu[1]) for i in range(-1, 2, 2)]
            for enpassant in potencijalni_potezi:
                if unutar_table(enpassant):  # Ako su koordinate potencijalnog enpassant-a u okviru table
                    if sahovnica[enpassant].figura:  # Ako na polju ima figura
                        if sahovnica[enpassant].figura.tip == "pijun":  # Ako je ta figura pijun
                            if sahovnica[enpassant].figura.enpassant:  # Ako je toj figuri dodeljen enpassant
                                sahovnica[enpassant].figura.enpassant = False  # Ukidamo enpassant nad njime

        # Proveravamo da li pijun radi enpassant
        vpx = validno_polje[0]
        vpy = validno_polje[1]
        if sahovnica[(vpx, vpy - smer)].figura:  # Proveravamo da li se na polju iza poteza nalazi figura
            if sahovnica[(vpx, vpy - smer)].figura.tip == "pijun":  # Da li je ta figura pijun
                if sahovnica[(vpx, vpy - smer)].figura.enpassant:  # Da li ima uslov za enpassant
                    sahovnica[(vpx, vpy - smer)].figura = None  # Praznimo polje na kojem se nalazi figura

    # Pomeramo figuru sa trenutnog polja na izabrano polje
    sahovnica[validno_polje].figura = sahovnica[figura_na_potezu].figura
    # Praznimo polje na kojem se više ne nalazi figura
    sahovnica[figura_na_potezu].figura = None


def pomeri_rokadu(figura_na_potezu, figura_za_rokadu, sahovnica):
    """
    Funkcija za izvršavanje rokade između kralja i topa.
    :param figura_na_potezu: Tuple: (x, y) koordinate figure koja pravi pomeraj.
    :param figura_za_rokadu: Tuple: (x, y) koordinate polja na koji će se pomeriti figura.
    :param sahovnica: Dict: Sadrži pozicije svih figura i stanja svih polja na celoj tabli.
    :return: None
    """
    # Ispitujem koja figura je kralj a koja je top
    if sahovnica[figura_na_potezu].figura.tip == "kralj":
        kralj = figura_na_potezu
        top = figura_za_rokadu
    else:
        top = figura_na_potezu
        kralj = figura_za_rokadu
    # Ispitujem da li je top levi ili desni
    y = figura_na_potezu[1]  # y koordinata je ista između topova i kralja istog tima
    if top[0] == 0:  # Ako je levi top
        sahovnica[(2, y)].figura = sahovnica[kralj].figura  # Pomera se kralj
        sahovnica[(2, y)].figura.pomeren = True  # Sprečavamo buduće rokade
        sahovnica[(3, y)].figura = sahovnica[top].figura  # Pomera se top
        sahovnica[(3, y)].figura.pomeren = True  # Sprečavamo buduće rokade
    elif top[0] == 7:
        sahovnica[(6, y)].figura = sahovnica[kralj].figura  # Pomera se kralj
        sahovnica[(6, y)].figura.pomeren = True  # Sprečavamo buduće rokade
        sahovnica[(5, y)].figura = sahovnica[top].figura  # Pomera se top
        sahovnica[(5, y)].figura.pomeren = True  # Sprečavamo buduće rokade
    sahovnica[kralj].figura = None  # Uklanja se top sa prethodne lokacije
    sahovnica[top].figura = None  # Uklanja se top sa prethodne lokacije
