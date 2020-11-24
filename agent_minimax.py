import random
from agent_scoring_heuristic import get_position_score

def minimax_agent(game, depth=3):
  valid_moves = game.get_valid_moves()
  move_scores = {}
  for m in valid_moves:
    g = game.copy()
    g.play_move(m)
    score = minimax(g, depth-1, False)
    #if we found a winning move, just return it
    if score >= 9000:
      return m
    #otherwise build the dictionary
    try:
      move_scores[score].append(m)
    except:
      move_scores[score] = [m]
  return random.choice( move_scores[max(move_scores.keys())])

def minimax(game, depth, maximizing=False):
  """Recursive evaluation function, implementation of the minimax base algorithm."""
  
  pattern_scores = {'.111': 50,
                    '111.': 50,
                    '1.11': 10,
                    '11.1': 10,
                    '.\n1\n1\n1': 50,
                    '1\n1\n1\n.': 50,
                    '1\n.\n1\n1': 10,
                    '1\n1\n.\n1': 10,
                    '1___\n_1__\n__1_\n___.': 50,
                    '.___\n_1__\n__1_\n___1': 50,
                    '___1\n__1_\n_1__\n.___': 50,
                    '___.\n__1_\n_1__\n1___': 50,
                    '1___\n_1__\n__1_\n___1': 10000, 
                    '___1\n__1_\n_1__\n1___': 10000, 
                    '1111': 10000, 
                    '1\n1\n1\n1': 10000,
                    '.000': -10000,
                    '000.': -10000,
                    '0.00': -10000,
                    '00.0': -10000,
                    '.\n0\n0\n0': -10000,
                    '0\n0\n0\n.': -10000,
                    '0\n.\n0\n0': -10000,
                    '0\n0\n.\n0': -10000,
                    '0___\n_0__\n__.': -10000,
                    '.__\n_0_\n__0': -10000,
                    '0__\n_._\n__0': -10000,
                    '__0\n_0_\n.__': -10000,
                    '__.\n_0_\n0__': -10000,
                    '__0\n_._\n0__': -10000
                    }
  g = game.copy()
  moves = game.get_valid_moves()
  #if end of variation, just evaluate the current position
  if (depth==0 or not moves) and maximizing:
    return get_position_score(pattern_scores, game)
  if (depth==0 or not moves) and not maximizing:
    g.change_active_player()
    return get_position_score(pattern_scores, g)
  #if we reached the max depth to search
  if depth==0:
    return max(get_move_scores(pattern_scores, game).keys())
  #now we can start the recursive step
  else:
    if not maximizing:
      maximizing=True
      value = -100000
      for m in moves:
        g = game.copy()
        g.play_move(m)
        value = max(value, minimax(g, depth-1, maximizing))
        #if we found a winning move we can end exploration
        if value >= 9000:
          return value
      return value
    else:
      maximizing = False
      value = 100000
      for m in moves:
        g = game.copy()
        g.play_move(m)
        value = min(value, minimax(g, depth-1, maximizing))
        #if we found a winning move we can end exploration
        if value <= -9000:
          return value
      return value