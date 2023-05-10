#!/usr/bin/python3
def print_last_digit(number):
    the_last_digit = abs(number) % 10
    print(the_last_digit, end="")
    return the_last_digit
