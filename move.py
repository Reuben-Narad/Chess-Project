class Move:
    def __init__(self, piece, end_rank, end_file, take=False, check=False, checkmate=False, xK=False, illegal=False):
        self.start_rank = piece.rank
        self.start_file = piece.file
        self.end_rank = end_rank
        self.end_file = end_file
        self.promotes = False
        self.xK = xK
        self.illegal = illegal
        self.piece = piece
        self.take = take
        self.check = check
        self.checkmate = checkmate
        self.take = take
        self.label = self.create_label()

    def create_label(self):
        if self.xK:
            take = True
        if self.piece.shape == 'pawn':
            if self.end_rank == 8 or self.end_rank == 1:
                self.promotes = True
        if self.promotes:
            promo = '=Q'
        else:
            promo = ''
        if self.take:
            ex = 'x'
        if self.piece.shape == 'pawn' and self.take:
            ex = self.start_file + 'x'
        else:
            ex = ''
        if self.check:
            plus = '+'
        else:
            plus = ''
        if self.checkmate:
            pound = '#'
        else:
            pound = ''
        if self.xK:
            gg = '!!Takes King!!'
        else:
            gg = ''
        label = \
            self.piece.letter + ex + self.end_file + str(self.end_rank) + promo + plus + pound + gg
        return label

    def update_label(self):
        self.label = self.create_label()
