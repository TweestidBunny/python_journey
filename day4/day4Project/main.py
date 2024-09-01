from random import randint

# Get random number between 0 and 2
computer_choice = randint(0, 2)

while True:
  player_choice = int(input('Pick a number between 0 and 2: '))

  if player_choice < 0 or player_choice > 2:
    print("Choice MUST be between 0 and 2!!!")
  else:
    break

# Add ascii art to list
art = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

computer_choice_art = art[computer_choice]
player_choice_art = art[player_choice]

# Print ascii art for both choices.
choices = f"{player_choice_art} vs {computer_choice_art}"

tie = False
winner = ''
beats = ''

# Compare player choice against computer choice
if player_choice == 0:
  if computer_choice == 1:
    winner = 'Computer'
  elif computer_choice == 2:
    winner = 'Player'
elif player_choice == 1:
  if computer_choice == 0:
    winner = 'Player'
  elif computer_choice == 2:
    winner = 'Computer'
else:
  if computer_choice == 0:
    winner = 'Computer'
  elif computer_choice == 1:
    winner = 'Player'

if player_choice == computer_choice:
  tie = True
  show_winner = 'It\'s a tie!'

if (player_choice == 0 or computer_choice == 0) and (player_choice == 1 or computer_choice == 1):
  beats = 'Paper covers rock!'
elif (player_choice == 1 or computer_choice == 1) and (player_choice == 2 or computer_choice == 2):
  beats = 'Scissors cuts paper!'
elif (player_choice == 2 or computer_choice == 2) and (player_choice == 0 or computer_choice == 0):
  beats = 'Rock crushes scissors!'

# Print winner.
print(choices)
if not tie:
  show_winner = f"{winner} wins!"
  print(beats)
print(show_winner)