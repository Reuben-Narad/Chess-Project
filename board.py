import pandas as pd
from pieces import *
from move import *
import numpy as np

#hello!

data1 = {
    'a': [None]*8,
    'b': [None]*8,
    'c': [None]*8,
    'd': [None]*8,
    'e': [None]*8,
    'f': [None]*8,
    'g': [None]*8,
    'h': [None]*8
        }


class Board:
    def __init__(self, data, turn):
        self.data = pd.DataFrame(data=data)
        self.colnames = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.piece_order = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
        self.turn = turn
        self.data.index = self.data.index + 1

    def place_piece(self, file, rank, color='empty', shape=None):
        self.data[file][rank] = Piece(file, rank, color, shape)

    def set_board(self):
        for i in range(8):
            self.place_piece(self.colnames[i], 1, 'white', self.piece_order[i])
            self.place_piece(self.colnames[i], 2, 'white', 'pawn')
            self.place_piece(self.colnames[i], 8, 'black', self.piece_order[i])
            self.place_piece(self.colnames[i], 7, 'black', 'pawn')
        for j in range(3, 7):
            for k in range(8):
                self.place_piece(self.colnames[k], j)
        self.turn = 'white'

    def execute_move(self, move):
        piece = self.data[move.start_file][move.start_rank]
        self.data[move.end_file][move.end_rank] = piece
        self.data[move.start_file][move.start_rank] = Piece(move.start_file, move.start_rank)
        print('moves ' + piece.label + ' to ' + move.end_file + str(move.end_rank))

    def summarise(self):
        display = self.data.copy()
        for n in display:
            for m in range(1, 9):
                display[n][m] = display[n][m].label
        print(display)


test_board = Board(data1, 'white')
test_board.set_board()
test_board.summarise()

test_move = Move(2, 'e', 4, 'e')
test_board.execute_move(test_move)
test_board.summarise()