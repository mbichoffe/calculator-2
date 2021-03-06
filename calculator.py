# -*- coding: utf-8 -*-

"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *
from functools import reduce

# Your code goes here
# No setup
#repeat forever:
    #read input
    #tokenize input
    #if the first token is "q":
        #quit
    #else:

        #decide which math function to call based on first token
"""
add(int, int) → int
Return the sum of the two input integers.
subtract(int, int) → int
Return the second number subtracted from the first.
multiply(int, int) → int
Multiply the two inputs together and return the result.
divide(int, int) → float
Divide the first input by the second and return a floating point.
square(int) → int
Return the square of the input.
cube(int) → int
Return the cube of the input.
power(int, int) → int
Raise the first input to the power of the second and return the result.
mod(int, int) → int
Divide the first input by the second input and return the remainder.
"""



while True:
    #get user input
    input_string = raw_input(">" )

    #input tokenization:
    tokens = input_string.split(" ")

    lista = tokens[1:]

    result = ""

    # to_int1 = int(tokens[1])
    operator = tokens[0]

    # if len(tokens) == 3:
    #     to_int2 = int(tokens[2])


    if operator == "q":
        print "You decided to quit the program"
        break

    elif operator == "+":
        result = reduce(add, lista)

    elif operator == "-":
        result = reduce(subtract, lista)
    elif operator == "/":
        result = reduce(divide, lista)
    elif operator == "*":
        result = reduce(multiply, lista)
    elif operator == "pow":
        result = reduce(power, lista)
    elif operator == "mod":
        result = reduce(mod, lista)
    elif operator == "square":
        result = map(square, lista)
    elif operator == "cube":
        result = map(cube, lista)
    else:
        print "invalid input. Try again"
        continue
    print result
