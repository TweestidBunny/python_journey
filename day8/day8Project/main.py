# Create alphabet to shift through
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Create function to shift letters
def shift_letters(message, shift, code_type):
  letters_list = []
  if code_type.lower() == 'decode':
    shift *= -1

  # Get index of letter in alphabet list and shift
  for letter in message:
    if letter.isalpha():
      starting_index = alphabet.index(letter)
      letters_list.append(alphabet[(starting_index + shift) % 52])
    else:
      letters_list.append(letter)

  return_message = ('').join(letters_list)

  return f'Here\'s the {code_type}d result: {return_message}'

while True:
  # Ask user to 'encode' or 'decode'
  encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrpyt:\n")

  # Get user message
  user_message = input("Type your message:\n")

  # Ask user for the shift amount
  shift_amount = int(input('Type the shift number:\n'))

  # Print result to console
  print(shift_letters(user_message, shift_amount, encode_or_decode))

  # Ask user if they want to go again.
  go_again = input('Type \'yes\' if you want to go again. Otherwise type \'no\'.\n')
  if go_again.lower() == 'no':
    break