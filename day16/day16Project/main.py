from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

menu = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()

while True:
  selection = input(f'Make Selection *{menu.get_items()}*: ')

  if selection == 'off':
    break
  elif selection == 'report':
    cm.report()
    mm.report()
    print('')
  elif menu.find_drink(selection):
    if cm.is_resource_sufficient(menu.find_drink(selection)):
      print(f'{selection.title()}: ${menu.find_drink(selection).cost}')
      if mm.make_payment(menu.find_drink(selection).cost):
        cm.make_coffee(menu.find_drink(selection))
        print(f'Enjoy your {selection.title()}\n')
