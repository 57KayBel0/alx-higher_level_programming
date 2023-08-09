#!/usr/bin/python3
def pow(a, b):
    # initialize result as 1
    result = 1
    # if b is negative, invert a and make b positive
    if b < 0:
        a = 1 / a
        b = -b
    # loop b times
    for i in range(b):
        # multiply result by a
        result *= a
    # return result
    return result
