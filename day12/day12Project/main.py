from random import randint

# Get random number between 1 and 100
random_number = randint(1, 100)

print('Welcome to the Number Guessing Game!\nI\'m thinking of a number between 1 and 100.')

# Ask for user to set difficulty, easy/hard
def get_difficulty():
  while True:
    choice = input("Choose a difficulty. Type 'easy' or 'hard: ").lower()
    if choice == 'easy' or choice == 'hard':
      return choice
    
def set_turns(dif):
  if dif == 'easy':
    return 10
  else:
    return 5
  
def check_answer(guess, num):
  if guess == num:
    print(f"You got it! The answer was {num}.")
    return True
  else:
    if guess > num:
      print('Too high.')
    else:
      print('Too low.')
    return False
  
def turns_remain(num):
  if num > 1:
    return 's'
  else:
    return ''

# Set difficulty
difficulty = get_difficulty()

# Set number of turns based on difficulty picked
turns = set_turns(difficulty)

while True:
  
  if turns > 0:
    print(f'You have {turns} attempt{turns_remain(turns)} remaining to guess the number.')

    # Ask user to guess the number
    guess = int(input('Make a guess: '))

    # Check guess vs selected random number
    if check_answer(guess, random_number):
      break
    else:
      turns -= 1
      if turns > 0:
        print('Guess again.')
  else:
    print("You've run out of guesses. You lose.")
    break