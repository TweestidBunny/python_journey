import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '?', '-', '+']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

numOfLetters = 0
numOfSymbols = 0
numOfNumbers = 0

while True:
  if numOfLetters < 1:
    numOfLetters = int(input("How many letters would you like in your password? "))
    continue
  if numOfSymbols < 1:
    numOfSymbols = int(input('How many symbols would you like? '))
    continue
  if numOfNumbers < 1:
    numOfNumbers = int(input('How many numbers would you like? '))
    continue
  else:
    break

charList = []

for i in range(numOfLetters):
  charList.append(random.choice(letters))
  
for i in range(numOfSymbols):
  charList.append(random.choice(symbols))

for i in range(numOfNumbers):
  charList.append(random.choice(numbers))
  
password = ''

while True:
  random.shuffle(charList)
  if charList[0].isalpha():
    password = charList
    break

joinedPassword = ('').join(password)
print(f'Your password is {joinedPassword}')