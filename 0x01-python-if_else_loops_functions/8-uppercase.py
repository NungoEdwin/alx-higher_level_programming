#!/usr/bin/python3
def to_upper(char):
    if ord(char) >= 97 and ord(char) <= 122:
        return (ord(char) - 32)
    else:
        return ord(char)


def uppercase(str):
    new_string = ""
    for character in str:
        new_string += "%c" % to_upper(character)
    print("{:s}".format(new_string))
