import sys
import pygame
import tabla
import figure


WIN = pygame.display.set_mode((tabla.SIRINA_TABLE, tabla.SIRINA_TABLE))  # Inicijalizuje se prozor
pygame.display.set_caption("Py-Šah")  # Postavlja se naslov na vrhu prozora
CLOCK = pygame.time.Clock()
FPS = 10


def main():

    sahovnica = {}
    tabla.napravi_tablu(sahovnica)
    igra = True

    while igra:
        CLOCK.tick(FPS)

        for event in pygame.event.get():  # Ako se desi da korisnik klikne na crveni X da izadje iz igre
            if event.type == pygame.QUIT:  # pojaviće se pygame.QUIT event. Tada zatvaramo celu igru.
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pozicija_misa = pygame.mouse.get_pos()
                polje = tabla.nadji_polje(pozicija_misa)
                tabla.deselektuj_sve(sahovnica)
                figure.iscrtaj_potez(polje, sahovnica)

        tabla.azuriraj_sliku(sahovnica, WIN)


main()
