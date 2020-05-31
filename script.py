from random import choice
from time import sleep

def flip_coin():
  print("\nGuess a side:")
  guess = get_input(coin)
  print('\nYour choice is {0}!'.format(guess))
  print('\nFlipping the coin...\n')
  result = choice(list(coin.values()))
  sleep(2)
  if result == guess:
    print("{0}! You're lucky!\n".format(result))
    return 'Win'
  else:
    print("{0}! What a shame!\n".format(result))
    return 'Lose' 

def throw_dice():
  print("\nGuess a result!")
  guess = get_input(range(1,7))
  print('\nYour choice is {0}!'.format(guess))
  print('\nThrowing the dice...\n')
  result = str(choice(range(1, 7)))
  sleep(2)
  if result == guess:
    print("{0}! You're lucky!\n".format(result))
    return 'Win'
  else:
    print("{0}! What a shame!\n".format(result))
    return 'Lose' 

def get_input(options):
  if type(options) is dict:
    for option in options:
      print(str(option) + ' for ' + str(options[option]))
    while True:
      answer = input('\n')
      if answer in options:
        return options[answer]
      else:
        print('\nNo such option! Try again!')
  if type(options) is range:
    print('From {0} to {1}:'.format(min(options), max(options)))
    while True:
      answer = input('\n')
      if int(answer) in options:
        return answer
      else:
        print('\nNo such option! Try again!')
    

#Set up variables
coin = {'H': 'Head', 'T': 'Tail'}
games = {'C': 'Coin', 'D': 'Dice'}
yes_no = {'Y': 'Yes', 'N': 'No'}
play = 'Yes'
games_played = 0
games_won = 0

#Start game
print("Let's start!")
while play == 'Yes':
  result = ''
  print('\nWhat you wanna play?\n')
  game = get_input(games)
  if game == 'Coin':
    game_result = flip_coin()
  elif game == 'Dice':
    game_result = throw_dice()
  games_played += 1
  if game_result == 'Win':
    games_won += 1
  print('You made {0} lucky guesses in {1} games!\n'.format(games_won, games_played))
  sleep(1)
  print("Wanna play again?\n")
  play = get_input(yes_no)