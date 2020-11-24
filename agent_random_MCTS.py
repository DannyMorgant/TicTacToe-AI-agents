import random
from agent_random import random_agent

def random_mcts(game, iters=100):
  """ Implementation of Monte Carlo Tree Search
  """

  def play_game(dimensions, agent1, agent2, game):
    board, player = game.get_state()
    valid_moves = game.get_valid_moves()
    while valid_moves:
      if player == 'X':
        game.play_move(agent1(game))
      if player == 'O':
        game.play_move(agent2(game))
      end, winner = game.check_win()
      if end:
        valid_moves = False
      else:
        board, player = game.get_state()
        valid_moves = game.get_valid_moves()
    return game

  valid_moves = game.get_valid_moves()
  dims = game.get_shape()
  move_scores = {}
  player = game.get_active_player()
  gamecopy = game.copy()
  cboard, c_aplayer = game.get_state()
  for m in valid_moves:
    for i in range(iters):
      gamecopy.set_state(cboard, c_aplayer)
      res = play_game(dims, random_agent, random_agent, gamecopy)
      if (player=='X' and res=='1-0') or (player=='O' and res=='0-1'):
        try:
          move_scores[m] += 1
        except:
          move_scores[m] = 1
      elif res=='0-1':
        try:
          move_scores[m] += .5
        except:
          move_scores[m] = .5
      else:
        try:
          move_scores[m] -= .2
        except:
          move_scores[m] = -.2

  best = (move_scores[valid_moves[0]], valid_moves[0])
  for m in valid_moves[1:]:
    if move_scores[m] > best[0]:
      best = (move_scores[m], m)
  return best[1]