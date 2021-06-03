from pieces import *
from move import *
from board import *

def check_legal(move, piece, board):
    if piece.color != board.turn:
        return False


#THings to check for:
#right color
#a square the piece can go to
#does not put yourself in check
#is a take? If so, not taking same color piece
#is within the board