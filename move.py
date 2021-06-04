class Move:
    def __init__(self, piece, end_rank, end_file, take=False, check=False, checkmate=False, xK=False):
        self.start_rank = piece.rank
        self.start_file = piece.file
        self.end_rank = end_rank
        self.end_file = end_file
        self.promotes = False
        if piece.shape == 'pawn':
            if end_rank == 8 or end_rank == 1:
                self.promotes = True
        if self.promotes:
            promo = '=Q'
        else:
            promo = ''
        if take:
            if piece.shape == 'pawn':
                self.take = self.start_file + 'x'
            else:
                self.take = 'x'
        else:
            self.take = ''
        if check:
            self.check = '+'
        else:
            self.check = ''
        if checkmate:
            self.checkmate = '#'
        else:
            self.checkmate = ''
        self.label = piece.letter + self.take + self.end_file + str(self.end_rank) + promo + self.check + self.checkmate


