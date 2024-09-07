# Clear screen after each bidder
def clear_screen():
  from os import system

  system('cls || clear')

def get_highest_bidder(dict):
  name = ''
  bid = 0

  for key in dict:
    if dict[key] > bid:
      name = key
      bid = dict[key]

  return name, bid

# Create 'silent auction'
print('Welcome to the secret auction program.')

# Create dictionary to hold names and bids.
bidders = {}

while True:

  # Ask user for name
  bidder_name = input('What is your name?: ')

  # Ask user for bid amount
  bidder_amount = int(input("What's your bid?: $"))

  # Store bidder information in dictionary
  bidders[bidder_name] = bidder_amount

  # After bid is entered, ask if any more bidders.
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

  # If yes, clear screen and ask for next 'bidder' name.
  if more_bidders == 'yes':
    clear_screen()
  else:

    # Show winning bidder name and bid amount.
    name, bid = get_highest_bidder(bidders)
    print(f'The winner is {name} with a bid of ${bid}.')
    break