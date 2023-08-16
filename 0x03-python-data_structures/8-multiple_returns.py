#!/usr/bin/python3

def multiple_returns(sentence):
    # check if the sentence is empty
    if not sentence:
        # return 0 and None as the tuple
        return (0, None)
    # otherwise, return the length and the first character as the tuple
    else:
        # get the length of the sentence
        length = len(sentence)
        # get the first character of the sentence
        first = sentence[0]
        # return the tuple
        return (length, first)
