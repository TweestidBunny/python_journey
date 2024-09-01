print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheeze? Y or N: ").lower()

total = 0

# work out how much they need to pay based on their size choice.
# S - 15, M - 20, L - 25

if size == 's':
  total += 15
elif size == 'm':
  total += 20
else:
  total += 25

# work out how much to add to their bill based on their pepperoni choice.
# S - 2, M & L - 3

if pepperoni == 'y':
  if size == 's':
    total += 2
  else:
    total += 3

# work out their final amount based on whether they want extra cheese.
# xtra - 1

if extra_cheese == 'y':
  total += 1

print(f"Your final bill is: ${total}.")