from random import choice
from time import sleep

def flip_the_coin():
  return choice(list(coin.keys()))
  
def get_input(options):
  for option in options:
    print(str(option) + ' for ' + str(options[option]))
  while True:
    answer = input('\n')
    if answer in options:
      return answer
    else:
      print('\nNo such option! Try again!')

coin = {'H': 'Head', 'T': 'Tail'}
yes_no = {'Y': 'Yes', 'N': 'No'}
play = 'Y'
games_count = 0
correct_guess_count = 0

while play == 'Y':
  print("\nGuess the side:")
  guess = get_input(coin)
  print('\nYour choice is {0}!'.format(coin[guess]))
  games_count += 1
  print('\nFlipping the coin...\n')
  sleep(2)
  flip_result = flip_the_coin()
  
  if flip_result == guess:
    print("{0}! You're lucky!\n".format(coin[flip_result]))
    correct_guess_count += 1
  else:
    print("{0}! What a shame!\n".format(coin[flip_result]))
  print('You made {0} lucky guesses in {1} games!'.format(correct_guess_count, games_count))
  sleep(1)
  print("Wanna play again?\n")
  play = get_input(yes_no)