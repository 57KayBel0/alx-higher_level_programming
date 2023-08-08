#!/usr/bin/python3
import random
number = random.randint(-10, 10)
for number in range(1, 10):
    if number > 0:
	print("is positive")
    elif number == 0:
	print("is zero")
    else:
	print("negative")
