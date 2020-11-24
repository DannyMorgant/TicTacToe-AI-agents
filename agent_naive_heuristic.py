import random
from copy import deepcopy

def simple_heuristics(game):
  """this agent will play a winning move if there is one.
  If there is not and the opponent threatens to win, he'll block him.
  Otherwise will return a move at random."""
  #if there is a winning move now, plays it
  valid_moves = game.get_valid_moves()
  opp_winning_move = []
  for m in valid_moves:
    g = deepcopy(game)
    g.play_move(m)
    win, player = g.check_win()
    if win:
      return m
    g = deepcopy(game)
    g.change_active_player()
    g.play_move(m)
    win, player = g.check_win()
    if win:
      opp_winning_move.append(m)
    
  #otherwise, if opponent is threatening to win, blocks him
  if opp_winning_move:
    return random.choice(opp_winning_move)
  #otherwise returns a random move
  return random.choice(valid_moves)