import chess
import sys # to read stdout

board = chess.Board()
 
def print_to_stdout(*a):
 
    print(*a, file=sys.stdout)

# define mymove for simplicity in making moves
mymove = str(list(board.legal_moves)[0])

# output the move
print_to_stdout(mymove)

# make the move on the board
board.push_san(mymove)