#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = str(number)
last1 = n[-1:]
last = int(last1) if number >= 0 else -1 * int(last1)
if last > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif last == 0:
    print(f"Last digit of {number} is {last} and is 0")
else:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
