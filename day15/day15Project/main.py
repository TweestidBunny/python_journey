resources = {
  'water': 300,
  'milk': 200,
  'coffee': 100,
  'money': 5,
}

MENU = {
  'espresso': {
    'ingredients': {
      'water': 50,
      'coffee': 18,
    },
    'cost': 1.5,
  },
  'latte': {
    'ingredients': {
      'water': 200,
      'milk': 150,
      'coffee': 24,
    },
    'cost': 2.5,
  },
  'cappuccino': {
    'ingredients': {
      'water': 250,
      'milk': 100,
      'coffee': 24,
    },
    'cost': 3.0,
  },
}


# Print report
def print_report():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = resources['money']

    print(f'Water: {water}ml, Milk: {milk}ml, Coffee: {coffee}g, Money: ${money:.2f}')


# Check if enough resources to make drink
def check_resources(drink):
  get_ingredients = MENU[drink]['ingredients']

  check_milk = get_ingredients['milk'] if 'milk' in get_ingredients else 0

  water = resources['water'] >= get_ingredients['water']
  coffee = resources['coffee'] >= get_ingredients['coffee']
  milk = resources['milk'] >= check_milk

  return water and coffee and milk

# Check if money enough to pay for drink
def check_payment(drink, amt):
  drink_cost = MENU[drink]['cost']

  if amt:
    return float(amt) >= drink_cost
  return False

# Give change if payment more than drink cost
def make_change(drink, amt):
  drink_cost = MENU[drink]['cost']

  if amt > drink_cost:
    change = amt - drink_cost
    resources['money'] -= change
    print(f'Change due: {change}')

# Make the drink
def make_drink(drink):
  ingredients = MENU[drink]['ingredients']

  resources['water'] -= ingredients['water']
  resources['coffee'] -= ingredients['coffee']

  if 'milk' in ingredients:
    resources['milk'] -= ingredients['milk']


selection = ''
payment = 0

while True:

  if not selection:
    # Give drink options
    print('Drink options are:\n')
    for drink in MENU:
      print(drink.title())

    # Get user drink selection
    selection = input('\nWhich would you like?: ').lower()

    if selection == 'off':
      break
    elif selection == 'report':
      print_report()
      selection = ''
    elif selection not in MENU:
      print("\nThat is not a drink option, please try again.\n")
      selection = ''
  else:

    if check_payment(selection, payment):
      make_drink(selection)
      print(f'Enjoy your {selection.title()}')
      make_change(selection, payment)
      resources['money'] += payment
      selection = ''
      payment = 0
    else:
      print(f'{selection.title()}: ${MENU[selection]['cost']:.2f}')
      print(f'Amount entered: ${payment}')
      
      payment += float(input('Insert money: '))