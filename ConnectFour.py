from GameLogic import *
from Parser import *

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" @author Jacob McCloughan
" @version 3/30/2017
" @see GameLogic.py
" @see Parser.py
"
" This .py file includes the main method for our Connect
" Four game.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
" Main method for our Connect Four Game. Drives the entire
" game with a while loop, while also reading in command line
" arguments and initializing the game data.
"""
def main():
    # Variables
    input = ""
    chip = ''
    setPlayer(1)

    # Checks command line arguments
    if (results.height <= 0):
        print "Error, height is invalid value. Setting to default."
    else:
        setHeight(results.height)
    if (results.width <= 0):
        print "Error, width is invalid value. Setting to default."
    else:
        setWidth(results.width)
    if (results.connect <= 0):
        print "Error, width is invalid value. Setting to default."
    else:
        setWinLength(results.connect)
    if (results.square < -1 or results.square == 0):
        print "Error, square is invalid value. Setting to default."
    elif (results.square == -1):
        pass
    else:
        setWidth(results.square)
        setHeight(results.square)
    if (results.loadName != None):
        try:
            loadGame(results.loadName)
        except IOError:
            print "Error reading file from command line."
            return
    else:
        populateBoard()

    # Introductory game message
    print "Welcome to Connect Four! Type 'stop' to stop, 'save' to save and 'load' to load."

    # The game loop
    while(True):
        # Sets the current chip based on the current player
        if getPlayer() == 1:
            chip = 'o'
        if getPlayer() == 2:
            chip = 'x'
        printBoard()

        # Receives player input
        print "\nIt is Player " + str(getPlayer()) + "'s turn."
        input = raw_input("Input a column (from 1 to " + str(getWidth())
                          + ") to place a token:\n")

        # Checks for any commands
        if (str(input) == 'stop'):
            return
        if (str(input) == 'save'):
            print "Type a filename to save to:"
            input = raw_input()
            saveGame(input)
            print "Game saved."
            continue
        if (str(input) == 'load'):
            print "Type a filename to load from:"
            input = raw_input()
            try:
                loadGame(input)
            except IOError:
                print "Error loading file."
            else:
                print "Game loaded."
            continue
        try:
            input = int(input)
        except ValueError:
            print "Invalid input. Try again."
            continue

        # Attempts to place chip in desired column
        input = input - 1
        if placeChip(input, chip) == False:
            print "Invalid input. Try again."
            continue
        else:
            if checkEnd(chip):
                printBoard()
                while (True):
                    print "Would you like to play again? Say 'yes' for yes and 'no' for no."

                    input = raw_input()

                    if (str(input) == 'yes'):
                        populateBoard()
                        setPlayer(1)
                        print "Welcome to Connect Four! Type 'stop' at any time to stop."
                        break
                    elif (str(input) == 'no'):
                        return
                    else:
                        print "Invalid input."
                        continue

                continue

            # Gives turn to the next player
            if getPlayer() == 1:
                setPlayer(2)
                continue
            if getPlayer() == 2:
                setPlayer(1)
                continue

"""
" Helper function that uses the checkWin() function
" from the GameLogic file to check for a win. Prints
" a message if the player whose chip is passed as a
" parameter won the game.
"
" @param c, the chip being checked for.
" @return a bool, based on whether or not the player won.
"""
def checkEnd(c):
    p = ""

    if c == 'o':
        p = "1"
    if c == 'x':
        p = "2"

    if checkWin(c):
        print "\nPlayer " + p + " wins!"
        return True
    else:
        return False

if __name__ == "__main__":
    main()


