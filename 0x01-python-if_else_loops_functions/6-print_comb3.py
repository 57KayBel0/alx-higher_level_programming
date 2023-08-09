#!/usr/bin/python3
for i in range(0, 90, 10):
    for j in range(i, i + 10):
        if j < 89:
            print("{:02d}, ".format(j), end='')
        else:
            print("{:02d}".format(j))
    print(end='\b\b ')
