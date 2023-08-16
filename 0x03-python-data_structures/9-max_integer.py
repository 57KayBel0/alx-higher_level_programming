#!/usr/bin/python3

def max_integer(my_list=[]):
    # If the list is empty, return None
    if not my_list:
        return None
    # Initialize the biggest integer as the first element of the list
    biggest = my_list[0]
    for num in my_list[1:]:
        # If the element is bigger than the biggest, update the biggest
        if num > biggest:
            biggest = num
    # Return the biggest integer
    return biggest
