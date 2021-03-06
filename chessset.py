class ChessSet:
    """
    Class for chess representation, it takes board and list of pieces.
    """
    def __init__(self, pieces, board):
        self.pieces = pieces
        self.board = board

    def for_3(self):
        """
        Put pieces on board for 3.
        """
        pos = self.board.board_position()
        for i in range(len(self.pieces)):
            if self.pieces[i][0].color == "white":
                for u in range(8):
                    pos[1][u] = 'P(W)'
                pos[0][0] = 'R(W)'
                pos[0][7] = 'R(W)'
                pos[0][1] = 'N(W)'
                pos[0][6] = 'N(W)'
                pos[0][2] = 'B(W)'
                pos[0][5] = 'B(W)'
                pos[0][3] = 'Q(W)'
                pos[0][4] = 'K(W)'
            elif self.pieces[i][0].color == "black":
                for q in range(4,12):
                    pos[6][q] = 'P(B)'
                pos[7][4] = 'Q(B)'
                pos[7][5] = 'B(B)'
                pos[7][6] = 'N(B)'
                pos[7][7] = 'R(B)'
                pos[7][8] = 'K(B)'
                pos[7][9] = 'B(B)'
                pos[7][10] = 'N(B)'
                pos[7][11] = 'R(B)'
            elif self.pieces[i][0].color == "yellow":
                for j in range(4):
                    pos[10][j] = 'P(Y)'
                for w in range(8, 12):
                     pos[10][w] = 'P(Y)'
                pos[11][0] = 'R(Y)'
                pos[11][1] = 'N(Y)'
                pos[11][2] = 'B(Y)'
                pos[11][3] = 'Q(Y)'
                pos[11][8] = 'K(Y)'
                pos[11][9] = 'B(Y)'
                pos[11][10] = 'M(Y)'
                pos[11][11] = 'R(Y)'
        return pos

    def board_double(self):
        """
        Put pieces on board for double chess.
        """
        pos = self.board.board_position()
        for i in range(len(self.pieces)):
            if self.pieces[i][0].color == "white":
                for i in range(16):
                    pos[1][i] = 'P(W)'
                pos[0][0] = 'R(W)'
                pos[0][7] = 'R(W)'
                pos[0][1] = 'N(W)'
                pos[0][6] = 'N(W)'
                pos[0][2] = 'B(W)'
                pos[0][5] = 'B(W)'
                pos[0][3] = 'Q(W)'
                pos[0][4] = 'K(W)'
                pos[0][8] = 'R(W)'
                pos[0][9] = 'N(W)'
                pos[0][10] = 'B(W)'
                pos[0][11] = 'Q(W)'
                pos[0][12] = 'K(W)'
                pos[0][13] = 'B(W)'
                pos[0][14] = 'N(W)'
                pos[0][15] = 'R(W)'
            elif self.pieces[i][0].color == "black":
                for j in range(16):
                    pos[10][j] = 'P(B)'
                pos[11][0] = 'R(B)'
                pos[11][7] = 'R(B)'
                pos[11][1] = 'N(B)'
                pos[11][6] = 'N(B)'
                pos[11][2] = 'B(B)'
                pos[11][5] = 'B(B)'
                pos[11][3] = 'Q(B)'
                pos[11][4] = 'K(B)'
                pos[11][8] = 'R(B)'
                pos[11][9] = 'N(B)'
                pos[11][10] = 'B(B)'
                pos[11][11] = 'Q(B)'
                pos[11][12] = 'K(B)'
                pos[11][13] = 'B(B)'
                pos[11][14] = 'N(B)'
                pos[11][15] = 'R(B)'
        return pos

    def board_Glynskyy(self):
        """
        Put pieces on board for Glynskyy chess.
        """
        pos = self.board.board_position()
        for i in range(len(self.pieces)):
            if self.pieces[i][0].color == "white":
                pos[0][1] = 'P(W)'
                pos[0][2] = 'R(W)'
                pos[0][3] = 'N(W)'
                pos[0][4] = 'K(W)'
                pos[0][5] = 'B(W)'
                pos[0][6] = 'Q(W)'
                pos[0][7] = 'N(W)'
                pos[0][8] = 'R(W)'
                pos[0][9] = 'P(W)'
                pos[1][2] = 'P(W)'
                pos[1][5] = 'B(W)'
                pos[1][8] = 'P(W)'
                pos[2][3] = 'P(W)'
                pos[2][5] = 'B(W)'
                pos[2][7] = 'P(W)'
                pos[3][4] = 'P(W)'
                pos[3][6] = 'P(W)'
                pos[4][5] = 'P(W)'
            elif self.pieces[i][0].color == "black":
                for i in range(1, 10):
                    pos[6][i] = 'P(B)'
                pos[7][2] = 'R(B)'
                pos[7][8] = 'R(B)'
                pos[8][3] = 'N(B)'
                pos[8][5] = 'B(B)'
                pos[8][7] = 'N(B)'
                pos[9][4] = 'K(B)'
                pos[9][5] = 'B(B)'
                pos[9][6] = 'Q(B)'
                pos[10][5] = 'B(B)'
        return pos

    def board_for_4(self):
        """
        Put pieces on board for 4.
        """
        pos = self.board.board_position()
        for i in range(len(self.pieces)):
            if self.pieces[i][0].color == "white":
                for i in range(3,11):
                    pos[1][i] = "P(W)"
                pos[0][3] = "R(W)"
                pos[0][4] = "N(W)"
                pos[0][5] = "B(W)"
                pos[0][6] = "Q(W)"
                pos[0][7] = "K(W)"
                pos[0][8] = "B(W)"
                pos[0][9] = "N(W)"
                pos[0][10] = "R(W)"
            elif self.pieces[i][0].color == 'black':
                for u in range(3,11):
                    pos[u][1] = "P(B)"
                pos[3][0] = "R(B)"
                pos[4][0] = "N(B)"
                pos[5][0] = "B(B)"
                pos[6][0] = "K(B)"
                pos[7][0] = "Q(B)"
                pos[8][0] = "B(B)"
                pos[9][0] = "N(B)"
                pos[10][0] = "R(B)"
            elif self.pieces[i][0].color == 'green':
                for q in range(3,11):
                    pos[q][12] = "P(G)"
                pos[3][13] = "R(G)"
                pos[4][13] = "N(G)"
                pos[5][13] = "B(G)"
                pos[6][13] = "K(G)"
                pos[7][13] = "Q(G)"
                pos[8][13] = "B(G)"
                pos[9][13] = "N(G)"
                pos[10][13] = "R(G)"
            elif self.pieces[i][0].color == 'yellow':
                for j in range(3, 11):
                    pos[12][j] = "P(Y)"
                pos[13][3] = "R(Y)"
                pos[13][4] = "N(Y)"
                pos[13][5] = "B(Y)"
                pos[13][6] = "Q(Y)"
                pos[13][7] = "K(Y)"
                pos[13][8] = "B(Y)"
                pos[13][9] = "N(Y)"
                pos[13][10] = "R(Y)"
        return pos


class Board:
    """
    Class for board generation.
    """
    def __init__(self, type_board):
        self.type_board = type_board

    def board_position(self):
        """
        Function which depend on type of board.
        """
        if self.type_board == "for_3":
            return [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        elif self.type_board == "double":
            return [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        elif self.type_board == "Glynskyy":
            return [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]

        elif self.type_board == "for_4":
            return [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
