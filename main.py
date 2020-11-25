import TicTacToe
import random
import time

def compare_agents(dimensions, agent1, agent2, iterations=100):
  def play_game(dimensions, agent1, agent2):
    game = TicTacToe.Board(dimensions[0], dimensions[1])
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

  def agent_evaluator(dimensions, agent1, agent2, iterations=100):
    agent1_score = 0
    agent2_score = 0
    for i in range(iterations):
      result = play_game(dimensions, agent1, agent2)
      end, winner = result.check_win()
      if winner == '1-0':
        agent1_score += 1
      elif winner == '0-1':
        agent2_score += 1
      else:
        agent1_score += .5
        agent2_score += .5
      print("Games: {0}, {1}: {2:.3g}% winrate, {3}: {4:.3g}%          ".format(i+1, agent1.__name__, 100*agent1_score/(i+1), agent2.__name__, 100*agent2_score/(i+1)), end='\r')
    print()
    return agent1_score/iterations, agent2_score/iterations

  start = time.time()
  
  score1, score2 = agent_evaluator(dimensions, agent1, agent2, iters)
  print(agent1.__name__,  'as X,', score1, agent2.__name__, 'as O,', score2)
  print()
  score1, score2 = agent_evaluator(dimensions, agent2, agent1, iters)
  print(agent2.__name__,  'as X,', score1, agent1.__name__, 'as O,', score2)
  print()
  print( 'Simulation took {} mins for {} iterations'.format(int((time.time() - start)/60), iters*2) )
  return

if __name__ == '__main__':
  from agent_minimax import minimax_agent, minimax
  from agent_random import random_agent
  from agent_naive_heuristic import naive_heuristics
  from agent_scoring_heuristic import scoring_heuristics
  from agent_random_MCTS import random_mcts

  dimensions = (10,10)
  iters = 50

  random = random_agent
  naive = naive_heuristics
  scoring = scoring_heuristics
  minimax = minimax_agent
  mcts = random_mcts
  
  print('Board size: ', dimensions, end='\n'+'_'*70+'\n')

  to_test = [(random, naive),
             (naive, mcts), 
             (scoring, minimax), 
             (minimax, mcts), 
             (mcts, mcts)]
  
  for t in to_test:
    compare_agents(dimensions, t[0], t[1], iters)
    print('_'*70+'\n')