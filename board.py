import pandas as pd
from pieces import *
from move import *
from detection import *
import numpy as np
from copy import deepcopy
import random

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
        self.last_board = None
        self.next_board = None

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

    def empty_board(self):
        for j in range(1, 9):
            for k in range(8):
                self.place_piece(self.colnames[k], j)

    def execute_move(self, move):
        self.last_board = deepcopy(self)
        piece = self.data[move.start_file][move.start_rank]
        self.data[move.end_file][move.end_rank] = piece
        if move.promotes:
            piece.promote()
        piece.rank = move.end_rank
        piece.file = move.end_file
        self.data[move.start_file][move.start_rank] = Piece(move.start_file, move.start_rank)
        print(move.label)
        self.turn = opposite[self.turn]

    def go_back(self):
        # reverts last move
        if self.last_board is not None:
            self.next_board = deepcopy(self)
            self.data = self.last_board.data
            self.turn = self.last_board.turn
            self.last_board = self.last_board.last_board
        else:
            print("fuck off its move 1")

    def summarise(self):
        display = pd.DataFrame(data={
            'a': [None] * 8,
            'b': [None] * 8,
            'c': [None] * 8,
            'd': [None] * 8,
            'e': [None] * 8,
            'f': [None] * 8,
            'g': [None] * 8,
            'h': [None] * 8
        })
        display.index += 1
        for n in display:
            for m in range(1, 9):
                display[n][m] = self.data[n][m].label
        print(display)



test_board = Board(data1, 'black')
test_board.set_board()
test_board.turn = 'white'
test_board.place_piece('e', 4, 'white', 'rook')
#test_board.place_piece('e', 5, 'black', 'pawn')
test_board.summarise()
list_moves(test_board, display=True)

