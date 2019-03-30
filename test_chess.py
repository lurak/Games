from piece import Pawn, Bishop, King, Knight, Queen, Rook
from chessset import Board, ChessSet

pieces = [[Pawn('white', 'P'), Pawn('white', 'P'), Pawn('white', 'P'), Pawn('white', 'P'), Pawn('white', 'P'),
           Pawn('white', 'P'), Pawn('white', 'P'), Pawn('white', 'P'),  Pawn('white', 'P'), Bishop('white', 'B'),
           Bishop('white', 'B'), Queen('white', 'Q'), King('white', 'K'), Rook('white', 'R'), Rook('white', 'R'),
           King('white', 'N'), Knight('white', 'N')],
          [Pawn('black', 'P'), Pawn('black', 'P'), Pawn('black', 'P'), Pawn('black', 'P'), Pawn('black', 'P'),
           Pawn('black', 'P'), Pawn('black', 'P'), Pawn('black', 'P'),  Pawn('black', 'P'), Bishop('black', 'B'),
           Bishop('black', 'B'), Queen('black', 'Q'), King('black', 'K'), Rook('black', 'R'), Rook('black', 'R'),
           King('black', 'N'), Knight('black', 'N')]]
if __name__ == "__main__":
    board = Board("Glynskyy")
    chess = ChessSet(pieces, board)
    red = chess.board_Glynskyy()
    for i in range(len(red)):
        print(red[i])