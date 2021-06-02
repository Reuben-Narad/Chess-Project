shape_names = {
    'rook': 'R',
    'knight': 'N',
    'bishop': 'B',
    'king': 'K',
    'queen': 'Q',
    'pawn': 'p',
    None: ''
}
color_names = {
    'black': 'b',
    'white': 'w',
    'empty': ''
}


class Piece:
    def __init__(self, file, rank, color='empty', shape=None):
        self.color = color
        self.shape = shape
        self.rank = rank
        self.file = file
        self.label = color_names[color] + shape_names[shape]
