#!/bin/env python3

# Problem: Receive miles and convert to kilometers

# Enter Miles 5

miles = input("Enter miles ")

# Concert string to int

miles = int(miles)

# Kilometers = miles * 1.60934

kilometers = miles * 1.60934

# 5 miles equals 8.04 kilometers

print("{} miles equals {} kilometers".format(miles, kilometers))
