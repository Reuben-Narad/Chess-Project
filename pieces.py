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
        self.letter = ''
        if shape == 'rook':
            self.letter = 'R'
        if shape == 'knight':
            self.letter = 'N'
        if shape == 'bishop':
            self.letter = 'B'
        if shape == 'king':
            self.letter = 'K'
        if shape == 'queen':
            self.letter = 'Q'

    def promote(self, shape='queen'):
        self.shape = shape
        if shape == 'rook':
            self.letter = 'R'
        if shape == 'knight':
            self.letter = 'N'
        if shape == 'bishop':
            self.letter = 'B'
        if shape == 'king':
            self.letter = 'K'
        if shape == 'queen':
            self.letter = 'Q'
        else:
            self.letter = ''
        self.label = color_names[self.color] + shape_names[shape]
