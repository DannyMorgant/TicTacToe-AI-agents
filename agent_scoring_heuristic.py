import random

def get_position_score(pattern_scores, game):
  """Receives a dictionary {pattern : score} as input, as well as a game object.
  Returns the score of the current position as an int or float"""

  counts = game.count_patterns(pattern_scores.keys(), game.get_active_player())
  score = 0
  for i, p in enumerate(pattern_scores.keys()):
    score += counts[i] * pattern_scores[p]
  return score

def scoring_heuristics(game):
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
  move_list = game.get_valid_moves()
  #calculates the score of each valid move
  move_scores = {}
  g = game.copy()
  cboard, c_aplayer = game.get_state()
  for m in move_list:
    g.set_state(cboard, c_aplayer)
    g.play_move(m)
    score = get_position_score(pattern_scores, g)
    try:
      move_scores[score].append(m)
    except:
      move_scores[score] = [m]
  return random.choice(move_scores[ max(move_scores.keys()) ])