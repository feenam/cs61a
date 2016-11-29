TOPLEFT = 0
TOPCENTER = 1
TOPRIGHT = 2
MIDLEFT = 3
MIDCENTER = 4
MIDRIGHT = 5
BOTLEFT = 6
BOTCENTER = 7
BOTRIGHT = 8

ALLSPACES  = [TOPLEFT,TOPCENTER,TOPRIGHT,MIDLEFT,MIDCENTER,MIDRIGHT,BOTLEFT,BOTCENTER,BOTRIGHT]
ROWS = [[TOPLEFT, TOPCENTER, TOPRIGHT], [MIDLEFT, MIDCENTER, MIDRIGHT], [BOTLEFT, BOTCENTER, BOTRIGHT]]
COLUMNS = [[TOPLEFT, MIDLEFT, BOTLEFT], [TOPCENTER, MIDCENTER, BOTCENTER], [TOPRIGHT, MIDRIGHT, BOTRIGHT]]
DIAGONALS = [[TOPLEFT, MIDCENTER, BOTRIGHT], [TOPRIGHT, MIDCENTER, BOTLEFT]]
WINLINES = ROWS + COLUMNS + DIAGONALS


class Board:
    def __init__(self, printing=True):
        """ Creates an empty board. """
        self.spaces = [None for _ in ALLSPACES]
        self.curr = 'X'
        self.printing = printing

    def other(self):
        """ Returns the piece to be placed on the following turn. """
        if self.curr == 'X':
            return 'O'
        elif self.curr == 'O':
            return 'X'

    def is_piece_win(self, piece):
        """ Returns True if the given piece is in a winning position. """
        for line in WINLINES:
            if all([self.spaces[space] == piece for space in line]):
                return True
        return False

    def terminal_state(self):
        """ Returns True if the game is over either by a player winning or all spaces are filled. """
        return self.is_piece_win('X') or self.is_piece_win('O') or all(self.spaces[space] != None for space in ALLSPACES)

    def winner(self):
        """ Returns the piece that has won the game or None if there is no winner."""
        if self.is_piece_win('X'):
            return 'X'
        elif self.is_piece_win('O'):
            return 'O'
        else:
            return None

    def place_piece(self, move):
        """ Takes in a move (a two element list with piece and space) and
        places the input piece on the given space.

        >>> b = Board(False)
        >>> b.place_piece(['X', 2])
        'X has been placed in space 2'
        >>> b.place_piece(['O', 4])
        'O has been placed in space 4'
        """
        piece, space = move
        if self.terminal_state():
            raise GameOverError(self.winner())
        if piece != self.curr:
            raise InvalidPieceError(piece)
        if self.spaces[space] is not None:
            raise InvalidSpaceError(space)
        self.spaces[space] = self.curr
        self.curr = self.other()
        if self.printing:
            self.print_board()
        return piece + " has been placed in space " + str(space)
    
    def space_string(self, space):
        """ For use in print_board. """
        if self.spaces[space] is None:
            return ' '
        else:
            return self.spaces[space]

    def print_board(self):
        """ Prints the board in its current setup. """
        print(' ' + self.space_string(TOPLEFT) + ' | ' + self.space_string(TOPCENTER) + ' | ' + self.space_string(TOPRIGHT))
        print('-----------')
        print(' ' + self.space_string(MIDLEFT) + ' | ' + self.space_string(MIDCENTER) + ' | ' + self.space_string(MIDRIGHT))
        print('-----------')
        print(' ' + self.space_string(BOTLEFT) + ' | ' + self.space_string(BOTCENTER) + ' | ' + self.space_string(BOTRIGHT))

        if self.terminal_state():
            if self.winner() is not None:
                print(self.winner(), "is the winner!")
            else:
                print("Nobody wins.")
        else:
            print(self.curr, "must place a piece.")



class GameOverError(Exception): # Game Over
    def __init__(self, winner):
        self.winner = winner
    def __str__(self):
        return 'The game is already over. You may not place a piece.'

class InvalidSpaceError(Exception): # Piece is already there
    def __init__(self, space):
        self.space = space
    def __str__(self):
        return str(self.space) + ' is not a valid space.'

class InvalidPieceError(Exception): # Opponent's piece instead of your own
    def __init__(self, piece):
        self.piece = piece
    def __str__(self):
        return str(self.piece) + ' cannot be placed for the current player.'


