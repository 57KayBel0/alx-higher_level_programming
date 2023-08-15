#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    # Check if the matrix is empty
    if not matrix or not matrix[0]:
        print()
        return
    # Iterate over the rows of the matrix
    for row in matrix:
        # Create a list of formatted strings for each element in the row
        formatted_row = ["{:d}".format(element) for element in row]
        # Join the list with spaces and print it
        print(" ".join(formatted_row))
