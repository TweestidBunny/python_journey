###### LIFE IN WEEKS ######

# def life_in_weeks(age):
#   end_of_life = 90
#   age_remaining = end_of_life - age
#   weeks_per_year = 52

#   return f'You have {weeks_per_year * age_remaining} weeks left!'

# print(life_in_weeks(39))


###### LOVE CALCULATOR ######

# Enter 2 names
# Loop through each name, and see how many times
#   the letters in 'TRUE' and 'LOVE' occur in the names.

# Combine both numbers to make a number.
# One number for letters in TRUE.
# One number for letters in LOVE.

# The end result will be just those 2 numbers as a string, not "added" together.

# name1 = input("First Name? ")
# name2 = input("Second Name? ")

def true_number(name):
  word = 'true'
  total = 0

  for letter in name:
    if letter.isalpha():
      if letter.lower() in word:
        total += 1
  return total

def love_number(name):
  word = 'love'
  total = 0

  for letter in name:
    if letter.isalpha():
      if letter.lower() in word:
        total += 1
  return total

def calculate_love_score(name1, name2):
  true_total = true_number(name1) + true_number(name2)
  love_total = love_number(name1) + love_number(name2)

  return f'Love Score = {true_total}{love_total}'

print(calculate_love_score('Angela Yu', 'Jack Bauer'))