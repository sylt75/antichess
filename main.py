import chess
import sys # to read stdin

board = chess.Board()
# temporary arg val, true if we play "white", false if we play "black"
player_colour = True
# true if we're white and we're currently making first move
first_move = False
print("here0")
print(board.legal_moves)

# while game not over (not stalemate or checkmate)
while not board.is_stalemate():
    # if we're not currently making first move, let opponent_move be the stdin
    # if we get unexpected stdin value, terminate game?
    # if we're white and it's first move, there's no stdin expected
    print("here1")
    if not first_move:
        print("here2")
        opponent_move = input()
        board.push(chess.Move.from_uci(opponent_move)) # make the opponent's move in our board
        print(board)
        print(board.legal_moves)
        print(opponent_move)
