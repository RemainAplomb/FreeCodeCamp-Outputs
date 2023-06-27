# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
def enemy1(prev_play, counter=[0]):

  counter[0] += 1
  choices = ["R", "R", "P", "P", "S"]
  return choices[counter[0] % len(choices)]


def enemy2(prev_opponent_play, opponent_history=[]):
  opponent_history.append(prev_opponent_play)
  last_ten = opponent_history[-10:]
  most_frequent = max(set(last_ten), key=last_ten.count)

  if most_frequent == '':
    most_frequent = "S"

  ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
  return ideal_response[most_frequent]


def enemy3(prev_opponent_play):
  if prev_opponent_play == '':
    prev_opponent_play = "R"
  ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
  return ideal_response[prev_opponent_play]


def enemy4(prev_opponent_play,
           opponent_history=[],
           play_order=[{
             "RR": 0,
             "RP": 0,
             "RS": 0,
             "PR": 0,
             "PP": 0,
             "PS": 0,
             "SR": 0,
             "SP": 0,
             "SS": 0,
           }]):

  if not prev_opponent_play:
    prev_opponent_play = 'R'
  opponent_history.append(prev_opponent_play)

  last_two = "".join(opponent_history[-2:])
  if len(last_two) == 2:
    play_order[0][last_two] += 1

  potential_plays = [
    prev_opponent_play + "R",
    prev_opponent_play + "P",
    prev_opponent_play + "S",
  ]

  sub_order = {
    k: play_order[0][k]
    for k in potential_plays if k in play_order[0]
  }

  prediction = max(sub_order, key=sub_order.get)[-1:]

  ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
  return ideal_response[prediction]


import random
from difflib import SequenceMatcher

similarity_threshold = 0.7


def calculate_similarity(a, b):
  return SequenceMatcher(None, a, b).ratio()


def player(prev_play,
           opponent_history=[],
           enemy1_history=[],
           enemy2_history=[],
           enemy3_history=[],
           enemy4_history=[],
           our_history=[],
           enemies=[],
           win_rate_threshold=0.6):
  if prev_play:
    opponent_history.append(prev_play)
  else:
    print(enemies)
    enemy1_history.clear()
    enemy2_history.clear()
    enemy3_history.clear()
    enemy4_history.clear()
    our_history.clear()

  window = 15
  if len(our_history) < window:
    # Play randomly for the first 10 rounds
    guess = random.choice(["R", "P", "S"])
    our_history.append(guess)
    enemy1_history.append(enemy1(our_history[-1]))
    enemy2_history.append(enemy2(our_history[-1]))
    enemy3_history.append(enemy3(our_history[-1]))
    enemy4_history.append(enemy4(our_history[-1]))
    return guess

  if len(our_history) == window:
    enemy1_similarity = calculate_similarity(opponent_history[-(window - 1):],
                                             enemy1_history[-(window - 1):])
    enemy2_similarity = calculate_similarity(opponent_history[-(window - 1):],
                                             enemy2_history[-(window - 1):])
    enemy3_similarity = calculate_similarity(opponent_history[-(window - 1):],
                                             enemy3_history[-(window - 1):])
    enemy4_similarity = calculate_similarity(opponent_history[-(window - 1):],
                                             enemy4_history[-(window - 1):])

    if enemy4_similarity >= similarity_threshold:
      enemies.append("enemy4")
    elif enemy2_similarity >= similarity_threshold:
      enemies.append("enemy2")
    elif enemy3_similarity >= similarity_threshold:
      enemies.append("enemy3")
    else:
      enemies.append("enemy1")

  # quincy, mrugesh, kris, abbey
  if enemies[-1] == "enemy4":
    enemy_response = enemy4(our_history[-1])
  elif enemies[-1] == "enemy2":
    enemy_response = enemy2(our_history[-1])
  elif enemies[-1] == "enemy3":
    enemy_response = enemy3(our_history[-1])
  else:
    enemy_response = enemy1(our_history[-1])

  opponent_history.append(enemy_response)

  if enemy_response == "R":
    guess = "P"
  elif enemy_response == "P":
    guess = "S"
  else:
    guess = "R"

  # Add some randomness to the strategy
  random_number = random.random()
  if random_number < 0.2:
    guess = random.choice(["R", "P",
                           "S"])  # Randomly choose a move with 20% probability
  our_history.append(guess)
  return guess
