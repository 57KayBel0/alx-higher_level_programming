#!/usr/bin/python3

def print_list_integer(my_list=[]):
    # loop through the list using a for loop
    for item in my_list:
        # print each item using str.format()
        print("{:d}".format(item))
