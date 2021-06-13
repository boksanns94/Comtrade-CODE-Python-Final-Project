"""
Class that is responsible for storing all info and caring about the state of the game. Responsible for
legal moves, and interactions between pieces. Also keeping a game log.
"""


class GameState:
    def __init__(self):
        # board is 8x8 2d list, and each element of the list represents a piece
        # the first character represents the color: b or w (black or white)
        # the second character represents the type of the piece:
        # r - rook, h - knight(horse), b - bishop, k - king, q - queen, p - pawn
        self.board = [
            ["br", "bh", "bb", "bq", "bk", "bb", "bh", "br"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wr", "wh", "wb", "wq", "wk", "wb", "wh", "wr"]
        ]
        self.whiteToMove = False
        self.moveLog = []


class Move:
    def __init__(self, start_sq, end_sq, board):
        self.start_row = start_sq[0]
        self.start_col = start_sq[1]
        self.end_row = end_sq[0]
        self.end_col = end_sq[1]
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]
