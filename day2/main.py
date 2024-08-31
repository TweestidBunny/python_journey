# This was just a practice within Day 2.
# It is a BMI calculator.
# There was a way to complete this within the course,
#   but I decided to save it in here as well.

# BMI = weight / height ^ 2 (height * height)

# The practice numbers were in metric

height = 1.65
weight = 84

# Height power of 2, reuse variable.
height *= height

bmi = weight / height

# Format to 2 decimals
print(f"{bmi:.2f}")