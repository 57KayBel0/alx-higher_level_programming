#!/usr/bin/python3
def print_last_digit(number):
    # Convert the number to a positive integer
    number = abs(number)
    # Get the last digit by using modulo 10
    last_digit = number % 10
    # Print the last digit as a string
    print(str(last_digit), end="")
    # Return the last digit as an integer
    return last_digit
