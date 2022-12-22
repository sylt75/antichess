import chess
import sys

board = chess.Board()

first_move = True # true since we're making our first move
player_type = sys.argv[1]
player_color = False

if player_type == "white":
    player_color = True
elif player_type == "black":
    player_color = False

# while game not over
while not (board.is_stalemate() or board.is_checkmate()):

    # our opponent made a move
    if not (first_move and player_type == "white"):
        opponent_move = input()
        board.push_san(opponent_move)

    # we make a move
    def print_to_stdout(*a):
        print(*a, file=sys.stdout)

    # antichess move generator
    antichess_legal = []
    for x in list(board.legal_moves):
        if board.is_capture(x) == True:
            antichess_legal.append(x)
    
    # strategy
    if len(antichess_legal) != 0:
        maxvalue = 0
        for x in (antichess_legal):
        ## checks if the move puts king in check
            if board.gives_check(x) == True:
                mymove = str(x)
                break
        ## determine the square the move lands on
            x = str(x)
            landing_pos = x[2:4]
        ## determine piece being captured at that square (piece_type_at)
            bsquare = chess.parse_square(landing_pos)
            capvalue = board.piece_type_at(bsquare)
            if capvalue == None:
                capvalue = 1
        ## if piece type value is higher than maxvalue
            if capvalue > maxvalue:
                maxvalue = capvalue
                mymove = x
    
    if len(antichess_legal) == 0:
        mymove = str(list(board.legal_moves)[0])
        for y in (list(board.legal_moves)):
        ## checks if the move puts king in check
            if board.gives_check(y) == True:
                mymove = str(y)

    # make the move on the board
    board.push_san(mymove)

    # output the move
    print_to_stdout(mymove)

    first_move = False
