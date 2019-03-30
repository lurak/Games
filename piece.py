class Piece:
    """
    Class for representation chess figures.
    """
    def __init__(self, color):
        self.color = color


class King(Piece):
    """
    Class for representation of chess figure - King.
    """
    def __init__(self, color, shape):
        super().__init__(color)
        self.shape = shape

    def move(self):
        pass


class Queen(Piece):
    """
    Class for representation of chess figure - Queen.
    """
    def __init__(self, color, shape):
        super().__init__(color)
        self.shape = shape

    def move(self):
        pass


class Pawn(Piece):
    """
    Class for representation of chess figure - Pawn.
    """
    def __init__(self, color, shape):
        super().__init__(color)
        self.shape = shape

    def move(self):
        pass


class Knight(Piece):
    """
    Class for representation of chess figure - Knight.
    """
    def __init__(self, color, shape):
        super().__init__(color)
        self.shape = shape

    def move(self):
        pass


class Bishop(Piece):
    """
    Class for representation of chess figure - Bishop.
    """
    def __init__(self, color, shape):
        super().__init__(color)
        self.shape = shape

    def move(self):
        pass


class Rook(Piece):
    """
    Class for representation of chess figure - Rook.
    """
    def __init__(self, color, shape):
        super().__init__(color)
        self.shape = shape

    def move(self):
        pass
