import chess
import sys # to read stdin

board = chess.Board()
print(board.legal_moves)
print(board)

first_move = True # true if we're making our first move
player_type = sys.argv[1]
player_color = False

if player_type == "white":
    player_color = True
    #print("true")
elif player_type == "black":
    player_color = False
    #print("false")

# while game not over
while not (board.is_stalemate() or board.is_checkmate()):
    # our opponent made a move
    if not (first_move and player_type == "white"):
        print("opponent player moving")
        opponent_move = input()
        board.push_san(opponent_move)
        print(board)
        print(board.legal_moves)

    # we make a move
    print("us moving")
    def print_to_stdout(*a):
        print(*a, file=sys.stdout)

    # define mymove for simplicity in making moves
    mymove = str(list(board.legal_moves)[0])

    # output the move
    print_to_stdout(mymove)

    # make the move on the board
    board.push_san(mymove)
    print(board)

    first_move = False