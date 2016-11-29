from tictactoe import *

def in_game_parse(line):
    """ Parse takes in a command from the user and returns an expression.
    If the first word of the command is 'Reset', the returned expression
    should be the 'Reset' command. Otherwise, the line corresponds to a
    'Place' expression.  In 'Place' expressions, the first symbol (X or O)
    encountered is the piece placed.  The first number 0 to 8 after finding
    the piece is the space where it is to be placed.
    
    Be sure to change the space number from a string to an integer.

    >>> in_game_parse('Reset the board, please')
    ['Reset']
    >>> in_game_parse('Reset the board X 1')
    ['Reset']
    >>> in_game_parse('Place X on 1')
    ['Place', ['X', 1]]
    >>> in_game_parse('I want O to be placed on 6')
    ['Place', ['O', 6]]
    >>> in_game_parse('Please put X on 8')
    ['Place', ['X', 8]]
    >>> in_game_parse('Would you put O on 2')
    ['Place', ['O', 2]]
    >>> in_game_parse('7 X 5')
    ['Place', ['X', 5]]
    >>> in_game_parse('X O 3')
    ['Place', ['X', 3]]
    >>> in_game_parse('O 4 3')
    ['Place', ['O', 4]]
    >>> in_game_parse('This is random gibberish')
    Traceback (most recent call last):
    SyntaxError: Symbol or Place is missing
    """
    tokens = line.split()
    if not tokens:
        raise SyntaxError('No Command Given')
    "*** YOUR CODE HERE ***"
    for token in tokens:
        if 'Reset' in token:
            return ['Reset']
    exp = ['Place', [None, None]]
    symbols = ['X', 'O']
    places = [str(i) for i in range(9)]

    def check_int(s):
        try: 
            int(s)
            return True
        except ValueError:
            return False

    while tokens:
        token = tokens.pop(0)
        "*** YOUR CODE HERE ***"
        if not exp[1][0] and symbols[0] in token:
            exp[1][0] = symbols[0]
        elif not exp[1][0] and symbols[1] in token:
            exp[1][0] = symbols[1]
        elif not exp[1][1] and exp[1][0] is not None and check_int(token):
            exp[1][1] = int(token)
    return exp
    raise SyntaxError("Symbol or Place is missing")

def end_game_parse(line):
    """ Takes in input from a user after the game has ended.
    The line is a response to the question "Would you like to play another game?"
    This input can correspond to a 'New' expression, an 'End' expression, or 
    None if no expression was found.

    To determine the expression, we look at the first letter of each word in the line.
    If the first letter of a word is 'y' or 'Y', the command is 'New'.
    If the first letter of a word is 'n' or 'N', the command is 'End'.
    If both 'y' and 'n' appear in the first letters of words in the input, we use whichever letter came first.
    
    >>> end_game_parse("yes")
    ['New']
    >>> end_game_parse("no")
    ['End']
    >>> end_game_parse("I do not like this game.") # 'not' begins with 'n'
    ['End']
    >>> end_game_parse("I could play against you all day") # 'you' begins with 'y'
    ['New']
    >>> end_game_parse("Purple snacks never yaks")
    ['End']
    >>> end_game_parse("There are zero valid commands in this line")
    """
    tokens = line.split()
    while tokens:
        token = tokens.pop(0)
        if token[0] == 'n':
            return ['End']
        elif token[0] == 'y':
            return ['New']
    return None


def ttc_eval(board, exp):
    """ Takes in the game board and the expression returned from a parse function
    and evaluates the expression given.

    Be sure to call ttc_apply whenever you want to call a function.

    If the command is 'Reset' or 'New', we begin a new game.  Remember that new_game
    takes in an intro message.  (We have no restrictions on what the message can be.)
    If the command is 'Place', we want to place a piece on the given board.
    (Look at the tictactoe.py file to figure out how to do this)
    If the command is 'End', we do nothing.

    >>> b = Board(False) # Create a board that doesn't print unnecessarily
    >>> line = "Place X at 7"
    >>> exp = in_game_parse(line)
    >>> ttc_eval(b, exp)
    'X has been placed in space 7'
    >>> ttc_eval(b, in_game_parse("O in for 6"))
    'O has been placed in space 6'
    """
    if exp[0] == 'Reset' or exp[0] == 'New':
        return ttc_apply(new_game, "The game has been reset!")
    elif exp[0] == 'Place':
        return ttc_apply(board.place_piece, exp[1])

def ttc_apply(operator, operand):
    """Applies the operator on the given operand.

    (This is a very simple function.)

    >>> ttc_apply(lambda x: x*x, 7)
    49
    >>> ttc_apply(lambda y: True, False)
    True
    """
    "*** YOUR CODE HERE ***"
    return operator(operand)

def new_game(message):
    """ Starts a new game with the given introductory message."""
    print(message)
    winner = False
    board = Board()
    # Run the game until the game is over
    while not board.terminal_state():
        try:
            line = input('ttc> ')
            exp = in_game_parse(line)
            ttc_eval(board, exp)
        except (KeyboardInterrupt, EOFError, SystemExit):
            print('Bye!')
            return
        except (SyntaxError, NameError, KeyError, TypeError, IndexError, InvalidPieceError, InvalidSpaceError) as e:
            print('Error:', e)
    # Determine whether to restart or end the session.
    while True:
        line = input("Would you like to play another game? ")
        exp = end_game_parse(line)
        if exp is not None:
            ttc_eval(board, exp)
            return

start_message = "Welcome to TicTacToe. The first player is 'X' and the second is 'O'. Please use Capitals."

if __name__ == '__main__':
    try:
        new_game(start_message)
    except ImportError as e:
        print(e)

