def islower(c):
    # Check if the input is a single character
    if len(c) != 1:
        return False
    # Get the ASCII code of the character
    ascii_code = ord(c)
    # Check if the ASCII code is in the range of lowercase letters (97-122)
    if ascii_code >= 97 and ascii_code <= 122:
        return True
    # Otherwise, return False
    else:
        return False
