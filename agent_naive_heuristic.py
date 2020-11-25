import random

def naive_heuristics(game):
  """this agent will play a winning move if there is one.
  If there is not and the opponent threatens to win, he'll block him.
  Otherwise will return a move at random."""
  #if there is a winning move now, plays it
  valid_moves = game.get_valid_moves()
  opp_winning_move = []
  for m in valid_moves:
    #checking if we can win now
    g = game.copy()
    g.play_move(m)
    win, player = g.check_win()
    if win:
      return m
    #checking if the opponent threatens to win
    g = game.copy()
    g.change_active_player()
    g.play_move(m)
    win, player = g.check_win()
    if win:
      opp_winning_move.append(m)
  #we can't win now, so block if opponent is threatening to win
  if opp_winning_move:
    return random.choice(opp_winning_move)
  #otherwise returns a random move
  return random.choice(valid_moves)