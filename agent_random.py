import random

def random_agent(game):
  
  """this agent simply plays a valid move at random"""
  return random.choice(game.get_valid_moves())