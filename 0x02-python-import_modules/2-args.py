#!/usr/bin/python3
import sys

# Get the number of arguments
num_arguments = len(sys.argv) - 1

# Print the number of arguments
if num_arguments == 0:
    print("0 arguments.")
elif num_arguments == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(num_arguments))

# Print the list of arguments
for i, argument in enumerate(sys.argv[1:], start=1):
    print("{}: {}".format(i, argument))
