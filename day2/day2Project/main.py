# Get total bill
# Get tip percentage
# Get total number of people
# Print total each person should pay.

bill = float(input('Total Bill: '))
tip = int(input('Tip Percentage? 10, 12, or 15: '))
persons = int(input('Number of people splitting the bill: '))

# Add 1 for easier math later.
tipPerc = 1 + tip / 100

# Create total with tip
total = bill * tipPerc

# Split bill
total /= persons

# Print total, with format to 2 decimals
print(f"Total bill is {total:.2f}")