#!/usr/bin/python3
for index in range(122, 96, -1):
    if index % 2 != 0:
        index -=  32
    print("{}".format(chr(index)), end="")
