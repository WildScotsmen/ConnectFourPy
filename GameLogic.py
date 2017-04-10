import cPickle as pickle

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" @author Scoots
" @version 3/30/2017
" @see https://docs.python.org/2/library/pickle.html
"
" This .py file includes the function needed to play the
" Connect Four game. It includes methods for saving and
" loading files along with the basic logic for the game
" rules.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# The game board.
board = []

# The height of the game board.
height = 7

# The width of the game board.
width = 6

# The win length for the game rules.
winLength = 4

# The current player.
player = 1

"""
" Sets the height of the game board to the passed parameter.
"
" @param h, the new height of the game board.
"""
def setHeight(h):
    global height
    height = h

"""
" Sets the width of the game board to the passed parameter.
"
" @param w, the new width of the game board.
"""
def setWidth(w):
    global width
    width = w

"""
" Sets the number of chips in a row needed to win the game.
"
" @param l, the new win length for the game rules.
"""
def setWinLength(l):
    global winLength
    winLength = l

"""
" Sets the game's turn to the player who is passed as a parameter.
"
" @param p, the new current player.
"""
def setPlayer(p):
    global player
    player = p

"""
" Returns the height of the game board.
"
" @return height, the height of the game board.
"""
def getWidth():
    global width
    return width

"""
" Returns the width of the game board.
"
" @return width, the width of the game board.
"""
def getHeight():
    global height
    return height

"""
" Returns the length to win the game.
"
" @return winLength, the length to win.
"""
def getWinLength():
    global winLength
    return winLength

"""
" Returns the current turn's player.
"
" @return player, the current player.
"""
def getPlayer():
    global player
    return player

"""
" Resets the board with the current parameters
" to start a new game.
"""
def populateBoard():
    global board, height, width
    board = []
    for i in range (0, height):
        board.append([])
        for j in range (0, width):
            board[i].append('')
        board[i] = ['*' for x in board[i]]

"""
" Prints the current game board.
"""
def printBoard():
    global board
    for i in board:
        for j in i:
            print j,
        print ''

"""
" Places a chip in the desired column. Also makes sure
" that you can place a chip in that column, returning False
" if you cannot and True if you can.
"
" @param col, the desired column.
" @param player, the chip being placed.
" @return a bool, based on whether or not its a valid move.
"""
def placeChip(col, player):
    global board, height, width

    if col > width - 1 or col < 0:
        return False

    for i in range(height - 1, -1, -1):
        if i > 0 and ((board[i][col] == 'o') or (board[i][col] == 'x')):
            continue
        elif i == 0 and (board[i][col] != '*'):
            return False
        else:
            board[i][col] = player
            break
    return True

"""
" Saves the current board, its parameters and the game
" parameters to a file using a pickling function.
"
" @param filename, the file being saved to.
"""
def saveGame(filename):
    global board, width, height, winLength

    game_data = [board, width, height, winLength]
    pickle.dump(game_data, open(filename, "wb"))

"""
" Loads a previous game from a file.
"
" @param filename, the file being loaded from.
"""
def loadGame(filename):
    global board, width, height, winLength

    game_data = pickle.load(open(filename, "rb" ))
    board = game_data[0]
    width = game_data[1]
    height = game_data[2]
    winLength = game_data[3]

"""
" Checks to see if the chip passed to the function has
" enough chips in a row to warrant a win. Returns True
" if that chip's player has won, and False if that
" player has not.
"
" @param player, the chip being checked for.
" @return a bool, based on whether or not the player won.
"""
def checkWin(player):
    global board, width, height
    row = 0
    col = 0

    # 1 by 1 board
    if height == 1 and width == 1 and winLength == 1:
        if board[0][0] == player:
            return True
        else:
            return False

    # Horizontal check
    count = 0
    for i in range(0, height):
        for j in range(0, width):
            if board[i][j] == player:
                count = count + 1
            else:
                count = 0
            if count == winLength:
                return True
        count = 0

    # Vertical check
    count = 0
    for i in range(0, width):
        for j in range(0, height):
            if board[j][i] == player:
                count = count + 1
            else:
                count = 0
            if count == winLength:
                return True
        count = 0

    # Negative slope diagonal
    count = 0
    for i in range(0, height):
        for j in range(0, width):
            row = i
            col = j
            count = 0
            while (row < height and col < width):
                if board[row][col] == player:
                    count = count + 1
                    row = row + 1
                    col = col + 1
                else:
                    row = row + 1
                    col = col + 1
                    count = 0
                if count == winLength:
                    return True

    # Positive slope diagonal
    count = 0
    for i in range(0, height):
        for j in range(0, width):
            row = i
            col = j
            count = 0
            while row >= 0 and col < width:
                if board[row][col] == player:
                    count = count + 1
                    row = row - 1
                    col = col + 1
                else:
                    row = row - 1
                    col = col + 1
                    count = 0
                if count == winLength:
                    return True

    return False
