#!/usr/bin/python3
for a in range(97, 123):
    if "{:c}".format(a) == 'q' or "{:c}".format(a) == 'e':
        pass
    else:
        print("{:c}".format(a))
