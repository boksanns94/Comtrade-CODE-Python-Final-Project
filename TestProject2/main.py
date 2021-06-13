import pygame
from bin import constants as c
from bin import gameclient as gc

win = gc.init_win()
clock = pygame.time.Clock()


def main():
    run = True

    while run:
        clock.tick(c.FPS)  # Limit the FPS of the game to a specified value

        for event in pygame.event.get():  # If the window is closed the game will exit
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass


main()
