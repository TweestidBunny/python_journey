from random import randint

# Get random number between 1 and 100
random_number = randint(1, 100)

print('Welcome to the Number Guessing Game!\nI\'m thinking of a number between 1 and 100.')

difficulty = ''

while difficulty != 'easy' and difficulty != 'hard':
  
  # Ask for user to set difficulty, easy/hard
  difficulty = input('Choose a difficulty. Type \'easy\' or \'hard\': ').lower()

win = None

# Set number of turns based on difficulty picked
turns = 0

if difficulty == 'easy':
  turns = 10
else:
  turns = 5

while True:
  print(f'You have {turns} remaining to guess the number.')
  
  # Ask user to guess the number
  guess = int(input('Make a guess: '))

  # Check guess vs selected random number
  if guess != random_number:
    if guess > random_number:
      print('Too high.')
    elif guess < random_number:
      print('Too low.')

    turns -= 1
  
  # Set win or lose
  if guess == random_number or turns == 0:
    if turns == 0:
      win = False
    else:
      win = True
    break
  
  print('Guess again.')

# Print win or lose
if win == True:
  print(f"You got it! The answer was {random_number}.")
else:
  print(f"You've run out of guesses, you lose.")