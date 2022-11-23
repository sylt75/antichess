import chess
import sys

board = chess.Board()

legalmoves = board.legal_moves
 
def print_to_stdout(*a):
 
    print(*a, file=sys.stdout)

print_to_stdout(list(legalmoves)[0])