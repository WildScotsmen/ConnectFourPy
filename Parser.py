import argparse

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" @author Scoots
" @version 3/30/2017
" @see https://docs.python.org/2.7/library/argparse.html
"
" This .py file implements our command line argument
" parser using argparse.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Creates our parser.
parser = argparse.ArgumentParser(description="Connect Four game!")

# Adds our arguments to the parser.
parser.add_argument('--height', default='6', action='store', type=int,
                    dest='height', help="Height of the game board.")
parser.add_argument('--width', default='7', action='store', type=int,
                    dest='width', help="Width of the game board.")
parser.add_argument('--square', default='-1', action='store', type=int,
                    dest='square', help='Square dimension for game board.')
parser.add_argument('--connect', default='4', action='store', type=int,
                    dest='connect', help="Chips in a row to win.")
parser.add_argument('--load', default=None, action='store', type=str,
                    dest='loadName', help="Load a previous game.")

# Save results from the command line for further usage.
results = parser.parse_args()

