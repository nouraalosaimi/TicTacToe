import datetime
start_time = datetime.datetime.now()
global gameTime #time of the game from starting the code till it finishes the game
searchTime = 0.0 #var to store time to search in minimax method

compMoveDepth = 0 #number of time the computer plays
playerMoveDepth = 0 #number of time the computer plays

numOfNodes = 0 #total number of tree nodes 
bestMoveNode = 0 #total number of expanded (visited) nodes that have been saved in memory

# printBoard: prints board and positions
def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")

#spaceIsFree: returns a boolean vaule after checking if the selected position free or not
def spaceIsFree(position): 
    if board[position] == ' ':
        return True
    else:
        return False

#insertLetter: before inseting it checks id the selected position free, if it's free it inserts it and prints the upated board
# then checks if the game is over by draw, win, or lose. If the game is over it prints the resluts. 
def insertLetter(letter, position):
    global DepthCount 
    DepthCount = compMoveDepth + playerMoveDepth #total turns/moves player and comp made, where every turn/move is a level (depth)
    if spaceIsFree(position): #checks if the selected position is free
        board[position] = letter

        printBoard(board)
        if (checkDraw()): # checks if the game is over after inserting
            print("Draw!")
            end_time = datetime.datetime.now()
            time_diff = (end_time - start_time)
            execution_time = time_diff.total_seconds()    
            gameTime = execution_time
            print('the time to search is ' + str(searchTime))
            print('Gmae time is ' + str(gameTime))
            print('Depth is ' + str(DepthCount))
            print('Total number of nodes is ' + str(numOfNodes))
            print('Total number bestMoveNode is ' + str(bestMoveNode))
            exit()
        if checkForWin():
            if letter == 'X':
                print("Bot wins!")
                end_time = datetime.datetime.now()
                time_diff = (end_time - start_time)
                execution_time = time_diff.total_seconds()    
                gameTime = execution_time
                print('the time to search is ' + str(searchTime))
                print('Gmae time is ' + str(gameTime))
                print('Depth is ' + str(DepthCount))
                print('Total number of nodes is ' + str(numOfNodes))
                print('Total number bestMoveNode is ' + str(bestMoveNode))


                exit()
            else:
                print("Player wins!")
                end_time = datetime.datetime.now()
                time_diff = (end_time - start_time)
                execution_time = time_diff.total_seconds()    
                gameTime = execution_time
                print('the time to search is ' + str(searchTime))
                print('Gmae time is ' + str(gameTime))
                print('Depth is ' + str(DepthCount))
                print('Total number of nodes is ' + str(numOfNodes))
                print('Total number bestMoveNode is ' + str(bestMoveNode))
                exit()

        return


    else: #space isn'nt free
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position)
        return

#checkForWin: if any of plays won by inserting the mark(latter) horizontally, vertically, or diagonally.
def checkForWin(): 
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

#checkWhichMarkWon: checks which player won based on mark(latter) placements
def checkWhichMarkWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

#checkDraw: checks every position in board, if there's no more free positions then the board is full,
#returns true (draw).
def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True


#playerMove: it asks user to insert for a position then call insertLetter for inserting
def playerMove(): 
    global playerMoveDepth
    position = int(input("Enter the position for 'O':  "))
    insertLetter(player, position)
    playerMoveDepth = playerMoveDepth + 1 #player's move, where every new move is depth + 1 (new level)
    return

#compMove: uses minimax to find the best position with best score by checking every state in the tree 
# by comparing the scores of positions
def compMove():
    global compMoveDepth
    bestScore = -10
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key 
    insertLetter(bot, bestMove)
    compMoveDepth = compMoveDepth + 1 #computer's move, where every new move is depth + 1 (new level)
    return


#minimax: finds the best position with best score by checking every state in the tree 
# by comparing the scores of positions
def minimax(board, depth, isMaximizing):
    global searchTime
    global numOfNodes
    global bestMoveNode

#evalution: if checkWhichMarkWon bot won it returns 1, player won returns -1, and if it is a draw it returns 0
    if (checkWhichMarkWon(bot)):
        return 1
    elif (checkWhichMarkWon(player)):
        return -1
    elif (checkDraw()):
        return 0

    

    if (isMaximizing): #Maximizing: find the best highest score (tries to maximze score to win) 
                        #by checking and comparing scores for every state
        start_time = datetime.datetime.now()
        bestScore = -100
        for key in board.keys():
            numOfNodes = numOfNodes + 1
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
                    bestMoveNode = bestMoveNode + 1

        end_time = datetime.datetime.now()
        time_diff = (end_time - start_time)
        execution_time = time_diff.total_seconds()    
        searchTime+= execution_time
        return bestScore

    else: #Minimizing: find the best lowest score (tries to minimaze score for the opposite player) 
        #by checking and comparing scores for every state
        bestScore = 100
        start_time = datetime.datetime.now()
        for key in board.keys():
            numOfNodes = numOfNodes + 1
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
                    bestMoveNode = bestMoveNode + 1
        return bestScore

#board is specified as dictionary, starts with 1 till 9 for evry position
board = {1: ' ', 2: ' ', 3: ' ',
        4: ' ', 5: ' ', 6: ' ',
        7: ' ', 8: ' ', 9: ' '}


printBoard(board)
print("Computer goes first! Good luck.")
print("Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")
player = 'O'
bot = 'X'

#lets the comp play first
global firstComputerMove
firstComputerMove = True

#if the game is not over, keep playing
while not checkForWin():
    compMove()
    playerMove()
