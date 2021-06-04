from move import *


def file(file, direction):
    files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    file_index = files.index(file)
    result = None
    if direction == 'right':
        if not file == 'h':
            result = files[file_index + 1]
        else:
            result = 'out'
    if direction == 'left':
        if not file == 'a':
            result = files[file_index + -1]
        else:
            result = 'out'
    return result


opposite = {
    'black': 'white',
    'white': 'black'
}


def list_moves(board):
    available_moves = []
    for file in board.data:
        for piece in board.data[file]:
            if piece.color == board.turn:
                if piece.shape == 'pawn':
                    available_moves.extend(
                        pawn_detect(piece, board)
                    )
    a = []
    for move in available_moves:
        a.append(move.label)
    # print(a)
    return available_moves


def pawn_detect(piece, board):
    moves = []
    direction = 0

    # standard moving
    if piece.color == 'white':
        direction = 1
    if piece.color == 'black':
        direction = -1
    if board.data[piece.file][piece.rank + direction].color == 'empty':
        moves.append(Move(piece, piece.rank + direction, piece.file))

    # for first move
    if piece.color == 'white' and piece.rank == 2 and board.data[piece.file][piece.rank + (
            2 * direction)].color == 'empty':
        moves.append(Move(piece, piece.rank + (2 * direction), piece.file))
    if piece.color == 'black' and piece.rank == 7 and board.data[piece.file][piece.rank + (
            2 * direction)].color == 'empty':
        moves.append(Move(piece, piece.rank + (2 * direction), piece.file))

    # for taking
    if file(piece.file, 'right') != 'out':
        if board.data[file(piece.file, 'right')][piece.rank + direction].color == opposite[piece.color]:
            moves.append(Move(piece, piece.rank + direction, file(piece.file, 'right'), take=True))
    if file(piece.file, 'left') != 'out':
        if board.data[file(piece.file, 'left')][piece.rank + direction].color == opposite[piece.color]:
            moves.append(Move(piece, piece.rank + direction, file(piece.file, 'left'), take=True))

    return moves


def rook_detect(piece, board):
    moves = []


def legal_detect(move, piece, board):
    if piece.color != board.turn:
        return False



#def takes_detect(move, board):

#def check_detect(board):


#THings to check for:
#right color
#a square the piece can go to
#does not put yourself in check
#is a take? If so, not taking same color piece
#is within the board