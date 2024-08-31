# Welcome to Treasure Island.
# Your mission is to find the treasure.
# You're at a cross road. Where do you want to go?
#   Type "left" or "right".

# Right:
# You fell into a hole. Game Over.

# Left:
# You've come to a lake. There is an island in the middle of the lake.
#   Type "wait" to wait for a boat. Type "swim" to swim across.

# Swim:
# You get attacked by an angry trout. Game Over

# Wait:
# You arrive at the island unharmed. There is a house with 3 doors.
#   One red, one yellow and one blue. Which color do you choose?

# Red:
# It's a room full of fire. Game Over.

# Yellow:
# You found the treasure! You Win!

# Blue:
# You enter a room of beasts. Game Over.

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

choice1 = input("You're at a cross road. Where do you want to go?\n\tType \"left\" or \"right\" ")

if(choice1.lower() == 'right'):
  print('You fell into a hole. Game Over.')
else:
  choice2 = input("You've come to a lake. There is an island in the middle of the lake.\n\
\tType \"wait\" to wait for a boat. Type \"swim\" to swim across. ")
  if(choice2.lower() == 'swim'):
    print("You get attacked by an angry trout. Game Over.")
  else:
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors.\n\
\tOne red, one yellow, and one blue. Which color do you choose? ")
    if(choice3.lower() == 'red'):
      print("It's a room full of fire. Game Over.")
    elif(choice3.lower() == 'blue'):
      print("You enter a room of beasts. Game Over.")
    else:
      print("You found the treasure! You Win!")