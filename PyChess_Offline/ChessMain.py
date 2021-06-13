"""
Main driver file. Responsible for handling user input and displaying the board.
"""
import pygame
import ChessEngine as ce

HEIGHT = WIDTH = 512  # size of the board
ROWS = COLS = 8  # number of total rows and columns
SQ_SIZE = HEIGHT // ROWS  # size of 1 square
SQ_COLOR = (200, 200, 200)
MAX_FPS = 15  # Animation speed
IMAGES = {}

pygame.init()


"""
Initialize image database
"""


def load_images():
    color = ["w", "b"]
    pieces = ["r", "h", "b", "k", "q", "p"]
    for c in color:
        for p in pieces:
            temp_image = pygame.image.load("images/" + c + p + ".png")
            IMAGES[c+p] = pygame.transform.scale(temp_image, (SQ_SIZE, SQ_SIZE))


"""
Main driver file. We handle user input and graphics.
"""


def main():
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    gs = ce.GameState()
    load_images()  # only do this once before the while loop because it uses a lot of resources

    sq_selected = ()
    player_clicks = []

    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sq_selected == (row, col):
                    sq_selected = ()
                    player_clicks = []
                else:
                    sq_selected = (row, col)
                    player_clicks.append(sq_selected)

        clock.tick(MAX_FPS)
        draw_game_state(win, gs)
        pygame.display.update()


"""
draws the squares on the board
draws pieces on the squares
"""


def draw_game_state(win, gs):
    win.fill("white")
    draw_board(win)
    draw_pieces(win, gs.board)
    pass


def draw_board(win):
    colors = [(255, 255, 255), (200, 200, 200)]
    for row in range(ROWS):
        for col in range(COLS):
            """if not row % 2:
                if col % 2:
                    pygame.draw.rect(win, SQ_COLOR, (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

            if row % 2:
                if not col % 2:
                    pygame.draw.rect(win, SQ_COLOR, (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))"""

            color = colors[(row + col) % 2]
            pygame.draw.rect(win, color, (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def draw_pieces(win, board):
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece != "--":
                win.blit(IMAGES[piece], (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()
