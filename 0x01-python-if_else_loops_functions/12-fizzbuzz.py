#!/usr/bin/python3
# 12-fizzbuzz.py

def fizzbuzz():
    """Print the numbers from 1 to 100 separated by space.
    For multi of three, print Fizz instead of the numb
    For multi of five, print Buzz
    For multi of three and five, print FizzBuzz
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
