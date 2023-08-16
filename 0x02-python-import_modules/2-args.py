#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:] # exclude the script name
    argc = len(argv) # get the number of arguments
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))
    for i, arg in enumerate(argv, 1): # loop through the arguments with index starting from 1
        print("{}: {}".format(i, arg)) # print the position and value of each argument
