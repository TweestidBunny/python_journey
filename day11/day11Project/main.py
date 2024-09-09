from random import shuffle

# Create cards and values
cards = {
  'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
  '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10,
}


# Create Deck
def create_deck():
  deck_list = []
  for card in cards:
    for i in range(4):
      deck_list.append(card)
  return deck_list


# Create Shoe
def create_shoe(num):
  shoe_list = []
  for card in create_deck():
    for i in range(num):
      shoe_list.append(card)
  shuffle(shoe_list)
  return shoe_list


# Calculate hand score
def calculate(hand):
  
  total = 0
  aces = []

  for card in hand:
    total += cards[card]
    if card == 'A':
      aces.append(card)
  
  if len(aces) > 0:
    for ace in aces:
      if total > 21:
        total -= 10

  return total


# Create player and dealer hands
player_cards = []
dealer_cards = []


# Deal Cards
def deal():
  return shoe.pop()


# Deal 2 cards to player and dealer
def initial_deal():
  for i in range(2):
    player_cards.append(deal())
    dealer_cards.append(deal())


# Check if either player gets 21
def check_21(pl_score, dl_score):
  if pl_score == 21 and dl_score != 21:
    print("BlackJack! You Win!!")
  elif pl_score != 21 and dl_score == 21:
    print("BlackJack! You Lose!!")
  else:
    print("2 BlackJacks!! It's a push!!")

  if input("Would you like to play again? yes or no: ").lower() == 'yes':
    return True
  return False


def show_dealer_hand(hand):
  dealer_hand = []
  for i in range(len(hand)):
    if i > 0:
      dealer_hand.append(hand[i])
  return dealer_hand


def show_win(pl_score, dl_score):
  
  print(f'Player: {(' ').join(player_cards)}, Score: {pl_score}')
  print(f'Dealer: {(' ').join(dealer_cards)}, Score: {dl_score} \n')

  if pl_score > dl_score:
    if pl_score > 21:
      return 'Dealer Wins!'
    else:
      return 'Player Wins!'
  elif pl_score < dl_score:
    if dl_score > 21:
      return 'Player Wins!'
    else:
      return 'Dealer Wins!'
  else:
    return 'It\'s a push!'


# Set initial values
shoe = []
shoe_size = 0
choice = ''

while True:

  # Check if game start
  while shoe_size != 3 and shoe_size != 6:
    shoe_size = int(input('What size shoe do you want? 3 or 6: '))
    
  if len(shoe) < 20:
    shoe = create_shoe(shoe_size)

  # Check if first deal is done
  if len(player_cards) < 2:
    initial_deal()
    
  # Check scores
  player_score = calculate(player_cards)
  dealer_score = calculate(dealer_cards)

  player_hand = (' ').join(player_cards)
  dealer_hand = (' ').join(show_dealer_hand(dealer_cards))

  # Print cards and values
  print(f'Player: {player_hand}, Score: {player_score}')

  # Show second dealer card and point value
  print(f'Dealer: {dealer_hand}, Score: {calculate(dealer_hand.split(' '))}\n')

  if player_score == 21 or dealer_score == 21:
    if check_21(player_score, dealer_score):
      player_cards = []
      dealer_cards = []
      continue
    else:
      break

  if choice != 'stand' and player_score < 21:
    choice = input('Hit or Stand? ').lower()
  else:
    choice = 'stand'

  if choice == 'hit':
    player_cards.append(deal())
  elif dealer_score < 17 and player_score < 21:
    dealer_cards.append(deal())
  else:
    print(show_win(player_score, dealer_score))

    if input('Would you like to play again? yes or no: ').lower() == 'yes':
      player_cards = []
      dealer_cards = []
      choice = ''
    else:
      break
