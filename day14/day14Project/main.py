# Higher Lower logo
# You're right! Current score: (number)

# Compare A: Shakira, a Musician, from Colombia.

# VS logo

# Against B: Zendaya, an Actress and musician, from United States

# Who has more followers? Type 'A' or 'B':

# To begin!
# Higher Lower Logo
# Compare A:
# VS logo
# Against B:
# Who has more followers?

# Clear screen after each selection
# End of game: 'Sorry, that's wrong. Final score: (number)

from art import logo, vs
from data import data
from random import choice

# Get random choice from options
def get_choice():
  return choice(data)

# Print choice to screen
def print_choice(choice):
  return f'{choice['name']}, a {choice['description']}, from {choice['country']}'

# Create clear screen function
def clear_screen():
  from os import system

  system('cls || clear')
  
score = 0
current = ''
a = ''
b = ''
correct = False
user_selection = ''

while True:
  clear_screen()
  print(logo)

  if correct:
    score += 1
    print(f"You're right! Current score: {score}")
    correct = False
  elif not correct and score > 0:
    print(f'Sorry, that\'s wrong. Final score: {score}')
    break

  # Set choices for 'compare' and 'against'
  if not a:
    a = get_choice()
  
  while not b or b['name'] == a['name']:
    b = get_choice()

  print(f'Compare A: {print_choice(a)}')

  print(vs)

  print(f'Against B: {print_choice(b)}')

  while not user_selection == 'a' and not user_selection == 'b':
    user_selection = input('Who has more followers? Type \'A\' or \'B\': ').lower()

  follower_comparison = a['follower_count'] > b['follower_count']

  if user_selection == 'a' and follower_comparison:
    correct = True
  elif user_selection == 'b' and not follower_comparison:
    correct = True
    a = b

  user_selection = ''
  b = ''