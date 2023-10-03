#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        print("FizzBuzz ", end='') if num % 3 == 0 and num % 5 == 0 \
                else print("Fizz ", end='') \
                if num % 3 == 0 else print("Buzz ", end='') \
                if num % 5 == 0 else print("{:d} ".format(num), end='')
