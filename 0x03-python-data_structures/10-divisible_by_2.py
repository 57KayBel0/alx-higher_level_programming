#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # create an empty list to store the results
    result = []
    # loop through each element in the original list
    for num in my_list:
        # check if the element is divisible by 2
        if num % 2 == 0:
            # append True to the result list
            result.append(True)
        else:
            # append False to the result list
            result.append(False)
    # return the result list
    return result
