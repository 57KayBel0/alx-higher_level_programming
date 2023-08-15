#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Initialize the result tuple with zeros
    result = (0, 0)
    # Loop through the first two elements of each tuple
    for i in range(2):
        # Add the corresponding elements if they exist, otherwise add zero
        if i < len(tuple_a):
            result = result[:i] + (result[i] + tuple_a[i],) + result[i+1:]
        if i < len(tuple_b):
            result = result[:i] + (result[i] + tuple_b[i],) + result[i+1:]
    # Return the result tuple
    return result
