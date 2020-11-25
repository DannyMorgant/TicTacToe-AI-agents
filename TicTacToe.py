import numpy as np

class Board(object):
  """This class represents the board of a TicTacToe game.
  It contains the information about the state of the game.
  Also contains methods to interact with it from outside."""

  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.board = np.array(['.' for i in range(self.width * self.height)])
    self.board = self.board.reshape(self.width, self.height)
    self.active_player = 'X'
    self.win_pattern = ['1___\n_1__\n__1_\n___1', 
                        '___1\n__1_\n_1__\n1___', 
                        '1111', 
                        '1\n1\n1\n1']

  def copy(self):
    """Returns a copy of the current object"""
    instance = Board(self.width, self.height)
    instance.board = self.board.copy()
    instance.active_player = self.active_player
    return instance

  def get_valid_moves(self):
    """This method returns a list containing all legal moves
    in the current position."""
    valid_moves = []
    for y in range(self.height):
      for x in range(self.width):
        if self.board[x][y] == '.':
          valid_moves.append((x,y))
    return valid_moves

  def change_active_player(self):
    """This method changes the player whose turn it is to play."""
    self.active_player = 'X' if self.active_player=='O' else 'O'
    return

  def get_active_player(self):
    """Returns the player whose turn it currently is to play."""
    return self.active_player

  def play_move(self, move):
    """This method receives a move as input. Move should be a tuple: (x, y), with x and y the coordinates of the square in which the current player plays.
    It adds the move to the current board and advances the turn to the enxt player. """
    self.board[move[0]][move[1]] = self.active_player
    self.change_active_player()
    return

  def get_shape(self):
    """Returns a tuple containing the diensions of the board"""
    return (self.width, self.height)

  def get_state(self):
    """Returns all information about the current game to be processed outside of this class if needed.
    self.board is a numpy array
    self.active_player is a string containg the symbol representing the current player"""
    return self.board, self.active_player

  def set_state(self, board, active_player):
    """This function sets the state of the object to
    a given board state and active player.
    self.board is a numpy array
    self.active_player is a string containg the symbol representing the current player
    """
    self.board = board
    d = self.board.shape
    self.width = d[0]
    self.height = d[1]
    self.active_player = active_player
    return

  def print_board(self):
    """Prints the current game state"""
    print('To play:', self.active_player)
    print(' ' + '_'*(self.height*2-1) + ' ')
    for row in self.board:
      display = ' '.join(row)
      print('|'+display+'|')
    print(' ' + '-'*(self.height*2-1) + ' ')
    return

  def count_patterns(self, pattern_list, player):
    """This method counts the number of occurences of
    each pattern in a pattern list in input, with regards to the active player also given in input.
    player should match a valid self.active_player attribute.
    pattern_list is a list containing pattern_list
    see the method 'convert to patterns' to check the format of the patterns.
    Returns a list containing the number of matches for each pattern, in the same order as in pattern_list."""

    #-----------Helper functions----------------
    def pattern_size(pattern):
      """Returns the shape of the pattern given in input"""
      y = pattern.count('\n') + 1
      p = pattern.split('\n')
      x = len(p) if type(p)==str else len(p[0])
      return x, y

    def convert_to_pattern(arr, active_player):
      """Receives an array and a active player of interest.
      Converts this array into a pattern, which is a 
      string containing the position of X, O, or empty tiles.
      X means player x
      O means player O
      . means empty square
      \n means next row"""
      pat = ''
      dims = arr.shape
      for y in range(dims[1]):
        for x in range(dims[0]):
          if arr[x,y] == active_player:
            l = '1'
          elif arr[x,y] in ('X', 'O'):
            l = 'O'
          else:
            l = '.'
          pat += l
        pat+= '\n'
      return pat[:-1]

    def is_pattern_in(pattern, arr):
      """Returns True if an array contains a pattern, False otherwise.
      Receives as input a pattern and an array converted to pattern format
      X means player x
      O means player O
      . means empty square
      \n means next row
      _ means anything can be in this square
      """
      for i, let in enumerate(pattern):
        #looking for mismatch for the values that are fixed
        if let=='1' and arr[i]!='1':
          return False
        if let=='0' and arr[i]!='0':
          return False
        if let=='.' and arr[i]!='.':
          return False
      #if no mismatch, then the pattern is there
      return True
    
    #-----Beginning of the method's code--------
    pattern_count = []
    for p in pattern_list:
      count = 0
      x, y = pattern_size(p)
      for i in range(self.width - x + 1):
        for j in range(self.height - y + 1):
          if is_pattern_in(p, convert_to_pattern(self.board[i:i+x, j:j+y], player)):
            count += 1
      pattern_count.append(count)
    return pattern_count

  def check_win(self):
    """This functions checks if the game is finished, either by a winner or no more moves can be played.
    Returns a boolean telling if the game is finished,
    as well as the score, as a string"""
    for res in [('X', '1-0'), ('O', '0-1')]:
      win_count = self.count_patterns(self.win_pattern, res[0])
      if sum(win_count)>0:
        return True, res[1]

    #checking full board
    if not self.get_valid_moves():
      return True, "1/2-1/2"

    #No reason to end the game, return False
    return False, None