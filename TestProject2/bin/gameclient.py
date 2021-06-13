import pygame
import bin.constants as c


def init_win():
    """
    Initialises window parameters.
    :return: WIN: Object with window parameters.
    """
    win = pygame.display.set_mode([c.WIDTH, c.HEIGHT])
    pygame.display.set_caption(c.CAPTION)
    return win


def redraw_window(win):
    """
    Redraws the window.
    :param win: Object containing window parameters
    :return: None
    """
    win.fill((255, 255, 255))
    pygame.display.update()
