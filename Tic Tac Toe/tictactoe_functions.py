import math

EMPTY = '-'

def is_between(value, min_value, max_value):
    """ (number, number, number) -> bool

    Precondition: min_value <= max_value

    Return True if and only if value is between min_value and max_value,
    or equal to one or both of them.

    >>> is_between(1.0, 0.0, 2)
    True
    >>> is_between(0, 1, 2)
    False
    """
    between = False
    if ((value == min_value) or (value == max_value)):
        between = True
    elif ((value > min_value) and (value < max_value)):
        between = True
    return (between)

def game_board_full (game_board):
    """ (str) -> bool
    
    Return True if and only if the game_board does not contain any
    EMPTY characters.
    
    >>> game_board_full("XOXOOXO-X")
    False
    >>> game_board_full("XOXOXOOXO")
    True
    """
    full = False
    if (game_board.find(EMPTY) == -1):
        full = True
    return (full)

def get_board_size (game_board):
    """ (str) -> int
    
    Precondition: The game_board that is given is a perfect square
    
    Return the side length of the game_board knowing that the 
    board has to be a perfect square
    
    >>> get_board_size("XOXO-X-XX")
    3
    >>> get_board_size("XOXO")
    2
    """
    size = 0
    length = 0
    length = len(game_board)
    size = int(length ** 0.5)
    return (size)

def make_empty_board (game_board_size):
    """ (int) -> str
    
    Return and empty game board that is represented in a string
    given the game_board_size
    
    >>>make_empty_board(3)
    "---------"
    >>make_empty_board(2)
    "----"
    """
    empty_game_board = EMPTY * (game_board_size ** 2)
    return (empty_game_board)

def get_position (row_index, col_index, game_board_size):
    """ (int, int, int) -> int
    
    Return the position of the specific cell relative to the game board
    while given the row_index, col_index, and the game_board_size
    
    >>>get_position(2, 2, 3)
    4
    >>>get_position(3, 2, 4)
    9
    """
    str_index = (row_index - 1) * game_board_size + col_index - 1
    return (str_index)

def make_move (symbol, row_index, col_index, game_board):
    """ (str, int, int, str) -> str
    
    Precondition: The desired index in the game_board is an EMPTY character
    
    Return the new game_board after adding the given symbol to it at the
    specific place given by the row_index and the col_index
    
    >>>make_move("X", 2, 2, "XOXO--X-O")
    "XOXOX-X-O"
    >>>make_move("O", 1, 1, "----")
    "O---"
    """
    length = get_board_size (game_board)
    position = get_position (row_index, col_index, length)
    print (position)
    part_1 = game_board[:(position)]
    part_1 = part_1 + symbol
    part_2 = game_board[(position + 1):]
    new_game_board = part_1 + part_2
    return (new_game_board)

def extract_line (game_board, direction, row_or_col_number):
    """ (str, str, int) -> str
    
    Return a string conating a line of symbols given the
    game_board, the direction, and the row_or_column_number
    
    >>>extract_line("XOXOXXOXO", "down", 1)
    "XOO"
    >>>extract_line("XOOX", up_diagonal, 1)
    "OO"
    """
    position = 0
    count = 1
    length = get_board_size (game_board)
    extracted_line = ""
    if (direction == "across"):
        position = get_position (row_or_col_number, 1, length)
        extracted_line = game_board[position:(position + length)]
    elif (direction == "down"):
        position = get_position (1, row_or_col_number, length)
        while (count <= length):
            extracted_line = extracted_line + game_board[position]
            position = position + length
            count = count + 1
    elif (direction == "up_diagonal"):
        position = get_position (length, 1, length)
        while (count <= length):
            extracted_line = extracted_line + game_board[position]
            position = position - (length - 1)
            count = count + 1
    elif (direction == "down_diagonal"):
        position = get_position (1, 1, length)
        while (count <= length):
            extracted_line = extracted_line + game_board[position]
            position = position + (length + 1)
            count = count + 1
    return (extracted_line)

