from move import *
from copy import deepcopy
from move_filters import *

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
    for side in ['left', 'right']:
        peek = look_at(piece, board, file(piece.file, side), piece.rank + direction)
        if peek == 'take':
            moves.append(Move(piece, piece.rank + direction, file(piece.file, side), take=True))
        if peek == 'xK':
            moves.append(Move(piece, piece.rank + direction, file(piece.file, side), xK=True))
    return moves


def rook_detect(piece, board):
    moves = []
    moves.extend(cardinals_detect(piece, board))
    return moves


def bishop_detect(piece, board):
    moves = []
    moves.extend(diagonals_detect(piece, board))
    return moves


def queen_detect(piece, board):
    moves = []
    moves.extend(cardinals_detect(piece, board))
    moves.extend(diagonals_detect(piece, board))
    return moves


def knight_detect(piece, board):
    moves = []
    for square in [(('right', 1), 2), (('right', 2), 1), (('right', 2), -1), (('right', 1), -2),
                   (('left', 1), -2), (('left', 2), -1), (('left', 2), 1), (('left', 1), 2)]:
        selected_file = file(piece.file, *square[0])
        selected_rank = piece.rank + square[1]
        if look_at(piece, board, selected_file, selected_rank) == 'empty':
            moves.append(Move(piece, selected_rank, selected_file))
        if look_at(piece, board, selected_file, selected_rank) == 'take':
            moves.append(Move(piece, selected_rank, selected_file, take=True))
        if look_at(piece, board, selected_file, selected_rank) == 'xK':
            moves.append(Move(piece, selected_rank, selected_file, xK=True))
    return moves


def king_detect(piece, board):
    moves = []
    for square in [('right', 1), ('right', 0), ('right', -1), ('center', -1),
                   ('left', -1), ('left', 0), ('left', 1), ('center', 1)]:
        selected_file = file(piece.file, square[0])
        selected_rank = piece.rank + square[1]
        if look_at(piece, board, selected_file, selected_rank) == 'empty':
            moves.append(Move(piece, selected_rank, selected_file))
        if look_at(piece, board, selected_file, selected_rank) == 'take':
            moves.append(Move(piece, selected_rank, selected_file, take=True))
        if look_at(piece, board, selected_file, selected_rank) == 'xK':
            moves.append(Move(piece, selected_rank, selected_file, xK=True))
    return(moves)


def cardinals_detect(piece, board):
    moves = []
    for direction in ['up', 'down', 'right', 'left']:
        if direction == 'up':
            selected_file = piece.file
            selected_rank = piece.rank
            running = True
            while running:
                selected_rank += 1
                peek = look_at(piece, board, selected_file, selected_rank)
                if peek == 'out':
                    running = False
                if peek == 'block':
                    running = False
                if peek == 'take':
                    moves.append(Move(piece, selected_rank, selected_file, take=True))
                    running = False
                if peek == 'empty':
                    moves.append(Move(piece, selected_rank, selected_file))
                if peek == 'xK':
                    moves.append(Move(piece, selected_rank, selected_file, xK=True))
        if direction == 'down':
            selected_file = piece.file
            selected_rank = piece.rank
            running = True
            while running:
                selected_rank -= 1
                peek = look_at(piece, board, selected_file, selected_rank)
                if peek == 'out':
                    running = False
                if peek == 'block':
                    running = False
                if peek == 'take':
                    moves.append(Move(piece, selected_rank, selected_file, take=True))
                    running = False
                if peek == 'empty':
                    moves.append(Move(piece, selected_rank, selected_file))
                if peek == 'xK':
                    moves.append(Move(piece, selected_rank, selected_file, xK=True))
        if direction == 'right':
            selected_file = piece.file
            selected_rank = piece.rank
            running = True
            while running:
                selected_file = file(selected_file, 'right')
                peek = look_at(piece, board, selected_file, selected_rank)
                if peek == 'out':
                    running = False
                if peek == 'block':
                    running = False
                if peek == 'take':
                    moves.append(Move(piece, selected_rank, selected_file, take=True))
                    running = False
                if peek == 'empty':
                    moves.append(Move(piece, selected_rank, selected_file))
                if peek == 'xK':
                    moves.append(Move(piece, selected_rank, selected_file, xK=True))
        if direction == 'left':
            selected_file = piece.file
            selected_rank = piece.rank
            running = True
            while running:
                selected_file = file(selected_file, 'left')
                peek = look_at(piece, board, selected_file, selected_rank)
                if peek == 'out':
                    running = False
                if peek == 'block':
                    running = False
                if peek == 'take':
                    moves.append(Move(piece, selected_rank, selected_file, take=True))
                    running = False
                if peek == 'empty':
                    moves.append(Move(piece, selected_rank, selected_file))
                if peek == 'xK':
                    moves.append(Move(piece, selected_rank, selected_file, xK=True))
    return moves


