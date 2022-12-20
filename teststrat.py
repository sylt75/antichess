## working file - use strategy.py for correct version

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
        print("opponent player moving")
        print(board.legal_moves)
        opponent_move = input()
        board.push_san(opponent_move)
        print(board)
        print(board.legal_moves)

    # we make a move
    print("us moving")
    def print_to_stdout(*a):
        print(*a, file=sys.stdout)

    # antichess move generator
    antichess_legal = []
    for x in list(board.legal_moves):
        if board.is_capture(x) == True:
            antichess_legal.append(x)
    print(antichess_legal)
    

    # strategy

    # case where capture moves are available
    if len(antichess_legal) != 0:

        # maximize value of opponent piece to capture

        maxvalue = 0
        mymove_win = "None"
        for x in (antichess_legal):
            # checks if the move puts king in check
            if board.gives_check(x) == True:
                mymove_win = str(x)
                break
            # determine the square the move lands on
            x = str(x)
            landing_pos = x[2:4]
            # determine piece being captured at that square
            bsquare = chess.parse_square(landing_pos)
            capvalue = board.piece_type_at(bsquare)
            if capvalue == None:
                capvalue = 1
            # picks the move that captures most valuable piece
            if capvalue >= maxvalue:
                maxvalue = capvalue
                mymove_max = x
                print(mymove)
        
        # minimize value of piece capturable by opponent

        board1 = chess.Board()
        minvalue = 6
        answer = "minimize"
        for i in antichess_legal:
            board2 = board1.push_san(str(i))
            opp_antilegal = []
            # define list of opponent moves
            for x in list(board2.legal_moves):
                if board2.is_capture(x) == True:
                    opp_antilegal.append(x)
            if len(opp_antilegal) == 0:
                opp_antilegal = list(board2.legal_moves)
            for y in opp_antilegal:
                # removes our moves that result in immediate loss
                if board2.gives_check(y) == True and len(antichess_legal) > 1:
                    antichess_legal.remove(i)
                if board2.gives_check(y) == True and len(antichess_legal) <= 1:
                    answer = "maximize"
                # determine the square the move lands on
                y = str(y)
                landing_pos_opp = y[2:4]
                # determine piece being captured at that square
                bsquare_opp = chess.parse_square(landing_pos_opp)
                capvalue_opp = board2.piece_type_at(bsquare_opp)
                if capvalue_opp == None:
                    capvalue_opp = 1
                # picks the move that minimizes value of piece capturable by opponent
                if capvalue_opp <= minvalue:
                    minvalue = capvalue_opp
                    mymove_min = y
        
        # choose which move to play

        if answer == "maximize":
            mymove = mymove_max
        if mymove_win != "None":
            mymove = mymove_win
        else:
            mymove = mymove_min

    
    # case where no capture moves are available
    if len(antichess_legal) == 0:
        
        # maximize value of opponent piece to capture

        mymove_win = "None"
        for y in (list(board.legal_moves)):
        # checks if the move puts king in check
            if board.gives_check(y) == True:
                mymove_win = str(y)
                break
        
        # minimize value of piece capturable by opponent

        board1 = chess.Board()
        minvalue = 6
        for i in list(board1.legal_moves):
            board2 = board1.push_san(str(i))
            opp_antilegal = []
            # define list of opponent moves
            for x in list(board2.legal_moves):
                if board2.is_capture(x) == True:
                    opp_antilegal.append(x)
            if len(opp_antilegal) == 0:
                opp_antilegal = list(board2.legal_moves)
            for y in opp_antilegal:
                # removes our moves that result in immediate loss
                if board2.gives_check(y) == True and len(list(board1.legal_moves)) > 1:
                    list(board1.legal_moves).remove(i)
                # determine the square the move lands on
                y = str(y)
                landing_pos_opp = y[2:4]
                # determine piece being captured at that square
                bsquare_opp = chess.parse_square(landing_pos_opp)
                capvalue_opp = board2.piece_type_at(bsquare_opp)
                if capvalue_opp == None:
                    capvalue_opp = 1
                # picks the move that minimizes value of piece capturable by opponent
                if capvalue_opp <= minvalue:
                    minvalue = capvalue_opp
                    mymove_min = y

        # choose which move to play
        if mymove_win != "None":
            mymove = mymove_win
        else:
            mymove = mymove_min


    # output the move
    print_to_stdout(mymove)

    # make the move on the board
    board.push_san(mymove)
    print(board)

    first_move = False
