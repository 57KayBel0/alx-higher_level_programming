#!/usr/bin/python3
def uppercase(str):
    for char in str:
        code = ord(char)
        if 97 <= code <= 122:
            code -= 32
            char = chr(code)
        print("{}".format(char), end='')
    print()