def diagonals_detect(piece, board):
    moves = []
    for direction in ['NW', 'NE', 'SW', 'SE']:
        if direction == 'NW':
            selected_file = piece.file
            selected_rank = piece.rank
            running = True
            while running:
                selected_rank += 1
                selected_file = file(selected_file, 'left')
                peek = look_at(piece, board, selected_file, selected_rank)
                if peek == 'out':
                    running = False
                if peek == 'block':
                    running = False
                if peek == 'take':
                    moves.append(Move(piece, selected_rank, selected_file, take=True))
                    running = False
                if peek == 'empty':
                    moves.append(Move(piece, selected_rank, selected_file))
                if peek == 'xK':
                    moves.append(Move(piece, selected_rank, selected_file, xK=True))
        if direction == 'NE':
            selected_file = piece.file
            selected_rank = piece.rank
            running = True
            while running:
                selected_rank += 1
                selected_file = file(selected_file, 'right')
                peek = look_at(piece, board, selected_file, selected_rank)
                if peek == 'out':
                    running = False
                if peek == 'block':
                    running = False
                if peek == 'take':
                    moves.append(Move(piece, selected_rank, selected_file, take=True))
                    running = False
                if peek == 'empty':
                    moves.append(Move(piece, selected_rank, selected_file))
                if peek == 'xK':
                    moves.append(Move(piece, selected_rank, selected_file, xK=True))
        if direction == 'SW':
            selected_file = piece.file
            selected_rank = piece.rank
            running = True
            while running:
                selected_rank -= 1
                selected_file = file(selected_file, 'left')
                peek = look_at(piece, board, selected_file, selected_rank)
                if peek == 'out':
                    running = False
                if peek == 'block':
                    running = False
                if peek == 'take':
                    moves.append(Move(piece, selected_rank, selected_file, take=True))
                    running = False
                if peek == 'empty':
                    moves.append(Move(piece, selected_rank, selected_file))
                if peek == 'xK':
                    moves.append(Move(piece, selected_rank, selected_file, xK=True))
        if direction == 'SE':
            selected_file = piece.file
            selected_rank = piece.rank
            running = True
            while running:
                selected_rank -= 1
                selected_file = file(selected_file, 'right')
                peek = look_at(piece, board, selected_file, selected_rank)
                if peek == 'out':
                    running = False
                if peek == 'block':
                    running = False
                if peek == 'take':
                    moves.append(Move(piece, selected_rank, selected_file, take=True))
                    running = False
                if peek == 'empty':
                    moves.append(Move(piece, selected_rank, selected_file))
                if peek == 'xK':
                    moves.append(Move(piece, selected_rank, selected_file, xK=True))
    return moves


def legal_detect(move, piece, board):
    if piece.color != board.turn:
        return False


opposite = {
    'black': 'white',
    'white': 'black'
}


# shifts file "skip" steps
def file(file, direction, skips=1):
    files = ['out', 'out', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'out', 'out']
    file_index = files.index(file)
    result = None
    if direction == 'right':
        if not file == 'h':
            result = files[file_index + skips]
        else:
            result = 'out'
    if direction == 'left':
        if not file == 'a':
            result = files[file_index - skips]
        else:
            result = 'out'
    if direction == 'center':
        result = file
    return result


# returns what's going on in target square
def look_at(piece, board, file, rank):
    if file == 'out':
        return 'out'
    if rank >= 9 or rank <= 0:
        return 'out'
    if board.data[file][rank].color == 'empty':
        return 'empty'
    if board.data[file][rank].color == opposite[piece.color]:
        if board.data[file][rank].shape == 'king':
            return 'xK'
        else:
            return 'take'
    if board.data[file][rank].color == piece.color:
        return 'block'


def list_moves(board, display=False, flipped=False, remove_illegal=True, checks=True):
    available_moves = []
    for file in board.data:
        for piece in board.data[file]:
            if (piece.color == board.turn and flipped==False) or\
                    (piece.color == opposite[board.turn] and flipped == True):
                if piece.shape == 'pawn':
                    available_moves.extend(
                        pawn_detect(piece, board)
                    )
                if piece.shape == 'rook':
                    available_moves.extend(
                        rook_detect(piece, board)
                    )
                if piece.shape == 'bishop':
                    available_moves.extend(
                        bishop_detect(piece, board)
                    )
                if piece.shape == 'queen':
                    available_moves.extend(
                        queen_detect(piece, board)
                    )
                if piece.shape == 'knight':
                    available_moves.extend(
                       knight_detect(piece, board)
                    )
                if piece.shape == 'king':
                    available_moves.extend(
                       king_detect(piece, board)
                    )
    if checks:
        apply_checks(available_moves, board)
    if remove_illegal:
        legal_moves = []
        for move in available_moves:
            if not check_detect(board.look_forward(move, turn=True)):
                legal_moves.append(move)
        available_moves = legal_moves
    if display:
        a = []
        for move in available_moves:
            a.append(move.label)
        print(a)
    return available_moves


def apply_checks(moves, board):
    for move in moves:
        forward = board.look_forward(move, turn=False)
        if check_detect(forward):
            move.check = True
            move.update_label()


def check_detect(board):
    moves = list_moves(board, flipped=False, remove_illegal=False, display=False, checks=False)
    check_present = False
    for move in moves:
        if move.xK:
            check_present = True
    return check_present


# THings to check for:
# does not put yourself in check
# is a take? If so, not taking same color piece
# is within the board