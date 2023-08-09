def add(a, b):
    # Check if the inputs are integers
    if isinstance(a, int) and isinstance(b, int):
        # Return the sum of a and b
        return a + b
    else:
        # Raise an exception if the inputs are not integers
        raise TypeError("Inputs must be integers")
