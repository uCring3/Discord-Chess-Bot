import random
#Channel allowed to play
TheGoodChannel = 'chess'
Chan = 'chess'
#Play
isPlaying = False
Player1 = False
Player2 = False
Promote = False
Pl = False
Pn = False
Winner = False
#init board
Ochessboard = [ #chessboard
	['⬜','⬛','⬜','⬛','⬜','⬛','⬜','⬛','🇦'], #a
	['⬛','⬜','⬛','⬜','⬛','⬜','⬛','⬜','🇧'], #b
	['⬜','⬛','⬜','⬛','⬜','⬛','⬜','⬛','🇨'], #c
	['⬛','⬜','⬛','⬜','⬛','⬜','⬛','⬜','🇩'], #d
	['⬜','⬛','⬜','⬛','⬜','⬛','⬜','⬛','🇪'], #e
	['⬛','⬜','⬛','⬜','⬛','⬜','⬛','⬜','🇫'], #f
	['⬜','⬛','⬜','⬛','⬜','⬛','⬜','⬛','🇬'], #g
	['⬛','⬜','⬛','⬜','⬛','⬜','⬛','⬜','🇭'], #h
    ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','⬜']] #Turn
unmoved = [ #for castling
    [0,0],[0,4],[0,7],[7,0],[7,4],[7,7]]
#images-emojis
w_pawn = '<:WhitePawn:1089626492725624912>'
w_rook = '<:WhiteRook:1089633245076930750>'
w_knite = '<:WhiteKnite:1089633240790356078>'
w_bishop = '<:WhiteBishop:1089633236998705204>'
w_king = '<:WhiteKing:1089633239381061753>'
w_queen = '<:WhiteQueen:1089633242338050059>'
b_pawn = '<:BlackPawn:1089633555220537426>'
b_rook = '<:BlackRook:1089633559746191500>'
b_knite = '<:BlackKnite:1089633553651863572>'
b_bishop = '<:BlackBishop:1089633282989232180>'
b_king = '<:BlackKing:1089633550942355649>'
b_queen = '<:BlackQueen:1089633557724540988>'

def sentBy(user,channel):
    global User
    global Chan
    User = user
    Chan = channel

def PrintBoard(): #send actual board
    #globals
    global chessboard
    global Winner
    global isPlaying
    global Player1
    global Player2
    if Winner == False:
        string = " "
        for letter in chessboard:
            for square in letter:
                string = string + str(square) + " "
            string = string + "\n"
        return string
    
    else:
        string = " "
        for letter in chessboard:
            for square in letter:
                string = string + str(square) + " "
            string = string + "\n"
        isPlaying = False
        Player1 = False
        Player2 = False
        return string + "\n" + Winner + " Win"

def Promotion(l,n,type):
    #globals
    global chessboard
    global Promote
    global Pl
    global Pn
    if chessboard[l][n] == w_pawn:
        if type == "queen":
            chessboard[l][n] = w_queen
        elif type == "rook":
            chessboard[l][n] = w_rook
        elif type == "knite":
            chessboard[l][n] = w_knite
        elif type == "bishop":
            chessboard[l][n] = w_bishop
    elif chessboard[l][n] == b_pawn:
        if type == "queen":
            chessboard[l][n] = b_queen
        elif type == "rook":
            chessboard[l][n] = b_rook
        elif type == "knite":
            chessboard[l][n] = b_knite
        elif type == "bishop":
            chessboard[l][n] = b_bishop
    Promote = False
    Pl = False
    Pn = False

def MovePiece(L1,N1,L2,N2): #move the piece
    #globals
    global chessboard
    global Ochessboard
    global Winner
    global Promote
    global Pl
    global Pn
    #Win
    if chessboard[L2][N2] == b_king:
        Winner = "White"
    elif chessboard[L2][N2] == w_king:
        Winner = "Black"
    #where it goes
    chessboard[L2][N2] = chessboard[L1][N1]
    #where it was
    chessboard[L1][N1] = Ochessboard[L1][N1]
    #change turn
    if chessboard[8][8] == '⬜':
        chessboard[8][8] = '⬛'
    elif chessboard[8][8] == '⬛':
        chessboard[8][8] = '⬜'
    #promotion
    if (chessboard[L2][N2] == w_pawn and L2 == 0) or (chessboard[L2][N2] == b_pawn and L2 == 7):
        Promote = True
        Pl = L2
        Pn = N2

def handle_response(message) -> str:
    #globals
    global TheGoodChannel
    global Chan
    global isPlaying
    global Player1
    global Player2
    global Promote
    global Pl
    global Pn
    global chessboard
    global w_pawn
    global w_rook
    global w_knite
    global w_bishop
    global w_king
    global w_queen
    global b_pawn
    global b_rook
    global b_knite
    global b_bishop
    global b_king
    global b_queen
    global unmoved
    #message
    p_message = message.lower()
    #only on the selected channel
    if Chan == TheGoodChannel:
        if p_message == 'help':
            return '''
            "play" to be a player
            "start" to start the game (it needs 2 players)
            "a1-b2" to move a piece from a1 to b2
            ex: "w_pawn :moyai "(space at the end of the message before sending) to change the White Pawn with the moyai emoji (it works with every discord emoji)
            "board" to generate the chess board
            start a command with "?" to send it in private
            "chess_channel" to set the channel to play chess
            "surrender" to surrender'''

        if p_message == 'play' and not isPlaying: #set the pieces
            if not Player1:
                Player1 = User
                return "White: " + Player1
            elif not Player2 and (User != Player1 or User == '265490503745667072'):
                Player2 = User
                return "Black: " + Player2 + "\n digit "+'''"start"'''+" to start"

        if p_message == 'start':
            if Player1 != False and Player2 != False and not isPlaying: #set the pieces
                isPlaying = True
                chessboard = [#chessboard
                    [b_rook,b_knite,b_bishop,b_queen,b_king,b_bishop,b_knite,b_rook,'🇦'], #a
                    [b_pawn,b_pawn,b_pawn,b_pawn,b_pawn,b_pawn,b_pawn,b_pawn,'🇧'], #b
                    ['⬜','⬛','⬜','⬛','⬜','⬛','⬜','⬛','🇨'], #c
                    ['⬛','⬜','⬛','⬜','⬛','⬜','⬛','⬜','🇩'], #d
                    ['⬜','⬛','⬜','⬛','⬜','⬛','⬜','⬛','🇪'], #e
                    ['⬛','⬜','⬛','⬜','⬛','⬜','⬛','⬜','🇫'], #f
                    [w_pawn,w_pawn,w_pawn,w_pawn,w_pawn,w_pawn,w_pawn,w_pawn,'🇬'], #g
                    [w_rook,w_knite,w_bishop,w_queen,w_king,w_bishop,w_knite,w_rook,'🇭'], #h
                    ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','⬜']] #Turn
                
                return PrintBoard() #send Actual Board
            else:
                return "need more layers or a game is already on"

        if p_message[2] == '-' and isPlaying and not Promote: #set movement
            #first letter
            L1 = 8
            if p_message[0] == 'a':
                L1 = 0
            elif p_message[0] == 'b':
                L1 = 1
            elif p_message[0] == 'c':
                L1 = 2
            elif p_message[0] == 'd':
                L1 = 3
            elif p_message[0] == 'e':
                L1 = 4
            elif p_message[0] == 'f':
                L1 = 5
            elif p_message[0] == 'g':
                L1 = 6
            elif p_message[0] == 'h':
                L1 = 7
            else:
                return "move a piece in a letter between A and H"
            #first number
            N1 = 8
            N1 = int(p_message[1]) -1
            #second letter
            L2 = 8
            if p_message[3] == 'a':
                L2 = 0
            elif p_message[3] == 'b':
                L2 = 1
            elif p_message[3] == 'c':
                L2 = 2
            elif p_message[3] == 'd':
                L2 = 3
            elif p_message[3] == 'e':
                L2 = 4
            elif p_message[3] == 'f':
                L2 = 5
            elif p_message[3] == 'g':
                L2 = 6
            elif p_message[3] == 'h':
                L2 = 7
            else:
                return "move a piece in a letter between A and H"
            #second number
            N2 = int(p_message[4]) -1
            #rules for moving
            if chessboard[8][8] == '⬜' and User == Player1: #White turn
                if chessboard[L1][N1] == w_pawn:
                    if L1 == 6: #2 space
                        #move
                        if ((L2 == L1-1 and N2 == N1) or (L2 == L1-2 and N2 == N1)) and (chessboard[L2][N2] == '⬜' or chessboard[L2][N2] == '⬛'):
                            MovePiece(L1,N1,L2,N2)
                        #kill
                        elif ((L2 == L1-1 and N2 == N1+1) or (L2 == L1-1 and N2 == N1-1)) and (chessboard[L2][N2] == b_pawn or chessboard[L2][N2] == b_rook or chessboard[L2][N2] == b_knite or chessboard[L2][N2] == b_bishop or chessboard[L2][N2] == b_king or chessboard[L2][N2] == b_queen):
                            MovePiece(L1,N1,L2,N2)
                    else:
                        #move
                        if (L2 == L1-1 and N2 == N1) and (chessboard[L2][N2] == '⬜' or chessboard[L2][N2] == '⬛'):
                            MovePiece(L1,N1,L2,N2)
                        #kill
                        elif ((L2 == L1-1 and N2 == N1+1) or (L2 == L1-1 and N2 == N1-1)) and (chessboard[L2][N2] == b_pawn or chessboard[L2][N2] == b_rook or chessboard[L2][N2] == b_knite or chessboard[L2][N2] == b_bishop or chessboard[L2][N2] == b_king or chessboard[L2][N2] == b_queen):
                            MovePiece(L1,N1,L2,N2)

                    if Promote:
                        return "chose:\n[queen]-Queen\n[rook]-Rook\n[knite]-Knite\n[bishop]-Bishop"

                elif chessboard[L1][N1] == w_rook:
                    Pos = []
                    def nextPos(l1,n1,dir):
                        if dir == "right": #right
                            if chessboard[l1][n1+1] == '⬜' or chessboard[l1][n1+1] == '⬛':
                                Pos.insert(0, [l1,n1+1])
                                nextPos(l1,n1+1,"right")
                            elif chessboard[l1][n1+1] == b_pawn or chessboard[l1][n1+1] == b_rook or chessboard[l1][n1+1] == b_knite or chessboard[l1][n1+1] == b_bishop or chessboard[l1][n1+1] == b_king or chessboard[l1][n1+1] == b_queen:
                                Pos.insert(0, [l1,n1+1])

                        if dir == "left": #left
                            if chessboard[l1][n1-1] == '⬜' or chessboard[l1][n1-1] == '⬛':
                                Pos.insert(0, [l1,n1-1])
                                nextPos(l1,n1-1,"left")
                            elif chessboard[l1][n1-1] == b_pawn or chessboard[l1][n1-1] == b_rook or chessboard[l1][n1-1] == b_knite or chessboard[l1][n1-1] == b_bishop or chessboard[l1][n1-1] == b_king or chessboard[l1][n1-1] == b_queen:
                                Pos.insert(0, [l1,n1-1])

                        if dir == "up": #up
                            if chessboard[l1-1][n1] == '⬜' or chessboard[l1-1][n1] == '⬛':
                                Pos.insert(0, [l1-1,n1])
                                nextPos(l1-1,n1,"up")
                            elif chessboard[l1-1][n1] == b_pawn or chessboard[l1-1][n1] == b_rook or chessboard[l1-1][n1] == b_knite or chessboard[l1-1][n1] == b_bishop or chessboard[l1-1][n1] == b_king or chessboard[l1-1][n1] == b_queen:
                                Pos.insert(0, [l1-1,n1])

                        if dir == "down": #down
                            if chessboard[l1+1][n1] == '⬜' or chessboard[l1+1][n1] == '⬛':
                                Pos.insert(0, [l1+1,n1])
                                nextPos(l1+1,n1,"down")
                            elif chessboard[l1+1][n1] == b_pawn or chessboard[l1+1][n1] == b_rook or chessboard[l1+1][n1] == b_knite or chessboard[l1+1][n1] == b_bishop or chessboard[l1+1][n1] == b_king or chessboard[l1+1][n1] == b_queen:
                                Pos.insert(0, [l1+1,n1])

                    nextPos(L1,N1,"right")
                    nextPos(L1,N1,"left")
                    nextPos(L1,N1,"up")
                    nextPos(L1,N1,"down")

                    for p in Pos:
                        if L2 == p[0] and N2 == p[1]:
                            MovePiece(L1,N1,L2,N2)
                            for posit in unmoved:
                                if posit[0] == L1 and posit[1] == N1: #moved rook
                                    unmoved.remove(posit)

                elif chessboard[L1][N1] == w_knite:
                    if ((L2 == L1-2 and N2 == N1-1) or (L2 == L1-2 and N2 == N1+1) or (L2 == L1+2 and N2 == N1-1) or (L2 == L1+2 and N2 == N1+1) or (L2 == L1-1 and N2 == N1-2) or (L2 == L1-1 and N2 == N1+2) or (L2 == L1+1 and N2 == N1-2) or (L2 == L1+1 and N2 == N1+2)) and (chessboard[L2][N2] == '⬜' or chessboard[L2][N2] == '⬛' or chessboard[L2][N2] == b_pawn or chessboard[L2][N2] == b_rook or chessboard[L2][N2] == b_knite or chessboard[L2][N2] == b_bishop or chessboard[L2][N2] == b_king or chessboard[L2][N2] == b_queen):
                        MovePiece(L1,N1,L2,N2)

                elif chessboard[L1][N1] == w_bishop:
                    Pos = []
                    def nextPos(l1,n1,dir):
                        if dir == "right-up": #"right-up"
                            if chessboard[l1-1][n1+1] == '⬜' or chessboard[l1-1][n1+1] == '⬛':
                                Pos.insert(0, [l1-1,n1+1])
                                nextPos(l1-1,n1+1,"right-up")
                            elif chessboard[l1-1][n1+1] == b_pawn or chessboard[l1-1][n1+1] == b_rook or chessboard[l1-1][n1+1] == b_knite or chessboard[l1-1][n1+1] == b_bishop or chessboard[l1-1][n1+1] == b_king or chessboard[l1-1][n1+1] == b_queen:
                                Pos.insert(0, [l1-1,n1+1])

                        if dir == "right-down": #"right-down"
                            if chessboard[l1+1][n1+1] == '⬜' or chessboard[l1+1][n1+1] == '⬛':
                                Pos.insert(0, [l1+1,n1+1])
                                nextPos(l1+1,n1+1,"right-down")
                            elif chessboard[l1+1][n1+1] == b_pawn or chessboard[l1+1][n1+1] == b_rook or chessboard[l1+1][n1+1] == b_knite or chessboard[l1+1][n1+1] == b_bishop or chessboard[l1+1][n1+1] == b_king or chessboard[l1+1][n1+1] == b_queen:
                                Pos.insert(0, [l1+1,n1+1])

                        if dir == "left-up": #"left-up"
                            if chessboard[l1-1][n1-1] == '⬜' or chessboard[l1-1][n1-1] == '⬛':
                                Pos.insert(0, [l1-1,n1-1])
                                nextPos(l1-1,n1-1,"left-up")
                            elif chessboard[l1-1][n1-1] == b_pawn or chessboard[l1-1][n1-1] == b_rook or chessboard[l1-1][n1-1] == b_knite or chessboard[l1-1][n1-1] == b_bishop or chessboard[l1-1][n1-1] == b_king or chessboard[l1-1][n1-1] == b_queen:
                                Pos.insert(0, [l1-1,n1-1])

                        if dir == "left-down": #"left-down"
                            if chessboard[l1+1][n1-1] == '⬜' or chessboard[l1+1][n1-1] == '⬛':
                                Pos.insert(0, [l1+1,n1-1])
                                nextPos(l1+1,n1-1,"left-down")
                            elif chessboard[l1+1][n1-1] == b_pawn or chessboard[l1+1][n1-1] == b_rook or chessboard[l1+1][n1-1] == b_knite or chessboard[l1+1][n1-1] == b_bishop or chessboard[l1+1][n1-1] == b_king or chessboard[l1+1][n1-1] == b_queen:
                                Pos.insert(0, [l1+1,n1-1])

                    nextPos(L1,N1,"right-up")
                    nextPos(L1,N1,"right-down")
                    nextPos(L1,N1,"left-up")
                    nextPos(L1,N1,"left-down")

                    for p in Pos:
                        if L2 == p[0] and N2 == p[1]:
                            MovePiece(L1,N1,L2,N2)

                elif chessboard[L1][N1] == w_queen:
                    Pos = []
                    def nextPos(l1,n1,dir):
                        if dir == "right": #right
                            if chessboard[l1][n1+1] == '⬜' or chessboard[l1][n1+1] == '⬛':
                                Pos.insert(0, [l1,n1+1])
                                nextPos(l1,n1+1,"right")
                            elif chessboard[l1][n1+1] == b_pawn or chessboard[l1][n1+1] == b_rook or chessboard[l1][n1+1] == b_knite or chessboard[l1][n1+1] == b_bishop or chessboard[l1][n1+1] == b_king or chessboard[l1][n1+1] == b_queen:
                                Pos.insert(0, [l1,n1+1])

                        if dir == "left": #left
                            if chessboard[l1][n1-1] == '⬜' or chessboard[l1][n1-1] == '⬛':
                                Pos.insert(0, [l1,n1-1])
                                nextPos(l1,n1-1,"left")
                            elif chessboard[l1][n1-1] == b_pawn or chessboard[l1][n1-1] == b_rook or chessboard[l1][n1-1] == b_knite or chessboard[l1][n1-1] == b_bishop or chessboard[l1][n1-1] == b_king or chessboard[l1][n1-1] == b_queen:
                                Pos.insert(0, [l1,n1-1])

                        if dir == "up": #up
                            if chessboard[l1-1][n1] == '⬜' or chessboard[l1-1][n1] == '⬛':
                                Pos.insert(0, [l1-1,n1])
                                nextPos(l1-1,n1,"up")
                            elif chessboard[l1-1][n1] == b_pawn or chessboard[l1-1][n1] == b_rook or chessboard[l1-1][n1] == b_knite or chessboard[l1-1][n1] == b_bishop or chessboard[l1-1][n1] == b_king or chessboard[l1-1][n1] == b_queen:
                                Pos.insert(0, [l1-1,n1])

                        if dir == "down": #down
                            if chessboard[l1+1][n1] == '⬜' or chessboard[l1+1][n1] == '⬛':
                                Pos.insert(0, [l1+1,n1])
                                nextPos(l1+1,n1,"down")
                            elif chessboard[l1+1][n1] == b_pawn or chessboard[l1+1][n1] == b_rook or chessboard[l1+1][n1] == b_knite or chessboard[l1+1][n1] == b_bishop or chessboard[l1+1][n1] == b_king or chessboard[l1+1][n1] == b_queen:
                                Pos.insert(0, [l1+1,n1])

                        if dir == "right-up": #"right-up"
                            if chessboard[l1-1][n1+1] == '⬜' or chessboard[l1-1][n1+1] == '⬛':
                                Pos.insert(0, [l1-1,n1+1])
                                nextPos(l1-1,n1+1,"right-up")
                            elif chessboard[l1-1][n1+1] == b_pawn or chessboard[l1-1][n1+1] == b_rook or chessboard[l1-1][n1+1] == b_knite or chessboard[l1-1][n1+1] == b_bishop or chessboard[l1-1][n1+1] == b_king or chessboard[l1-1][n1+1] == b_queen:
                                Pos.insert(0, [l1-1,n1+1])

                        if dir == "right-down": #"right-down"
                            if chessboard[l1+1][n1+1] == '⬜' or chessboard[l1+1][n1+1] == '⬛':
                                Pos.insert(0, [l1+1,n1+1])
                                nextPos(l1+1,n1+1,"right-down")
                            elif chessboard[l1+1][n1+1] == b_pawn or chessboard[l1+1][n1+1] == b_rook or chessboard[l1+1][n1+1] == b_knite or chessboard[l1+1][n1+1] == b_bishop or chessboard[l1+1][n1+1] == b_king or chessboard[l1+1][n1+1] == b_queen:
                                Pos.insert(0, [l1+1,n1+1])

                        if dir == "left-up": #"left-up"
                            if chessboard[l1-1][n1-1] == '⬜' or chessboard[l1-1][n1-1] == '⬛':
                                Pos.insert(0, [l1-1,n1-1])
                                nextPos(l1-1,n1-1,"left-up")
                            elif chessboard[l1-1][n1-1] == b_pawn or chessboard[l1-1][n1-1] == b_rook or chessboard[l1-1][n1-1] == b_knite or chessboard[l1-1][n1-1] == b_bishop or chessboard[l1-1][n1-1] == b_king or chessboard[l1-1][n1-1] == b_queen:
                                Pos.insert(0, [l1-1,n1-1])

                        if dir == "left-down": #"left-down"
                            if chessboard[l1+1][n1-1] == '⬜' or chessboard[l1+1][n1-1] == '⬛':
                                Pos.insert(0, [l1+1,n1-1])
                                nextPos(l1+1,n1-1,"left-down")
                            elif chessboard[l1+1][n1-1] == b_pawn or chessboard[l1+1][n1-1] == b_rook or chessboard[l1+1][n1-1] == b_knite or chessboard[l1+1][n1-1] == b_bishop or chessboard[l1+1][n1-1] == b_king or chessboard[l1+1][n1-1] == b_queen:
                                Pos.insert(0, [l1+1,n1-1])

                    nextPos(L1,N1,"right")
                    nextPos(L1,N1,"left")
                    nextPos(L1,N1,"up")
                    nextPos(L1,N1,"down")
                    nextPos(L1,N1,"right-up")
                    nextPos(L1,N1,"right-down")
                    nextPos(L1,N1,"left-up")
                    nextPos(L1,N1,"left-down")

                    for p in Pos:
                        if L2 == p[0] and N2 == p[1]:
                            MovePiece(L1,N1,L2,N2)

                elif chessboard[L1][N1] == w_king: #White King
                    if ((L2 == L1-1 and N2 == N1) or (L2 == L1-1 and N2 == N1+1) or (L2 == L1 and N2 == N1+1) or (L2 == L1+1 and N2 == N1+1) or (L2 == L1+1 and N2 == N1) or (L2 == L1+1 and N2 == N1-1) or (L2 == L1 and N2 == N1-1) or (L2 == L1-1 and N2 == N1-1)) and (chessboard[L2][N2] == '⬜' or chessboard[L2][N2] == '⬛' or chessboard[L2][N2] == b_pawn or chessboard[L2][N2] == b_rook or chessboard[L2][N2] == b_knite or chessboard[L2][N2] == b_bishop or chessboard[L2][N2] == b_king or chessboard[L2][N2] == b_queen):
                        MovePiece(L1,N1,L2,N2)
                        for posit in unmoved:
                            if posit[0] == L1 and posit[1] == N1: #moved king
                                unmoved.remove(posit)
                    elif chessboard[L2][N2] == w_rook:
                        unmoved_rook = False
                        unmoved_king = False
                        for posit in unmoved:
                            if posit[0] == L2 and posit[1] == N2: #unmoved rook
                                unmoved_rook = True
                            elif posit[0] == L1 and posit[1] == N1: #unmoved king
                                unmoved_king = True
                        if L2 == L1 and unmoved_rook and unmoved_king:
                            if N2 > N1 and (chessboard[L1][N1+1] == '⬜' or chessboard[L1][N1+1] =='⬛') and (chessboard[L1][N1+2] == '⬜' or chessboard[L1][N1+2] =='⬛'):
                                MovePiece(L1,N1,L2,N2-1)
                                chessboard[L1][N1+1] = w_rook
                                chessboard[L1][N2] = '⬜'
                                for posit in unmoved:
                                    if posit[0] == L1 and posit[1] == N1: #moved king
                                        unmoved.remove(posit)
                            elif N2 < N1 and (chessboard[L1][N1-1] == '⬜' or chessboard[L1][N1-1] =='⬛') and (chessboard[L1][N1-2] == '⬜' or chessboard[L1][N1-2] =='⬛') and (chessboard[L1][N1-3] == '⬜' or chessboard[L1][N1-3] =='⬛'):
                                MovePiece(L1,N1,L2,N2+1)
                                chessboard[L1][N1-2] = w_rook
                                chessboard[L1][N2] = '⬛'
                                for posit in unmoved:
                                    if posit[0] == L1 and posit[1] == N1: #moved king
                                        unmoved.remove(posit)

            elif chessboard[8][8] == '⬛' and User == Player2: #Black turn
                if chessboard[L1][N1] == b_pawn:
                    if L1 == 1: #2 space
                        #move
                        if ((L2 == L1+1 and N2 == N1) or (L2 == L1+2 and N2 == N1)) and (chessboard[L2][N2] == '⬜' or chessboard[L2][N2] == '⬛'):
                            MovePiece(L1,N1,L2,N2)
                        #kill
                        elif ((L2 == L1+1 and N2 == N1+1) or (L2 == L1+1 and N2 == N1-1)) and (chessboard[L2][N2] == w_pawn or chessboard[L2][N2] == w_rook or chessboard[L2][N2] == w_knite or chessboard[L2][N2] == w_bishop or chessboard[L2][N2] == w_king or chessboard[L2][N2] == w_queen):
                            MovePiece(L1,N1,L2,N2)
                    else:
                        #move
                        if (L2 == L1+1 and N2 == N1) and (chessboard[L2][N2] == '⬜' or chessboard[L2][N2] == '⬛'):
                            MovePiece(L1,N1,L2,N2)
                        #kill
                        elif ((L2 == L1+1 and N2 == N1+1) or (L2 == L1+1 and N2 == N1-1)) and (chessboard[L2][N2] == w_pawn or chessboard[L2][N2] == w_rook or chessboard[L2][N2] == w_knite or chessboard[L2][N2] == w_bishop or chessboard[L2][N2] == w_king or chessboard[L2][N2] == w_queen):
                            MovePiece(L1,N1,L2,N2)                   

                elif chessboard[L1][N1] == b_rook:
                    Pos = []
                    def nextPos(l1,n1,dir):
                        if dir == "right": #right
                            if chessboard[l1][n1+1] == '⬜' or chessboard[l1][n1+1] == '⬛':
                                Pos.insert(0, [l1,n1+1])
                                nextPos(l1,n1+1,"right")
                            elif chessboard[l1][n1+1] == w_pawn or chessboard[l1][n1+1] == w_rook or chessboard[l1][n1+1] == w_knite or chessboard[l1][n1+1] == w_bishop or chessboard[l1][n1+1] == w_king or chessboard[l1][n1+1] == w_queen:
                                Pos.insert(0, [l1,n1+1])

                        if dir == "left": #left
                            if chessboard[l1][n1-1] == '⬜' or chessboard[l1][n1-1] == '⬛':
                                Pos.insert(0, [l1,n1-1])
                                nextPos(l1,n1-1,"left")
                            elif chessboard[l1][n1-1] == w_pawn or chessboard[l1][n1-1] == w_rook or chessboard[l1][n1-1] == w_knite or chessboard[l1][n1-1] == w_bishop or chessboard[l1][n1-1] == w_king or chessboard[l1][n1-1] == w_queen:
                                Pos.insert(0, [l1,n1-1])

                        if dir == "up": #up
                            if chessboard[l1-1][n1] == '⬜' or chessboard[l1-1][n1] == '⬛':
                                Pos.insert(0, [l1-1,n1])
                                nextPos(l1-1,n1,"up")
                            elif chessboard[l1-1][n1] == w_pawn or chessboard[l1-1][n1] == w_rook or chessboard[l1-1][n1] == w_knite or chessboard[l1-1][n1] == w_bishop or chessboard[l1-1][n1] == w_king or chessboard[l1-1][n1] == w_queen:
                                Pos.insert(0, [l1-1,n1])

                        if dir == "down": #down
                            if chessboard[l1+1][n1] == '⬜' or chessboard[l1+1][n1] == '⬛':
                                Pos.insert(0, [l1+1,n1])
                                nextPos(l1+1,n1,"down")
                            elif chessboard[l1+1][n1] == w_pawn or chessboard[l1+1][n1] == w_rook or chessboard[l1+1][n1] == w_knite or chessboard[l1+1][n1] == w_bishop or chessboard[l1+1][n1] == w_king or chessboard[l1+1][n1] == w_queen:
                                Pos.insert(0, [l1+1,n1])

                    nextPos(L1,N1,"right")
                    nextPos(L1,N1,"left")
                    nextPos(L1,N1,"up")
                    nextPos(L1,N1,"down")

                    for p in Pos:
                        if L2 == p[0] and N2 == p[1]:
                            MovePiece(L1,N1,L2,N2)
                            for posit in unmoved:
                                if posit[0] == L1 and posit[1] == N1: #moved rook
                                    unmoved.remove(posit)

                elif chessboard[L1][N1] == b_knite:
                    if ((L2 == L1-2 and N2 == N1-1) or (L2 == L1-2 and N2 == N1+1) or (L2 == L1+2 and N2 == N1-1) or (L2 == L1+2 and N2 == N1+1) or (L2 == L1-1 and N2 == N1-2) or (L2 == L1-1 and N2 == N1+2) or (L2 == L1+1 and N2 == N1-2) or (L2 == L1+1 and N2 == N1+2)) and (chessboard[L2][N2] == '⬜' or chessboard[L2][N2] == '⬛' or chessboard[L2][N2] == w_pawn or chessboard[L2][N2] == w_rook or chessboard[L2][N2] == w_knite or chessboard[L2][N2] == w_bishop or chessboard[L2][N2] == w_king or chessboard[L2][N2] == w_queen):
                        MovePiece(L1,N1,L2,N2)

                elif chessboard[L1][N1] == b_bishop:
                    Pos = []
                    def nextPos(l1,n1,dir):
                        if dir == "right-up": #"right-up"
                            if chessboard[l1-1][n1+1] == '⬜' or chessboard[l1-1][n1+1] == '⬛':
                                Pos.insert(0, [l1-1,n1+1])
                                nextPos(l1-1,n1+1,"right-up")
                            elif chessboard[l1-1][n1+1] == w_pawn or chessboard[l1-1][n1+1] == w_rook or chessboard[l1-1][n1+1] == w_knite or chessboard[l1-1][n1+1] == w_bishop or chessboard[l1-1][n1+1] == w_king or chessboard[l1-1][n1+1] == w_queen:
                                Pos.insert(0, [l1-1,n1+1])

                        if dir == "right-down": #"right-down"
                            if chessboard[l1+1][n1+1] == '⬜' or chessboard[l1+1][n1+1] == '⬛':
                                Pos.insert(0, [l1+1,n1+1])
                                nextPos(l1+1,n1+1,"right-down")
                            elif chessboard[l1+1][n1+1] == w_pawn or chessboard[l1+1][n1+1] == w_rook or chessboard[l1+1][n1+1] == w_knite or chessboard[l1+1][n1+1] == w_bishop or chessboard[l1+1][n1+1] == w_king or chessboard[l1+1][n1+1] == w_queen:
                                Pos.insert(0, [l1+1,n1+1])

                        if dir == "left-up": #"left-up"
                            if chessboard[l1-1][n1-1] == '⬜' or chessboard[l1-1][n1-1] == '⬛':
                                Pos.insert(0, [l1-1,n1-1])
                                nextPos(l1-1,n1-1,"left-up")
                            elif chessboard[l1-1][n1-1] == w_pawn or chessboard[l1-1][n1-1] == w_rook or chessboard[l1-1][n1-1] == w_knite or chessboard[l1-1][n1-1] == w_bishop or chessboard[l1-1][n1-1] == w_king or chessboard[l1-1][n1-1] == w_queen:
                                Pos.insert(0, [l1-1,n1-1])

                        if dir == "left-down": #"left-down"
                            if chessboard[l1+1][n1-1] == '⬜' or chessboard[l1+1][n1-1] == '⬛':
                                Pos.insert(0, [l1+1,n1-1])
                                nextPos(l1+1,n1-1,"left-down")
                            elif chessboard[l1+1][n1-1] == w_pawn or chessboard[l1+1][n1-1] == w_rook or chessboard[l1+1][n1-1] == w_knite or chessboard[l1+1][n1-1] == w_bishop or chessboard[l1+1][n1-1] == w_king or chessboard[l1+1][n1-1] == w_queen:
                                Pos.insert(0, [l1+1,n1-1])

                    nextPos(L1,N1,"right-up")
                    nextPos(L1,N1,"right-down")
                    nextPos(L1,N1,"left-up")
                    nextPos(L1,N1,"left-down")

                    for p in Pos:
                        if L2 == p[0] and N2 == p[1]:
                            MovePiece(L1,N1,L2,N2)

                elif chessboard[L1][N1] == b_queen:
                    Pos = []
                    def nextPos(l1,n1,dir):
                        if dir == "right": #right
                            if chessboard[l1][n1+1] == '⬜' or chessboard[l1][n1+1] == '⬛':
                                Pos.insert(0, [l1,n1+1])
                                nextPos(l1,n1+1,"right")
                            elif chessboard[l1][n1+1] == w_pawn or chessboard[l1][n1+1] == w_rook or chessboard[l1][n1+1] == w_knite or chessboard[l1][n1+1] == w_bishop or chessboard[l1][n1+1] == w_king or chessboard[l1][n1+1] == w_queen:
                                Pos.insert(0, [l1,n1+1])

                        if dir == "left": #left
                            if chessboard[l1][n1-1] == '⬜' or chessboard[l1][n1-1] == '⬛':
                                Pos.insert(0, [l1,n1-1])
                                nextPos(l1,n1-1,"left")
                            elif chessboard[l1][n1-1] == w_pawn or chessboard[l1][n1-1] == w_rook or chessboard[l1][n1-1] == w_knite or chessboard[l1][n1-1] == w_bishop or chessboard[l1][n1-1] == w_king or chessboard[l1][n1-1] == w_queen:
                                Pos.insert(0, [l1,n1-1])

                        if dir == "up": #up
                            if chessboard[l1-1][n1] == '⬜' or chessboard[l1-1][n1] == '⬛':
                                Pos.insert(0, [l1-1,n1])
                                nextPos(l1-1,n1,"up")
                            elif chessboard[l1-1][n1] == w_pawn or chessboard[l1-1][n1] == w_rook or chessboard[l1-1][n1] == w_knite or chessboard[l1-1][n1] == w_bishop or chessboard[l1-1][n1] == w_king or chessboard[l1-1][n1] == w_queen:
                                Pos.insert(0, [l1-1,n1])

                        if dir == "down": #down
                            if chessboard[l1+1][n1] == '⬜' or chessboard[l1+1][n1] == '⬛':
                                Pos.insert(0, [l1+1,n1])
                                nextPos(l1+1,n1,"down")
                            elif chessboard[l1+1][n1] == w_pawn or chessboard[l1+1][n1] == w_rook or chessboard[l1+1][n1] == w_knite or chessboard[l1+1][n1] == w_bishop or chessboard[l1+1][n1] == w_king or chessboard[l1+1][n1] == w_queen:
                                Pos.insert(0, [l1+1,n1])

                        if dir == "right-up": #"right-up"
                            if chessboard[l1-1][n1+1] == '⬜' or chessboard[l1-1][n1+1] == '⬛':
                                Pos.insert(0, [l1-1,n1+1])
                                nextPos(l1-1,n1+1,"right-up")
                            elif chessboard[l1-1][n1+1] == w_pawn or chessboard[l1-1][n1+1] == w_rook or chessboard[l1-1][n1+1] == w_knite or chessboard[l1-1][n1+1] == w_bishop or chessboard[l1-1][n1+1] == w_king or chessboard[l1-1][n1+1] == w_queen:
                                Pos.insert(0, [l1-1,n1+1])

                        if dir == "right-down": #"right-down"
                            if chessboard[l1+1][n1+1] == '⬜' or chessboard[l1+1][n1+1] == '⬛':
                                Pos.insert(0, [l1+1,n1+1])
                                nextPos(l1+1,n1+1,"right-down")
                            elif chessboard[l1+1][n1+1] == w_pawn or chessboard[l1+1][n1+1] == w_rook or chessboard[l1+1][n1+1] == w_knite or chessboard[l1+1][n1+1] == w_bishop or chessboard[l1+1][n1+1] == w_king or chessboard[l1+1][n1+1] == w_queen:
                                Pos.insert(0, [l1+1,n1+1])

                        if dir == "left-up": #"left-up"
                            if chessboard[l1-1][n1-1] == '⬜' or chessboard[l1-1][n1-1] == '⬛':
                                Pos.insert(0, [l1-1,n1-1])
                                nextPos(l1-1,n1-1,"left-up")
                            elif chessboard[l1-1][n1-1] == w_pawn or chessboard[l1-1][n1-1] == w_rook or chessboard[l1-1][n1-1] == w_knite or chessboard[l1-1][n1-1] == w_bishop or chessboard[l1-1][n1-1] == w_king or chessboard[l1-1][n1-1] == w_queen:
                                Pos.insert(0, [l1-1,n1-1])

                        if dir == "left-down": #"left-down"
                            if chessboard[l1+1][n1-1] == '⬜' or chessboard[l1+1][n1-1] == '⬛':
                                Pos.insert(0, [l1+1,n1-1])
                                nextPos(l1+1,n1-1,"left-down")
                            elif chessboard[l1+1][n1-1] == w_pawn or chessboard[l1+1][n1-1] == w_rook or chessboard[l1+1][n1-1] == w_knite or chessboard[l1+1][n1-1] == w_bishop or chessboard[l1+1][n1-1] == w_king or chessboard[l1+1][n1-1] == w_queen:
                                Pos.insert(0, [l1+1,n1-1])

                    nextPos(L1,N1,"right")
                    nextPos(L1,N1,"left")
                    nextPos(L1,N1,"up")
                    nextPos(L1,N1,"down")
                    nextPos(L1,N1,"right-up")
                    nextPos(L1,N1,"right-down")
                    nextPos(L1,N1,"left-up")
                    nextPos(L1,N1,"left-down")

                    for p in Pos:
                        if L2 == p[0] and N2 == p[1]:
                            MovePiece(L1,N1,L2,N2)
                    
                elif chessboard[L1][N1] == b_king:
                    if ((L2 == L1-1 and N2 == N1) or (L2 == L1-1 and N2 == N1+1) or (L2 == L1 and N2 == N1+1) or (L2 == L1+1 and N2 == N1+1) or (L2 == L1+1 and N2 == N1) or (L2 == L1+1 and N2 == N1-1) or (L2 == L1 and N2 == N1-1) or (L2 == L1-1 and N2 == N1-1)) and (chessboard[L2][N2] == '⬜' or chessboard[L2][N2] == '⬛' or chessboard[L2][N2] == w_pawn or chessboard[L2][N2] == w_rook or chessboard[L2][N2] == w_knite or chessboard[L2][N2] == w_bishop or chessboard[L2][N2] == w_king or chessboard[L2][N2] == w_queen):
                        MovePiece(L1,N1,L2,N2)
                        for posit in unmoved:
                            if posit[0] == L1 and posit[1] == N1: #moved king
                                unmoved.remove(posit)
                    elif chessboard[L2][N2] == w_rook:
                        unmoved_rook = False
                        unmoved_king = False
                        for posit in unmoved:
                            if posit[0] == L2 and posit[1] == N2: #unmoved rook
                                unmoved_rook = True
                            elif posit[0] == L1 and posit[1] == N1: #unmoved king
                                unmoved_king = True
                        if L2 == L1 and unmoved_rook and unmoved_king:
                            if N2 > N1 and (chessboard[L1][N1+1] == '⬜' or chessboard[L1][N1+1] =='⬛') and (chessboard[L1][N1+2] == '⬜' or chessboard[L1][N1+2] =='⬛'):
                                MovePiece(L1,N1,L2,N2-1)
                                chessboard[L1][N1+1] = w_rook
                                chessboard[L1][N2] = '⬛'
                                for posit in unmoved:
                                    if posit[0] == L1 and posit[1] == N1: #moved king
                                        unmoved.remove(posit)
                            elif N2 < N1 and (chessboard[L1][N1-1] == '⬜' or chessboard[L1][N1-1] =='⬛') and (chessboard[L1][N1-2] == '⬜' or chessboard[L1][N1-2] =='⬛') and (chessboard[L1][N1-3] == '⬜' or chessboard[L1][N1-3] =='⬛'):
                                MovePiece(L1,N1,L2,N2+1)
                                chessboard[L1][N1-2] = w_rook
                                chessboard[L1][N2] = '⬜'
                                for posit in unmoved:
                                    if posit[0] == L1 and posit[1] == N1: #moved king
                                        unmoved.remove(posit)

            return PrintBoard() #send Actual Board
        
        if Promote:
            if p_message == 'queen':
                Promotion(Pl,Pn,'queen')
            elif p_message == 'rook':
                Promotion(Pl,Pn,'rook')
            elif p_message == 'knite':
                Promotion(Pl,Pn,'knite')
            elif p_message == 'bishop':
                Promotion(Pl,Pn,'bishop')
            return PrintBoard() #send Actual Board

        if p_message == 'board':
            return PrintBoard() #send Actual Board

        if p_message == 'surrender' and isPlaying: #Forfait
            if User == Player1:
                Winner = "Black"
            elif User == Player2:
                Winner = "White"
            isPlaying = False
            Player1 = False
            Player2 = False
            return Winner + " Win"
        
        if p_message[0] == 'w' or p_message[0] == 'b': #set emojis
            space_index = False
            start_emoji_index = False
            for l,let in enumerate(p_message): #ex:"w_pawn :moyai "
                if (not space_index) and let == " ":
                    space_index = l
                elif (not start_emoji_index) and let == ":":
                    start_emoji_index = l
            
            if space_index != False and start_emoji_index != False:
                globals()[p_message[0:space_index]] = p_message[start_emoji_index:len(p_message)]+':'
                return p_message[0:space_index] + " " + globals()[p_message[0:space_index]]
        
    else:
        if p_message == 'chess_channel':
            TheGoodChannel = Chan
            return "This will be the channel to play Chess"
    #return "I didn't get" + p_message
