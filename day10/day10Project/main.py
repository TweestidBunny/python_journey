# Get first and second numbers
def get_number(str):
  return float(input(f'What\'s the {str} number?: '))

# Check if result needs to be formatted to 2 decimals
def check_for_format(num):
  if len(str(num)) > 4:
    return float(f'{num:.2f}')
  elif float(int(num)) == num:
    return int(num)
  return num

# Create functions for the 4 math operators.
def add(num1, num2):
  return num1 + num2

def sub(num1, num2):
  return num1 - num2

def mul(num1, num2):
  return num1 * num2

def div(num1, num2):
  return num1 / num2

# Dictionary to hold data
calculator = {
  "total": None,
  'operand': None,
  'operator': None,

  '+': add,
  '-': sub,
  '*': mul,
  '/': div,
}

while True:

  # Check if fist number needed
  if calculator['total']:

    # Get operator
    print('+\n-\n*\n/')
    calculator['operator'] = input('Pick an operation: ')

    # Get second number
    calculator['operand'] = get_number('second')
  else:

    # Get first number
    calculator['total'] = get_number('first')

  # Check for second number
  if calculator['operand']:
    num1 = check_for_format(calculator['total'])
    num2 = check_for_format(calculator['operand'])
    op = calculator['operator']

    # Calculate
    calculator['total'] = check_for_format(calculator[op](num1, num2))

    # Print result
    print(f'{num1} {op} {num2} = {calculator["total"]}')
  
    again = input(f'Type \'y\' to continue calculating with {calculator["total"]}, or type \'n\' to start a new calculation: ')

    if again.lower() == 'y' or again.lower() == 'n':
      calculator['operand'] = None
      calculator['operator'] = None
    if again.lower() == 'n':
      calculator['total'] = None
    else:
      break