from random import choice

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''',
'''  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', 
'''  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words_library = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

# Check if start of new game
game_start = True

# Letters to be uncovered
letters_arr = []

# Default to add random word
word_to_guess = ''

# Keep track of letters guessed.
guessed_letters = []

# Keep track of 'lives'(turns)
starting_lives = 6
lives = 6

end_of_game = False

# Game Loop
while True:

  if game_start:

    # Set starting lives
    lives = starting_lives

    # Get random word from words library.
    word_to_guess = choice(words_library)

    # Create empty spots from word to be shown to user.
    letters_arr = []
    for letter in word_to_guess:
      letters_arr.append('_')

    # Change game start checker so game init doesn't run again.
    game_start = False

  # Show how many letters there are total.
  print(f'Word to guess: {(' ').join(letters_arr)}\n')

  # Ask user for letter.
  pick_letter = input('Guess a letter: \n')

  # If user selects same letter twice, give message.
  if pick_letter in guessed_letters:
    print("You have already guessed that letter, try another!")
    continue
  elif pick_letter in word_to_guess:

    # Check guessed letter against ALL letters in word.
    for i in range(len(word_to_guess)):
      if(word_to_guess[i] == pick_letter):

      # If ANY letter in word matches guess, show ALL matching letters.
        letters_arr[i] = word_to_guess[i]
    print(letters_arr)

  else:

    # If incorrect guess, show message, lose life.
    print(f'You guessed {pick_letter}, that\'s not in the word. You lose a life.')
    lives -= 1

  # Check win/lose
  if lives == 0:
    print(f"You've run out of lives. The word was {word_to_guess}.")
    end_of_game = True
  elif not '_' in letters_arr:
    print("You guessed the word! You win!!")
    end_of_game = True

  if end_of_game:
    play_again = input('Would you like to play again? Yes or No: ').lower()

    if play_again == 'yes':
      game_start = True
      end_of_game = False
      continue
    else:
      break

  # Show hangman progression
  hangman_image = len(HANGMANPICS) - lives
  print(HANGMANPICS[hangman_image])

  # Show remaining 'lives'(turns).
  print(f'Lives remaining: {lives}')