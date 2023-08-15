#!/usr/bin/python3

def no_c(my_string):
    # Initialize an empty string to store the result
    result = ""
    # Loop through each character in the input string
    for char in my_string:
        # If the character is not c or C, append it to the result
        if char != 'c' and char != 'C':
            result += char
    # Return the result
    return result
