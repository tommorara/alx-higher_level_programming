#!/usr/bin/env python3

# Ask the user to input 2 values and store them in variables num1 and num2

num1, num2 = input('Enter 2 numbers: ').split()

# Convert the strings into regular numbers Integer

num1 = int(num1)

num2 = int(num2)

# Add the values entered and store in sum

sum = num1 + num2

# Subtract the values and store in dirrence

dif = num1 - num2

# Multiply the values and store in product

product  = num1 * num2

# Divide the  values and store in quotient

quotient = num1 / num2

# Find the reminder by using modulus

remainder = num1 % num2

# Print the results for the user

print("{} + {} = {}".format(num1, num2, sum))

print("{} - {} = {}".format(num1, num2, dif))

print("{} * {} = {}".format(num1, num2, product))

print("{} / {} = {}".format(num1, num2, quotient))

print("{} % {} = {}".format(num1, num2, sum))
